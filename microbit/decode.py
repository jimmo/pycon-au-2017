import struct
import os
import sys

f = open('data1dark', 'rb')
#f = open('/home/jimmo/data2', 'r')
#f = open('/home/jimmo/data3-darken', 'r')

b0 = 0
b1 = 0
s = ''

def reversebits(word, numbits=8):
  return sum(1<<(numbits-1-i) for i in range(numbits) if word>>i&1)

def lfsr_decode(word, data):
  word = word & 0xff
  for i in range(8):
    if word & 0x80:
      word ^= 0x11
      data ^= (1 << (7-i))
    word = (word << 1) & 0xff
  return (word, data)

#address = 0b 01110101 01100010 01101001 01110100
#group = 0

packet = ''

#while True:
  #chunk = os.read(f.fileno(), 200)
chunk = f.read()
for xi in range(0, len(chunk), 2):
  x, = struct.unpack('h', chunk[xi:xi+2])
  if x < 500:
    if b1:
      n = round(b1/8)
      s += '1'*n
      b1 = 0
    b0 += 1
    if b0 > 1000 and s:
      s = s[s.find('01010101'):]

      lfsr = 0x18 | 2
      for i in range(0, len(s)-7, 8):
        bb = s[i:i+8]
        if i < 6*8:
          packet += bb + ', '
        else:
          b = int(bb, 2)
          lfsr, b = lfsr_decode(lfsr, b)
          packet += '{:08b}'.format(b) + ', '
      print(packet)
      packet = ''
      s = ''
  else:
    if b0:
      n = round(b0/8)
      if n > 1000:
        n = 1
      s += '0'*n
      b0 = 0
    b1 += 1
