import struct
import os
import sys

f = open('/tmp/fifo', 'rb')

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

data = 0
n = 0
nn = 0
en = 0
packet = []

while True:
  bit = os.read(f.fileno(), 1)
  if not bit:
    break
  bit = bit[0]
  if bit & 2 and not en:
    en = 1
    data = 0
    n = 0
    packet = []
  if not en:
    continue

  data <<= 1
  data |= (bit & 1)
  n += 1
  if n == 8:
    packet.append(data)
    data = 0
    n = 0
    if len(packet) == 20:
      lfsr = 0x18 | 2
      for i in range(5, len(packet)):
        lfsr, packet[i] = lfsr_decode(lfsr, packet[i])
      for i in range(len(packet)):
        packet[i] = reversebits(packet[i])
      #print(' '.join('{:08b}'.format(x) for x in packet))
      print('Address: 0x{:08x}, Base: 0x{:02x}, Length: 0x{:02x}'.format(packet[0] | (packet[1] << 8) | (packet[2] << 16) | (packet[3] << 24), packet[4], packet[5]))
      print('  ' + ' '.join('{:02x}'.format(x) for x in packet[6:6+packet[5]+2]))
      en = 0
