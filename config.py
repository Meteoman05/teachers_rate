TOKEN = '5mq}8p^u9kka0e~C8|9#0ca74T;j3)FC7WC(3G5^:D;+A(CgAHn*E0bN8D#f9wZ9ii1fCEe=P6@DBXTfc1uXV8+ouiclG%Spl!V0u=GNKY%mlVH>y{]=3_2FR:M:G DZdx8-t\GRqAJXYYt45$.q2n0}1y}>E -j06^UA;`E9n[}VLa^DC UI1;2'

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
