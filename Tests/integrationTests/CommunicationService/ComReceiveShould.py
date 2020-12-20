import pickle
import socket
import threading
import time
from unittest import TestCase

from Crypto.Cipher import AES

from CommunicationService.ComReceive import ComReceive
from CommunicationService.SocketPool import SocketPool

bufferZone = ""
message = "I love ASET"
messageReceived = message


def run_fake_client(key, iv):
    # Run a client which connects to a server
    # inspiration source https://www.devdungeon.com/content/unit-testing-tcp-server-client-python
    global bufferZone
    global message
    try:
        time.sleep(0.5)
        server_sock = socket.socket()
        server_sock.connect(('127.0.0.1', 4455))
        cipher = AES.new(key, AES.MODE_CFB, iv)
        message = pickle.dumps(message)
        message = cipher.encrypt(message)
        message = bytes(f"{len(message):<{10}}", 'utf-8') + message
        server_sock.send(message)

    except ConnectionRefusedError:
        bufferZone = "CONNECTION ERROR"


class ComReceiveShould(TestCase):
    key = "Thats my Kung Fu".encode('utf8')
    iv = "ABCDE FG HIJK LM".encode('utf8')

    def test_receiveConnection(self):

        global bufferZone

        comReceive = ComReceive(SocketPool(5))
        client_thread = threading.Thread(target=run_fake_client, args=(self.key, self.iv))
        client_thread.start()
        comReceive.receive(ipToReceive="127.0.0.1",
                           portToReceive=4455,
                           HEADERSIZE=10, aesCipher=AES.new(self.key, AES.MODE_CFB, self.iv))

        client_thread.join()
        if bufferZone == "CONNECTION ERROR":
            self.fail()

    def test_receiveConnAndMessage(self):

        global bufferZone
        global messageReceived

        comReceive = ComReceive(SocketPool(5))
        client_thread = threading.Thread(target=run_fake_client, args=(self.key, self.iv))
        client_thread.start()
        data = comReceive.receive(ipToReceive="127.0.0.1",
                                  portToReceive=4455,
                                  HEADERSIZE=10, aesCipher=AES.new(self.key, AES.MODE_CFB, self.iv))

        self.assertEqual(data, messageReceived)

        client_thread.join()
        if bufferZone == "CONNECTION ERROR":
            self.fail()
