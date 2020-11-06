import threading
import socket
from unittest import TestCase
import time

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

    def test_failWhereConnectionRefused(self):

        comSend = ComSend(SocketPool(5))
        #no server is at the designated address
        with self.assertRaises(ConnectionRefusedError):
            comSend.send(toBeSent="dummyData", ipDestination="127.0.0.1",
                          portDestination=4455,
                          HEADERSIZE=100)

    def test_successWhenConnectionValid(self):

        comSend = ComSend(SocketPool(5))
        toBeSent = "dummyData"
        ipDestination = "127.0.0.1"
        portDestination = 4455
        HEADERSIZE=10

        server_thread = threading.Thread(target=run_fake_server)
        server_thread.start()
        time.sleep(0.5)
        comSend.send(toBeSent, ipDestination,
                     portDestination,
                     HEADERSIZE)

        server_thread.join()

            # else:
            #     #child process
            #     # trying to create a server on a different child process
            #     socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #     socketServer.bind(("127.0.0.1", int(portDestination)))
            #     socketServer.listen(5)
            #
            #     connection, address = socketServer.accept()
            #
            #     receivedObject = b''
            #     newMessage = True
            #     msglen = 0
            #     while (True):
            #         msg = connection.recv(16)
            #         if newMessage:
            #             msglen = int(msg[:HEADERSIZE])
            #             newMessage = False
            #
            #         receivedObject += msg
            #
            #         if len(receivedObject) - HEADERSIZE == msglen:
            #             # self._socketPool.release(socket)
            #
            #             self.assertEqual(pickle.loads(receivedObject[HEADERSIZE:]), toBeSent)
            #
















