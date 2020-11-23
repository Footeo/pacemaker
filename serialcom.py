import serial

#note DO NOT name the file serial.py, it will break the import feature
##Test codes

# --checks to see if serial port COM3 is in use--

# ser = serial.Serial()
# ser.baudrate = 19200
# ser.port = 'COM3'
# print(ser)

ser = serial.Serial('COM3') # open serial port (@ the serial port path)
print(ser.name) # check which port was really used
ser.write(b'hello') # write a string
ser.close() #close port