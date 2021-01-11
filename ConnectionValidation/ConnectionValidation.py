import socket


class ConnectionValidation:
    _address = ''
    _port = 0

    def __init__(self, address, port):
        self._address = address
        self._port = port

    def check_address(self):
        try:
            socket.inet_aton(self._address)
            return True
        except socket.error:
            return False

    def check_port(self):
        if self._port < 1024 or self._port > 65535:
            return False
        return True

