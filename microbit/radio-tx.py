import radio
from microbit import *
radio.on()
radio.config(channel=65, data_rate=radio.RATE_250KBIT, power=7)
i = 0
while True:
  if button_a.was_pressed():
    display.show(Image.HEART)
    radio.send('UUUUpy' + chr(i%10))
    display.clear()
    i += 1
