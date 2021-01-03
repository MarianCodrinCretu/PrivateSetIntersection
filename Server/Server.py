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
from ConnectionValidation.ConnectionValidation import ConnectionValidation


class ServerWindow(QWidget):
    def __init__(self, parent=None):
        super(ServerWindow, self).__init__(parent)

        self.data = {}
        self.setMinimumSize(QSize(400, 600))
        self.setMaximumSize(QSize(400, 600))
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

        self.error_label = QLabel()
        self.error_label.setStyleSheet("font-weight: bold; font-size: 20px; color: red")
        self.error_label.setDisabled(True)
        self.error_label.setContentsMargins(-1, 10, -1, 10)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.tab_layout.addWidget(self.error_label)


        # Int Validator
        self.onlyInt = QIntValidator()

        self.server_address_layout = QHBoxLayout()
        self.server_address_label = QLabel()
        self.server_address_label.setText("Server address: ")
        self.server_address_value = QLineEdit()
        self.server_address_value.setFixedWidth(185)
        self.server_address_value.setText("127.0.0.1")
        self.server_address_layout.addWidget(self.server_address_label)
        self.server_address_layout.addWidget(self.server_address_value)
        self.tab_layout.addLayout(self.server_address_layout)

        self.server_port_layout = QHBoxLayout()
        self.server_port_label = QLabel()
        self.server_port_label.setText("Server port: ")
        self.server_port_value = QLineEdit()
        self.server_port_value.setValidator(self.onlyInt)
        self.server_port_value.setFixedWidth(185)
        self.server_port_value.setText("5586")
        self.server_port_layout.addWidget(self.server_port_label)
        self.server_port_layout.addWidget(self.server_port_value)
        self.tab_layout.addLayout(self.server_port_layout)

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

    def check_if_fields_are_filled(self):
        if self.add_file_value.text() == '':
            return False
        elif self.server_address_value.text() == '':
            return False
        elif self.server_port_value.text() == '':
            return False

        return True

    def verify_server_connection_info(self):
        validation_check = ConnectionValidation(self.server_address_value.text(), int(self.server_port_value.text()))

        if validation_check.check_address() is False and validation_check.check_port() is False:
            self.error_label.setText("Incorrect server address and port")
            return False
        elif validation_check.check_address() is False:
            self.error_label.setText("Incorrect server address")
            return False
        elif validation_check.check_port() is False:
            self.error_label.setText("Incorrect server port")
            return False

        return True

    def start_button_clicked(self):
        if self.check_if_fields_are_filled() is False:
            return 0

        if self.verify_server_connection_info() is False:
            self.error_label.setDisabled(False)
            return 0

        self.error_label.setDisabled(True)
        self.start_button.setEnabled(False)
        self.log_textbox.setText("Server started...\n")
        self.log_textbox.setText(self.log_textbox.toPlainText() + "\n" + "Waiting for connection..")
        self.worker = WorkerThread(self.data.get(self.column_name.currentText()),
                                   (str(self.server_address_value.text()), int(self.server_port_value.text())))
        self.worker.start()
        self.worker.update_data.connect(self.update_textbox)

    def update_textbox(self, value):
        text = "Client from address " + str(value[0]) + " with the port " + str(value[1]) + " is connected"
        self.log_textbox.setText(self.log_textbox.toPlainText() + "\n" + "\n" + text)


class WorkerThread(QThread):
    update_data = pyqtSignal(tuple)
    data = []
    server_info = ()

    def __init__(self, data, server_info):
        super().__init__()
        self.data = data
        self.server_info = server_info

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
            {'Server IP': self.server_info[0], 'Server Port': self.server_info[1],
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