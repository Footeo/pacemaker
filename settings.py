#settings.py
import serial

def init():
    global user
    user = "user"

    global ser
    ser = serial.Serial()
    ser.port = 'COM4' #Change based on computer
    ser.baudrate = 115200  
    ser.timeout = 0.5
    ser.dtr = 0
    

