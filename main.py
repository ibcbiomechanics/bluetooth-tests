from BluetoothCaptureDevice import BluetoothCaptureDevice
import struct
import sys

INERTIAL_ADDRESS=["00:07:80:6F:99:79"]

def run():
    print(socket)

if __name__ == "__main__":
    inertial = BluetoothCaptureDevice(INERTIAL_ADDRESS[0])
    if inertial.connect():
        print("Connected to device")
    else:
        sys.exit()
    # send first command
    try:
        data = struct.pack(">BB",ord('M'),0x30)
        print("sending data")
        inertial.csend(data)
        recv = inertial.receive(1)
        print("received", recv)
    except KeyboardInterrupt:
        print("Failed to communicate")
        inertial.close()
