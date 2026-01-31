import serial
from playsound import playsound

COM_PORT = 'COM3'               # your Pico COM port
BAUD_RATE = 115200
AUDIO_FILE = r'C:\path\to\alert.mp3'

ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)

while True:
    line = ser.readline().decode().strip()
    if line:
        print("Pico:", line)
        if "ALERT" in line:
            print("Temperature above 30°C! Playing alert...")
            playsound(AUDIO_FILE)
