from sympy import *

# pre-computed continued fraction convergents
with open('b002485.txt','r') as fp:
  for line in fp:
    a,b = line.strip().split(' ')
    ib = int(b)
    if(((ib & 1) == 0) and isprime(int(b)//2)):
      print("Prime ", a, b, int(b)//2 )

