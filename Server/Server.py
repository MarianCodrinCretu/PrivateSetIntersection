from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import socket
import csv
from datetime import date, datetime
import aspectlib
from aspectlib import Aspect


import os

from Crypto.PublicKey import RSA

import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol
from NegotiationParameters.NegotiateParameters import NegociateParameters
from NegotiationParameters.NegotiateParametersUtils import NegotiateParametersUtils
from NucleusAlgorithm.NucleusAlgorithm import NucleusAlgorithm
from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation
from OTService.OTService import OTService
from Precomputation.Precomputation import Precomputation
from DataEngineeringService import DataEngineering


class ServerWindow(QWidget):
    def __init__(self, parent=None):
        super(ServerWindow, self).__init__(parent)

        self.data = {}
        self.setMinimumSize(QSize(400, 500))
        self.setMaximumSize(QSize(400, 500))
        self.setWindowTitle("Server")
        QApplication.setStyle("fusion")
        self.move(500, 250)
        self.init_UI()

    def init_UI(self):

        self.tab_layout = QVBoxLayout()
        self.tab_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.tab_layout)

        self.log_textbox = QTextBrowser()
        self.tab_layout.addWidget(self.log_textbox)

        self.add_file_layot = QHBoxLayout()
        self.add_file_value = QLineEdit()
        self.add_file_value.setReadOnly(True)
        self.add_file_button = QPushButton("Choose file")
        self.add_file_button.setFixedWidth(100)
        self.add_file_button.clicked.connect(self.choose_file_clicked)
        self.add_file_layot.addWidget(self.add_file_value)
        self.add_file_layot.addWidget(self.add_file_button)
        self.tab_layout.addLayout(self.add_file_layot)

        self.column_layout = QHBoxLayout()
        self.column_label = QLabel("Choose column:")
        self.column_layout.addWidget(self.column_label)
        self.column_name = QComboBox()
        self.column_layout.addWidget(self.column_name)
        self.column_layout.setContentsMargins(0, 0, 0, 30)
        self.tab_layout.addLayout(self.column_layout)

        self.start_button = QPushButton("Start Server")
        self.start_button.clicked.connect(self.start_button_clicked)
        self.tab_layout.addWidget(self.start_button)

        self.show()

    def choose_file_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(filter='Format(*.csv *.xlsx)')
        if filename is not '':
            self.add_file_value.setText(filename)
            data_service = DataEngineering.DataEngineering(DataEngineering.CSVParser.CSVParser(), DataEngineering.XLSParser.XLSParser())
            self.data = data_service.parse(filename)
            for key in self.data.keys():
                self.column_name.addItem(key)

    def start_button_clicked(self):
        if self.add_file_value.text() == '':
            return 0

        self.start_button.setEnabled(False)
        self.log_textbox.setText("Server started...\n")
        self.log_textbox.setText(self.log_textbox.toPlainText() + "\n" + "Waiting for connection..")
        self.worker = WorkerThread(self.data.get(self.column_name.currentText()))
        self.worker.start()
        self.worker.update_data.connect(self.update_textbox)

    def update_textbox(self, value):
        text = "Client from address " + str(value[0]) + " with the port " + str(value[1]) + " is connected"
        self.log_textbox.setText(self.log_textbox.toPlainText() + "\n" + "\n" + text)


class WorkerThread(QThread):
    update_data = pyqtSignal(tuple)
    data = []

    def __init__(self, data):
        super().__init__()
        self.data = data

    @Aspect
    def log_results(self, value):
        data = yield aspectlib.Proceed
        with open('log.csv', mode='a') as log:
            log_writer = csv.writer(log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            log_writer.writerow(data)

    def emit_data(self, value):
        self.update_data.emit(value)
        return value

    def run(self):

        dictParameters = {
            'lambda': None,
            'sigma': None,
            'm': None,
            'w': None,
            'l1': None,
            'l2': None,
            'hash1': None,
            'hash2': None,
            'prf': None,
            'otVariant': None,
        }

        pubKeyServer = RSA.importKey(open(os.path.join("../server_rsa_public.pem")).read())
        privKeyServer = RSA.importKey(open(os.path.join("../server_rsa_private.pem")).read())

        comSend = ComSend(SocketPool(20))
        comReceive = ComReceive(SocketPool(20))

        transferProtocol = TransferProtocol(
            {'Server IP': Constants.SENDER_ADDRESS, 'Server Port': Constants.SENDER_PORT,
             'Client IP': None, 'Client Port': None}
            , comSend, comReceive, "Thats my Kung Fu", "ABCDE FG HIJK LM")

        address, ip = transferProtocol.receiveInitiateConnection()

        with aspectlib.weave(self.emit_data, self.log_results):
            self.emit_data((address, ip))

        transferProtocol._connectionParams = {'Server IP': Constants.SENDER_ADDRESS,
                                              'Server Port': Constants.SENDER_PORT,
                                              'Client IP': address, 'Client Port': int(ip)}

        transferProtocol.sendConfirmationInitiateConnection()

        negociateParametersUtils = NegotiateParametersUtils()
        negotiateParameters = NegociateParameters(transferProtocol, negociateParametersUtils)
        precomputation = Precomputation()
        otService = OTService(transferProtocol)
        oprfEvaluation = OPRFEvaluation(transferProtocol)

        nucleusAlgorithm = NucleusAlgorithm(self.data, dictParameters, negotiateParameters, precomputation, otService,
                                            oprfEvaluation)
        pubKeyClient = transferProtocol.receiveRSAReceiverPublicKey()
        transferProtocol.sendRSASenderPublicKey(pubKeyServer)
        transferProtocol.receiveIVByRSA(privKeyServer)
        transferProtocol.sendAESKeyByRSA(transferProtocol.aesKey, pubKeyClient)
        nucleusAlgorithm.senderAlgorithmSide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerWindow()
    sys.exit(app.exec_())