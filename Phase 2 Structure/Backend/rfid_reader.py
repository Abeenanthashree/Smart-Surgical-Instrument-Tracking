import serial


class RFIDReader:

    def __init__(self):

        self.port = "COM3"

        self.baudrate = 9600

    def connect(self):

        try:

            self.serial = serial.Serial(

                self.port,

                self.baudrate,

                timeout=1

            )

            print("RFID Reader Connected")

        except:

            print("Connection Failed")

    def read_tag(self):

        try:

            if self.serial.in_waiting:

                tag = self.serial.readline()

                return tag.decode().strip()

        except:

            return None
