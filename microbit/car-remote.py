from microbit import *
import radio

radio.config(channel=65, data_rate=radio.RATE_250KBIT, power=7)
radio.on()

while True:
  if button_a.was_pressed():
    radio.send('lock')
    display.show(Image.NO)
    sleep(400)
    display.clear()
  if button_b.was_pressed():
    radio.send('unlock')
    display.show(Image.YES)
    sleep(400)
    display.clear()
