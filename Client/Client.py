from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import socket

sock = 0


class ConnectWindow(QWidget):
    def __init__(self, parent=None):
        super(ConnectWindow, self).__init__(parent)
        self.setWindowTitle("Connect to Server")
        QApplication.setStyle("fusion")
        self.setMinimumSize(QSize(400, 400))
        self.setMaximumSize(QSize(400, 400))
        self.move(775, 250)
        self.appWindow = AppWindow()
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
        self.port.setText("1234") # TO BE REMOVED
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
        # address = ('127.0.0.1', 1234)
        global sock
        address = (self.address.text(), int(self.port.text()))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)
        self.appWindow.address_value_label.setText(self.address.text())
        self.appWindow.port_label_value.setText(self.port.text())
        self.appWindow.show()
        self.close()


class AppWindow(QWidget):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        # super().__init__(sys.argv)

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

        # Hash Line
        self.hash_layout = QHBoxLayout()
        self.hash_label = QLabel("Hash:")
        self.hash_layout.addWidget(self.hash_label)
        self.hash_combobox = QComboBox()
        self.hash_combobox.addItem("MD5")
        self.hash_combobox.addItem("SHA1")
        self.hash_combobox.addItem("SHA256")
        self.hash_layout.addWidget(self.hash_combobox)
        self.left_layout.addLayout(self.hash_layout)

        # PRF Line
        self.prf_layout = QHBoxLayout()
        self.prf_label = QLabel("PRF:")
        self.prf_layout.addWidget(self.prf_label)
        self.prf_combobox = QComboBox()
        self.prf_combobox.addItem("PRF1")
        self.prf_combobox.addItem("PRF2")
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
        self.lambda_value = QLineEdit()
        self.lambda_value.setValidator(self.onlyInt)
        self.lambda_value.setFixedWidth(205)
        self.lambda_layout.addWidget(self.lambda_value)
        self.left_layout.addLayout(self.lambda_layout)

        # Sigma Line
        self.sigma_layout = QHBoxLayout()
        self.sigma_label = QLabel("Sigma:")
        self.sigma_layout.addWidget(self.sigma_label)
        self.sigma_value = QLineEdit()
        self.sigma_value.setValidator(self.onlyInt)
        self.sigma_value.setFixedWidth(205)
        self.sigma_layout.addWidget(self.sigma_value)
        self.left_layout.addLayout(self.sigma_layout)

        # M Line
        self.m_layout = QHBoxLayout()
        self.m_label = QLabel("M:")
        self.m_layout.addWidget(self.m_label)
        self.m_value = QLineEdit()
        self.m_value.setValidator(self.onlyInt)
        self.m_value.setFixedWidth(205)
        self.m_layout.addWidget(self.m_value)
        self.left_layout.addLayout(self.m_layout)

        # W Line
        self.w_layout = QHBoxLayout()
        self.w_label = QLabel("W:")
        self.w_layout.addWidget(self.w_label)
        self.w_value = QLineEdit()
        self.w_value.setValidator(self.onlyInt)
        self.w_value.setFixedWidth(205)
        self.w_layout.addWidget(self.w_value)
        self.left_layout.addLayout(self.w_layout)

        # L1 Line
        self.l1_layout = QHBoxLayout()
        self.l1_label = QLabel("L1:")
        self.l1_layout.addWidget(self.l1_label)
        self.l1_value = QLineEdit()
        self.l1_value.setValidator(self.onlyInt)
        self.l1_value.setFixedWidth(205)
        self.l1_layout.addWidget(self.l1_value)
        self.left_layout.addLayout(self.l1_layout)

        # L2 Line
        self.l2_layout = QHBoxLayout()
        self.l2_label = QLabel("L2:")
        self.l2_layout.addWidget(self.l2_label)
        self.l2_value = QLineEdit()
        self.l2_value.setValidator(self.onlyInt)
        self.l2_value.setFixedWidth(205)
        self.l2_layout.addWidget(self.l2_value)
        self.left_layout.addLayout(self.l2_layout)

        # Add File Line
        self.file_layout = QHBoxLayout()
        self.file_name = QLineEdit()
        self.file_name.setReadOnly(True)
        self.file_layout.addWidget(self.file_name)
        self.choose_file_button = QPushButton("Choose File")
        self.choose_file_button.clicked.connect(self.choose_file_clicked)
        self.file_layout.addWidget(self.choose_file_button)
        self.left_layout.addLayout(self.file_layout)

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

    def choose_file_clicked(self):
        self.choose_file_isClicked = True

        filename, _ = QFileDialog.getOpenFileName(filter='CSV(*.csv)')
        if filename is not '':
            self.file_name.setText(filename)

    def start_clicked(self):
        self.start_isClicked = True

    def export_clicked(self):
        self.export_isClicked = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConnectWindow()
    sys.exit(app.exec_())
