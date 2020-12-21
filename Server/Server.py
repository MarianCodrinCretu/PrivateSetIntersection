from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import socket
import csv
from datetime import date, datetime
import aspectlib
from aspectlib import Aspect


class ServerWindow(QWidget):
    def __init__(self, parent=None):
        super(ServerWindow, self).__init__(parent)

        self.setMinimumSize(QSize(400, 400))
        self.setMaximumSize(QSize(400, 400))
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

        self.start_button = QPushButton("Start Server")
        self.start_button.clicked.connect(self.start_button_clicked)
        self.tab_layout.addWidget(self.start_button)

        self.show()

    def choose_file_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(filter='CSV(*.csv)')
        if filename is not '':
            self.add_file_value.setText(filename)

    def start_button_clicked(self):
        self.start_button.setEnabled(False)
        self.log_textbox.setText("Server started...\n")
        self.log_textbox.setText(self.log_textbox.toPlainText() + "\n" + "Waiting for connection..")
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.update_data.connect(self.update_textbox)

    def update_textbox(self, value):
        text = "Client from " + str(value) + " is connected"
        self.log_textbox.setText(self.log_textbox.toPlainText() + "\n" + "\n" + text)


class WorkerThread(QThread):
    update_data = pyqtSignal(tuple)

    @Aspect
    def log_results(self, value):
        data = yield aspectlib.Proceed
        with open('log.csv', mode='a') as log:
            log_writer = csv.writer(log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            log_writer.writerow([date.today().strftime("%b-%d-%Y"), datetime.now().time(), data[0], data[1]])

    def emit_data(self, value):
        self.update_data.emit(value)
        return value

    def run(self):
        address = ('127.0.0.1', 1234)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(address)
        sock.listen(10)

        while True:
            print("Waiting for connection..")
            connection, client_address = sock.accept()
            with aspectlib.weave(self.emit_data, self.log_results):
                self.emit_data(client_address)
            connection.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ServerWindow()
    sys.exit(app.exec_())