TOKEN = '5890804373:AAE89iCPBcVuGluKly3RGdtqY521E0A9VDI'

def to_3(n):
  n3 = ''
  d = {0: 'A', 1: 'B', 2: 'O'}
  while n != 0:
    n3 = ''.join((n3, d[n % 3]))
    n //= 3
  return n3[::-1].zfill(6).replace('0', 'A')


def from_3(n3):
  d = {'A': 0, 'B': 1, 'O': 2}
  len_ = len(n3)
  n3 = n3[::-1]
  n = list((d[n3[i]]*3**i for i in range(len(n3))))
  return sum(n)


def vigen(msg, key):
  al = 256
  ln = len(msg)
  lnk = len(key)
  encrypt = [(msg[i] + key[i % lnk]) % al for i in range(ln)]
  return encrypt


def vigendec(enc, key):
  al = 256
  ln = len(enc)
  lnk = len(key)
  msg = [(enc[i] - key[i % lnk]) % al for i in range(ln)]
  return msg
