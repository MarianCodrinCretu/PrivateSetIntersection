import abc
from aspectlib.test import record
# from Transfer import Transfer_Protocol
import MOP


class Mapper:
    def __init__(self, value):
        pass


class Entity(metaclass=abc.ABCMeta):

    @record
    @MOP.sameTransferProtocol
    def __init__(self, transfer_protocol):
        """Uses property setter."""
        self.lambda_ = "lambda"
        self.sigma = "sigma"
        self.m = 3
        self.w = 5
        self.l1 = "l1"
        self.l2 = "l2"
        # print(self.__init__.calls)
        self.transfer_protocol = transfer_protocol

    @property
    def lambda_(self):
        """lambda property"""
        return self._lambda_

    @lambda_.setter
    def lambda_(self, new_value):
        """lambda property setter"""
        self._lambda_ = new_value

    @property
    def sigma(self):
        """sigma property"""
        return self._sigma

    @sigma.setter
    def sigma(self, new_value):
        """sigma property setter"""
        self._sigma = new_value

    @property
    def m(self):
        """m property"""
        return self._m

    @m.setter
    def m(self, new_value):
        """m property setter"""
        self._m = new_value

    @property
    def w(self):
        """w property"""
        return self._w

    @w.setter
    def w(self, new_value):
        """w property setter"""
        self._w = new_value

    @property
    def l1(self):
        """l1 property"""
        return self._l1

    @l1.setter
    def l1(self, new_value):
        """l1 property setter"""
        self._l1 = new_value

    @property
    def l2(self):
        """l2 property"""
        return self._l2

    @l2.setter
    def l2(self, new_value):
        """l2 property setter"""
        self._l2 = new_value

    @property
    def transfer_protocol(self):
        """transfer protocol property"""
        return self._transfer_protocol

    @transfer_protocol.setter
    def transfer_protocol(self, new_value):
        """transfer protocol property setter"""
        self._transfer_protocol = new_value

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'execute_protocol') and
                callable(subclass.execute_protocol) and
                hasattr(subclass, 'get_data') and
                callable(subclass.get_data) or
                NotImplemented)

    @abc.abstractmethod
    def execute_protocol(self, ip: str, port: str, mapper, transfer_protocol):
        """execute transfer protocol with specific parameters"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_data(self):
        """specific implementation for get_data"""
        raise NotImplementedError

    @abc.abstractmethod
    def end_entity(self):
        """specific implementation for get_data"""
        raise NotImplementedError
