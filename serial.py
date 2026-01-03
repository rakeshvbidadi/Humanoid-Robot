import serial

ser = serial.Serial('COM6', 9600)  # Open serial connection to COM6 at 9600 baud rate

command = '1'  # Set command to '1' to turn on LED
ser.write(command.encode())  # Send command as bytes
