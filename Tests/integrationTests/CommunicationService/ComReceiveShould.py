import pickle
import threading
import socket
from unittest import TestCase
import time

from CommunicationService.ComReceive import ComReceive
from CommunicationService.SocketPool import SocketPool
from Crypto.Cipher import AES

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

    def test_receiveConnection(self):

        global bufferZone

        comReceive = ComReceive(SocketPool(5), "Thats my Kung Fu", "ABCDE FG HIJK LM")
        client_thread = threading.Thread(target=run_fake_client, args=(comReceive.aesKey, comReceive.aesIV))
        client_thread.start()
        comReceive.receive(ipToReceive="127.0.0.1",
                           portToReceive=4455,
                           HEADERSIZE=10)

        client_thread.join()
        if bufferZone == "CONNECTION ERROR":
            self.fail()

    def test_receiveConnAndMessage(self):

        global bufferZone
        global messageReceived

        comReceive = ComReceive(SocketPool(5), "Thats my Kung Fu", "ABCDE FG HIJK LM")
        client_thread = threading.Thread(target=run_fake_client, args=(comReceive.aesKey, comReceive.aesIV))
        client_thread.start()
        data = comReceive.receive(ipToReceive="127.0.0.1",
                           portToReceive=4455,
                           HEADERSIZE=10)

        self.assertEqual(data, messageReceived)

        client_thread.join()
        if bufferZone == "CONNECTION ERROR":
            self.fail()



