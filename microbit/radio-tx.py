import radio
from microbit import *
radio.on()
radio.config(channel=65, data_rate=radio.RATE_250KBIT, power=7)
i = 0
while True:
  if button_a.was_pressed():
    display.show(Image.HEART)
    #radio.send_bytes(bytes([0xff]*(i%10)) + bytes([0xff,0x00,0xaa,0x55,i%256]))
    radio.send_bytes(bytes([1,2,3,4]))
    display.clear()
    i += 1
