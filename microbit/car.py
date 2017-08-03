from microbit import *
import radio
import neopixel

n = neopixel.NeoPixel(pin13, 12)
n.clear()
n.show()

radio.config(channel=65, data_rate=radio.RATE_250KBIT, power=7)
radio.on()

def beep(d1, d2=0):
  pin14.write_digital(True)
  sleep(d1)
  pin14.write_digital(False)
  sleep(d2)

def lock_car():
  n.clear()
  n[0] = (100, 0, 0,)
  n[6] = (100, 0, 0,)
  n.show()
  beep(100, 100)
  beep(30, 100)
  beep(30, 0)

def unlock_car():
  n.clear()
  n[0] = (0, 100, 0,)
  n[6] = (0, 100, 0,)
  n.show()
  beep(30, 100)
  beep(30, 100)
  beep(100, 0)


lock_car()

while True:
  try:
    msg = radio.receive()
    if msg == 'unlock':
      unlock_car()
    elif msg == 'lock':
      lock_car()
  except:
    radio.off()
    radio.on()
