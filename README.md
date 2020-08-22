# PiPrimes
Find primes in the Continued Fraction approximation to Pi

Motivated by Matt Parker's Stand-up Maths video "What is the biggest tangent of a prime?" https://www.youtube.com/watch?v=A7eJb8n8zAw&t=1s.  In that video, looking for integers such that tan(N) > N boils down to finding N which are close to (K+1/2)*Pi.  This equivalent to finding rational approximations to Pi of the form (2*N)/(2*K+1).  Instead of brute forcing this, it occurred to me that the continued Fraction approximation technique already produces the sequence of progressively closer rational approximations to a value.  No searching needed.

https://en.wikipedia.org/wiki/Approximations_of_%CF%80#Continued_fractions
https://en.wikipedia.org/wiki/Continued_fraction#Generalized_continued_fraction

Unfortunately, the formula PI = [3; 7,15,1,292,1,1,1,2,...] has no obvious formula.  But convieniently, the first 1000 Convergents (fractional approximations) are available in https://oeis.org/A002485 (numerator) and https://oeis.org/A002486 (demoninator).

Download the numerator sequence https://oeis.org/A002486/b002486.txt read them into some python code, and check for numerators of the form 2*N.  Then check N to see if it isprime().

Interestingly, line 86 looks like this:
86 2339618734654425141409627264213705772778073822

But that is EXACTLY 2x the prime mentioned in the video: 1,169,809,367,327,212,570,704,813,632,106,852,886,389,036,911

See piprime1.py for details.

It uses the Python package sympy to get the isprime() function: https://www.geeksforgeeks.org/python-sympy-isprime-method/.  It uses the Miller-Rabin test https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test.

Stand alone implimentations are available here:
https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Proved_correct_up_to_large_N

## Unfortunately, the first 1000 terms don't have another prime.

To go further, you have to generate more convergents.  Conveniently, the Continued Fraction terms are available here https://oeis.org/A001203.  Downloading the first 20000 values from https://oeis.org/A001203/b001203.txt

Running piprime2.py checks the values and finds one big one.

But this process gets a bit slow for terms beyond about 10000.  Running this out to 20000 doesn't find anything.  180 Million terms in the sequence are availble here: http://chesswanks.com/seq/cfpi/.  But it would take a long time to check those all.

Happy Hunting!

