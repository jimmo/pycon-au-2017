def whiten(data, lfsr, poly):
  result = []
  for b in data:
    for i in range(8):
      if lfsr & 0x80:
        lfsr ^= poly
        b ^= (1 << (7-i))
      lfsr <<= 1
    result.append(b)
  return result


rx = [0b00111001, 0b10010000, 0b01100100, 0b00010011, 0b11111100, 0b00010011]
tx = [0b00100000, 0b10000000, 0b01000000, 0b11000000, 0b00100000, 0b00101100]


for i in range(256):
  for j in range(256):
    guess = whiten(rx, i, j)
    if guess == tx:
      print('0x{:02x} (0b{:08b}) 0x{:02x} (0b{:08b})'.format(i, i, j, j))
