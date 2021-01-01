from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

import os

from Crypto.PublicKey import RSA

import Constants
from CommunicationService.ComReceive import ComReceive
from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool
from CommunicationService.TransferProtocol import TransferProtocol
from NegotiationParameters.NegotiateParameters import NegociateParameters
from NegotiationParameters.NegotiateParametersUtils import NegotiateParametersUtils
from NegotiationParameters.Constants import *
from NucleusAlgorithm.NucleusAlgorithm import NucleusAlgorithm
from OPRFEvaluation.OPRFEvaluation import OPRFEvaluation
from OTService.OTService import OTService
from Precomputation.Precomputation import Precomputation
from DataEngineeringService import DataEngineering


class ConnectWindow(QWidget):
    def __init__(self, parent=None):
        super(ConnectWindow, self).__init__(parent)
        self.setWindowTitle("Connect to Server")
        QApplication.setStyle("fusion")
        self.setMinimumSize(QSize(400, 400))
        self.setMaximumSize(QSize(400, 400))
        self.move(775, 250)
        self.init_UI()

    def init_UI(self):
        self.tab_layout = QVBoxLayout()
        self.tab_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.tab_layout)

        self.label = QLabel()
        self.label.setText("Connect to server: ")
        self.label.setStyleSheet("font-weight: bold; font-size: 20px")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setContentsMargins(-1, -1, -1, 75)

        self.address = QLineEdit()
        self.address.setStyleSheet("background-color:white")
        self.address.setFixedWidth(170)
        self.address.setPlaceholderText("Address")
        self.address.setText("127.0.0.1") # TO BE REMOVED

        self.port = QLineEdit()
        self.port.setStyleSheet("background-color:white")
        self.port.setFixedWidth(170)
        self.port.setPlaceholderText("Port")
        self.port.setText("5586") # TO BE REMOVED
        self.port.setContentsMargins(-1, -1, -1, 50)

        self.connection_button = QPushButton("Connect", self)
        self.connection_button.setFixedHeight(40)
        self.connection_button.setFixedWidth(170)
        self.connection_button.setStyleSheet("background-color:#FDD20E")
        self.connection_button.clicked.connect(self.passingInformation)

        self.tab_layout.addWidget(self.label)
        self.tab_layout.addWidget(self.address)
        self.tab_layout.addWidget(self.port)
        self.tab_layout.addWidget(self.connection_button)

        self.show()

    def passingInformation(self):

        comSend = ComSend(SocketPool(20))
        comReceive = ComReceive(SocketPool(20))

        transferProtocol = TransferProtocol(
            {'Server IP': self.address.text(), 'Server Port': int(self.port.text()),
             'Client IP': Constants.RECEIVER_ADDRESS, 'Client Port': 5585}
            , comSend, comReceive, "Thats my Kung Fu", "ABCDE FG HIJK LM")

        transferProtocol.initiateConnection()
        transferProtocol.receiveConfirmationInitiateConnection()

        self.appWindow = AppWindow(transferProtocol)
        self.appWindow.address_value_label.setText(self.address.text())
        self.appWindow.port_label_value.setText(self.port.text())
        self.appWindow.show()
        self.close()


class AppWindow(QWidget):
    def __init__(self, transferProtocol, parent=None):
        super(AppWindow, self).__init__(parent)
        # super().__init__(sys.argv)
        self.transferProtocol = transferProtocol
        self.data = {}
        self.setMinimumSize(QSize(900, 600))
        self.setMaximumSize(QSize(900, 400))
        self.setWindowTitle("Client")
        QApplication.setStyle("fusion")
        self.move(500, 250)
        self.choose_file_isClicked = False
        self.export_isClicked = False
        self.start_isClicked = False
        self.init_UI()

    def init_UI(self):
        # Main layouts
        self.tab_layout = QHBoxLayout()
        self.setLayout(self.tab_layout)
        self.left_layout = QVBoxLayout()
        self.left_layout.setAlignment(Qt.AlignCenter)
        self.right_layout = QVBoxLayout()
        self.right_layout.setAlignment(Qt.AlignCenter)

        # Address line
        self.address_layout = QHBoxLayout()
        self.address_label = QLabel("Server Address:")
        self.address_layout.addWidget(self.address_label)
        self.address_value_label = QLabel("Default")
        self.address_layout.addWidget(self.address_value_label)
        self.address_layout.setContentsMargins(-1, 75, -1, -1)
        self.left_layout.addLayout(self.address_layout)

        # Port Line
        self.port_layout = QHBoxLayout()
        self.port_label = QLabel("Port:")
        self.port_layout.addWidget(self.port_label)
        self.port_label_value = QLabel("Default")
        self.port_layout.addWidget(self.port_label_value)
        self.left_layout.addLayout(self.port_layout)

        # Hash1 Line
        self.hash1_layout = QHBoxLayout()
        self.hash1_label = QLabel("Hash1:")
        self.hash1_layout.addWidget(self.hash1_label)
        self.hash1_combobox = QComboBox()
        self.hash1_layout.addWidget(self.hash1_combobox)
        self.left_layout.addLayout(self.hash1_layout)

        # Hash2 Line
        self.hash2_layout = QHBoxLayout()
        self.hash2_label = QLabel("Hash2:")
        self.hash2_layout.addWidget(self.hash2_label)
        self.hash2_combobox = QComboBox()
        self.hash2_layout.addWidget(self.hash2_combobox)
        self.left_layout.addLayout(self.hash2_layout)

        # PRF Line
        self.prf_layout = QHBoxLayout()
        self.prf_label = QLabel("PRF:")
        self.prf_layout.addWidget(self.prf_label)
        self.prf_combobox = QComboBox()
        self.prf_layout.addWidget(self.prf_combobox)
        self.left_layout.addLayout(self.prf_layout)

        # OT Line
        self.ot_layout = QHBoxLayout()
        self.ot_label = QLabel("OT:")
        self.ot_layout.addWidget(self.ot_label)
        self.ot_combobox = QComboBox()
        self.ot_combobox.addItem("OTMultiPoint")
        self.ot_combobox.addItem("OTRandomOracle")
        self.ot_layout.addWidget(self.ot_combobox)
        self.left_layout.addLayout(self.ot_layout)

        # Int Validator
        self.onlyInt = QIntValidator()

        # Lambda Line
        self.lambda_layout = QHBoxLayout()
        self.lambda_label = QLabel("Lambda:")
        self.lambda_layout.addWidget(self.lambda_label)
        self.lambda_combobox = QComboBox()
        self.lambda_combobox.currentIndexChanged.connect(self.change_lambda_options)
        self.lambda_layout.addWidget(self.lambda_combobox)
        self.left_layout.addLayout(self.lambda_layout)

        # Sigma Line
        self.sigma_layout = QHBoxLayout()
        self.sigma_label = QLabel("Sigma:")
        self.sigma_layout.addWidget(self.sigma_label)
        self.sigma_value = QLineEdit()
        self.sigma_value.setValidator(self.onlyInt)
        self.sigma_value.setFixedWidth(200)
        self.sigma_value.setText("60")
        self.sigma_layout.addWidget(self.sigma_value)
        self.left_layout.addLayout(self.sigma_layout)

        # M Line
        self.m_layout = QHBoxLayout()
        self.m_label = QLabel("M:")
        self.m_layout.addWidget(self.m_label)
        self.m_value = QLineEdit()
        self.m_value.setValidator(self.onlyInt)
        self.m_value.setFixedWidth(200)
        self.m_value.setText("64")
        self.m_layout.addWidget(self.m_value)
        self.left_layout.addLayout(self.m_layout)

        # W Line
        self.w_layout = QHBoxLayout()
        self.w_label = QLabel("W:")
        self.w_layout.addWidget(self.w_label)
        self.w_value = QLineEdit()
        self.w_value.setValidator(self.onlyInt)
        self.w_value.setFixedWidth(200)
        self.w_value.setText("633")
        self.w_layout.addWidget(self.w_value)
        self.left_layout.addLayout(self.w_layout)

        # Add File Line
        self.file_layout = QHBoxLayout()
        self.file_name = QLineEdit()
        self.file_name.setReadOnly(True)
        self.file_layout.addWidget(self.file_name)
        self.choose_file_button = QPushButton("Choose File")
        self.choose_file_button.clicked.connect(self.choose_file_clicked)
        self.file_layout.addWidget(self.choose_file_button)
        self.left_layout.addLayout(self.file_layout)

        # Choose column
        self.column_layout = QHBoxLayout()
        self.column_label = QLabel("Choose column:")
        self.column_layout.addWidget(self.column_label)
        self.column_name = QComboBox()
        self.column_layout.addWidget(self.column_name)
        self.left_layout.addLayout(self.column_layout)

        # Run Button
        self.start_button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_clicked)
        self.start_button_layout.addWidget(self.start_button)
        self.start_button_layout.setAlignment(Qt.AlignCenter)
        self.start_button_layout.setContentsMargins(-1, 75, -1, -1)
        self.left_layout.addLayout(self.start_button_layout)

        # Right Layout Design
        # Textbox layout
        self.result_textbox_layout = QHBoxLayout()
        self.result_textbox = QTextBrowser()
        self.result_textbox.setMaximumSize(500, 400)
        self.result_textbox_layout.addWidget(self.result_textbox)
        self.result_textbox_layout.setAlignment(Qt.AlignCenter)
        self.right_layout.addLayout(self.result_textbox_layout)

        # Export Layout
        self.export_button_layout = QHBoxLayout()
        self.export_button = QPushButton("Export")
        self.export_button.setMaximumSize(150, 50)
        self.export_button.clicked.connect(self.export_clicked)
        self.export_button_layout.addWidget(self.export_button)
        self.export_button_layout.setAlignment(Qt.AlignCenter)
        self.export_button_layout.setContentsMargins(-1, -1, -1, 5)
        self.right_layout.addLayout(self.export_button_layout)

        # Splitter
        self.left_widget = QWidget()
        self.left_widget.setLayout(self.left_layout)
        self.right_widget = QWidget()
        self.right_widget.setLayout(self.right_layout)
        self.splitter = QSplitter()
        self.splitter.addWidget(self.left_widget)
        self.splitter.addWidget(self.right_widget)
        self.tab_layout.addWidget(self.splitter)

        self.fill_comboboxes()

    def fill_comboboxes(self):

        for i in HASHES.get(LAMBDAS[0]):
            self.hash1_combobox.addItem(i)

        for i in sorted(HASH_LIST):
            self.hash2_combobox.addItem(i)

        for i in LAMBDAS:
            self.lambda_combobox.addItem(str(i))

        for i in PRFS.get(LAMBDAS[0]):
            self.prf_combobox.addItem(i)

    def change_lambda_options(self):
        # Hashes options are updated
        new_hashes = HASHES.get(int(self.lambda_combobox.currentText()))
        self.hash1_combobox.clear()
        for i in new_hashes:
            self.hash1_combobox.addItem(i)

        # PRF options are updated:
        new_prf = PRFS.get(int(self.lambda_combobox.currentText()))
        self.prf_combobox.clear()
        for i in new_prf:
            self.prf_combobox.addItem(i)


    def choose_file_clicked(self):
        self.choose_file_isClicked = True

        filename, _ = QFileDialog.getOpenFileName(filter="Format(*.csv *.xlsx)")
        if filename is not '':
            self.file_name.setText(filename)
            data_service = DataEngineering.DataEngineering(DataEngineering.CSVParser.CSVParser(), DataEngineering.XLSParser.XLSParser())
            self.data = data_service.parse(filename)
            for key in self.data.keys():
                self.column_name.addItem(key)

    def build_parameters_dict(self):
        dictParameters = {'lambda': str(self.lambda_combobox.currentText()),
                          'sigma': int(self.sigma_value.text()),
                          'm': int(self.m_value.text()),
                          'w': int(self.w_value.text()),
                          'l1': L1,
                          'l2': L2,
                          'hash1': str(self.hash1_combobox.currentText()),
                          'hash2': str(self.hash2_combobox.currentText()),
                          'prf': str(self.prf_combobox.currentText()),
                          'otVariant': str(self.ot_combobox.currentIndex() + 1),
                          }

        return dictParameters

    def check_if_fields_are_filled(self):
        if self.sigma_value.text() == '':
            return False
        elif self.m_value.text() == '':
            return False
        elif self.w_value.text() == '':
            return False
        elif self.file_name.text() == '':
            return False
        else:
            return True

    def start_clicked(self):
        if self.check_if_fields_are_filled() is False:
            return 0

        current_data_list = self.data.get(str(self.column_name.currentText()))
        dictParameters = self.build_parameters_dict()
        print(dictParameters)

        self.worker = WorkerThread(transferProtocol=self.transferProtocol, dictParameters=dictParameters, data=current_data_list)
        self.worker.start()
        self.worker.update_data.connect(self.update_textbox)

    def update_textbox(self, result):
        print(result)
        text = ''
        for i in result:
            text += i + "\n"
        self.result_textbox.setText(text)

    def export_clicked(self):
        self.export_isClicked = True


class WorkerThread(QThread):
    transferProtocol = ''
    dictParameters = {}
    data = []
    update_data = pyqtSignal(list)

    def __init__(self, transferProtocol, dictParameters, data, parent=None):
        QThread.__init__(self, parent)
        self.transferProtocol = transferProtocol
        self.dictParameters = dictParameters
        self.data = data

    def run(self):

        pubKeyClient = RSA.importKey(open(os.path.join("../client_rsa_public.pem")).read())
        privKeyClient = RSA.importKey(open(os.path.join("../client_rsa_private.pem")).read())

        negociateParametersUtils = NegotiateParametersUtils()
        negotiateParameters = NegociateParameters(self.transferProtocol, negociateParametersUtils)
        precomputation = Precomputation()
        otService = OTService(self.transferProtocol)
        oprfEvaluation = OPRFEvaluation(self.transferProtocol)

        # execute
        self.transferProtocol.sendRSAReceiverPublicKey(pubKeyClient)
        pubKeyServer = self.transferProtocol.receiveRSASenderPublicKey()
        self.transferProtocol.sendIVByRSA(self.transferProtocol.aesIV, pubKeyServer)
        self.transferProtocol.receiveAESKeyByRSA(privKeyClient)

        nucleusAlgorithm = NucleusAlgorithm(self.data, self.dictParameters, negotiateParameters, precomputation, otService,
                                            oprfEvaluation)


        self.update_data.emit(nucleusAlgorithm.receiverAlgorithmSide())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConnectWindow()
    sys.exit(app.exec_())
