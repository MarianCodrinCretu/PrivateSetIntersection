import pickle
import threading
import socket
from unittest import TestCase
import time

from CommunicationService.ComReceive import ComReceive
from CommunicationService.SocketPool import SocketPool

bufferZone = ""
message = "I love ASET"
messageReceived = message

def run_fake_client():
    # Run a client which connects to a server
    # inspiration source https://www.devdungeon.com/content/unit-testing-tcp-server-client-python
    global bufferZone
    global message
    try:
        time.sleep(0.5)
        server_sock = socket.socket()
        server_sock.connect(('127.0.0.1', 4455))
        message = pickle.dumps(message)
        message = bytes(f"{len(message):<{10}}", 'utf-8') + message
        server_sock.send(message)

    except ConnectionRefusedError:
        bufferZone = "CONNECTION ERROR"

class ComReceiveShould(TestCase):

    def test_receiveConnection(self):

        global bufferZone

        client_thread = threading.Thread(target=run_fake_client)
        client_thread.start()

        comReceive = ComReceive(SocketPool(5))
        comReceive.receive(ipToReceive="127.0.0.1",
                           portToReceive=4455,
                           HEADERSIZE=10)

        client_thread.join()
        if bufferZone == "CONNECTION ERROR":
            self.fail()

    def test_receiveConnAndMessage(self):

        global bufferZone
        global messageReceived

        client_thread = threading.Thread(target=run_fake_client)
        client_thread.start()

        comReceive = ComReceive(SocketPool(5))
        data = comReceive.receive(ipToReceive="127.0.0.1",
                           portToReceive=4455,
                           HEADERSIZE=10)

        self.assertEqual(data, messageReceived)

        client_thread.join()
        if bufferZone == "CONNECTION ERROR":
            self.fail()



