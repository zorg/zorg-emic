from zorg.adaptor import Adaptor
import serial
import time


class Serial(Adaptor):

    def __init__(self, options):
        super(Serial, self).__init__(options)

        self.port = options.get("port", "/dev/ttyAMA0")
        self.baudrate = options.get("baudrate", 9600)
        self.serial = serial.Serial(self.port, baudrate=self.baudrate)

    def write(self, value):
        waiting = True

        while waiting:
            self.serial.write("\n")
            time.sleep(0.3)
            data = self.serial.read()
            if data == ':':
                self.serial.write("%s\n" % (value))
                waiting = False
            time.sleep(0.5)

        return value

    def connect(self):
        self.serial.open()
        self.serial.write("\n")

        # Pause for 500 milliseconds
        time.sleep(0.05)

    def disconnect(self):
        self.serial.close()
