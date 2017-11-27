import bluetooth
from CaptureDevice import CaptureDevice

class BluetoothCaptureDevice(CaptureDevice):
    __slots__ = ["_address","_proto","_port","_socket"]

    """
    Given the address of the Bluetooth device to connect, connects to it and
    returns true or false depending if the connection succeded or not

    @param  address     bluetooth address string in the following format
        AA:BB:CC:DD:EE:FF (where A-F are hexadecimal characters)
    """
    def __init__(self, address):
        self._socket = None
        self._address = address

    """
    Connects to the device in the mode set to the port specified. The mode
    will create a socket that will allow communications (mode is a bluetooth
    protocol)

    Mode can be any of the modes in bluetooth module that allow socket creation

    @param  proto   socket communications mode
    @param  port    port where to connect (1 by default)
    @return true or false depending on the result of the operation
    """
    def connect(self, proto=bluetooth.RFCOMM, port=1):
        self._socket = bluetooth.BluetoothSocket(proto)
        try:
            self._socket.connect((self._address,port))
        except Exception as e:
            print("Unable to connect to device %s. " % self._address)
            print("Failed to connect to port %d using proto %s"
            %(port,proto))
            self._socket = None
            return False
        self._proto = proto
        self._port = port
        return True

    """
    Retrieves the current mode of the communications (bluetooth protocol)

    @return constant that represents bluetooth communication mode that is used
    to communicate or None if no communication is active (no connect has been
    done succesfully)
    """
    def getProtocol(self):
        return self._proto

    def getAddress(self):
        return self._address

    def send(self,data):
        print("SND: Sent [%s] (%d bytes)"%(data,len(data)))
        self._socket.send(data)

    def csend(self,data):
        """ send, but with checksum added and btc_command offset applied """
        data = bytes([data[0] + 0x70]) + data[1:]
        checksum = sum(data) & 0xFF
        self.send(data+bytes([checksum]))

    def receive(self, length):
        data = self._socket.recv(length)
        print("RCV: Received [%s] (%d bytes)"%(
            data,len(data)
        ))
    def close(self):
        assert self._socket != None
        self._socket.close()
