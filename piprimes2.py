from sympy import *

# create the continued fraction convergents

with open('b001203.txt','r') as fp:
  p2,q2 = 0, 1
  p1,q1 = 1, 0
  for line in fp:
    sn,sa = line.strip().split(' ')
    n = int(sn)
    a = int(sa)
    #
    # Extend continued fraction for one more term
    #
    p,q = a*p1+p2, a*q1+q2
    p2,q2 = p1,q1
    p1,q1 = p,q
    #
    # Check if P is even (LSB == ) and if P/2 is prime
    if(((p & 1) == 0) and isprime(p//2)):
      print("Prime ", n, p//2 )
