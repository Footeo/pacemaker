#settings.py
import serial

def init():
    global user
    user = "user"

    global ser
    ser = serial.Serial()
    ser.port = 'COM3'
    ser.baudrate = 115200  #idk about this right now
    ser.timeout = 2
    ser.dtr = 0
    

