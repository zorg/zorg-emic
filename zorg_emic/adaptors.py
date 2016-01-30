from zorg.adaptor import Adaptor
import serial


class Serial(Adaptor):

    def __init__(self, options):
        super(Serial, self).__init__(options)

        self.port = options.get("port", "/dev/ttyAMA0")
        self.baudrate = options.get("baudrate", 9600)
        self.serial = serial.Serial(self.port, baudrate=self.baudrate)

    def serial_read(self):
        return self.serial.read()

    def serial_write(self, value):
        self.serial.write(value)
        return value

    def connect(self):
        self.serial.open()

    def disconnect(self):
        self.serial.close()
