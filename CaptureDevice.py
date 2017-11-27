from abc import ABCMeta

class CaptureDevice(object):
    _metaclass_ = ABCMeta
    def connect(self):
        pass
    def send(self, data):
        pass
    def receive(self, length):
        pass
    def close(self):
        pass
