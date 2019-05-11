import serial
from time import sleep

try:
    ser = serial.Serial('/dev/ttyACM1', 9600)

except Exception as e:
    print("[INFO] Error: " + str(e))

while True:
    #input_cmd = input("Input 1 or 0: ")
    ser.write(str('1').encode())
