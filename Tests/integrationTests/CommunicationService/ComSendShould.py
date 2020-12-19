import socket
import threading
import time
from unittest import TestCase

from Crypto.Cipher import AES

from CommunicationService.ComSend import ComSend
from CommunicationService.SocketPool import SocketPool


def run_fake_server():
    # Run a server to listen for a connection and then close it
    # inspiration source https://www.devdungeon.com/content/unit-testing-tcp-server-client-python
    server_sock = socket.socket()
    server_sock.bind(('127.0.0.1', 4455))
    server_sock.listen(1)
    server_sock.accept()
    server_sock.close()


class ComSendShould(TestCase):
    key = "Thats my Kung Fu".encode('utf8')
    iv = "ABCDE FG HIJK LM".encode('utf8')

    def test_failWhereConnectionRefused(self):
        comSend = ComSend(SocketPool(5))
        # no server is at the designated address
        with self.assertRaises(ConnectionRefusedError):
            comSend.send(toBeSent="dummyData", ipDestination="127.0.0.1",
                         portDestination=4455,
                         HEADERSIZE=100, aesCipher=AES.new(self.key, AES.MODE_CFB, self.iv))

    def test_successWhenConnectionValid(self):
        comSend = ComSend(SocketPool(5))
        toBeSent = "dummyData"
        ipDestination = "127.0.0.1"
        portDestination = 4455
        HEADERSIZE = 10

        server_thread = threading.Thread(target=run_fake_server)
        server_thread.start()
        time.sleep(0.5)
        comSend.send(toBeSent, ipDestination,
                     portDestination,
                     HEADERSIZE, aesCipher=AES.new(self.key, AES.MODE_CFB, self.iv))

        server_thread.join()
