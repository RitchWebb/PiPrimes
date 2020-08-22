# PiPrimes
Find primes in the Continued Fraction approximation to Pi

Motivated by Matt Parker's Stand-up Maths video "What is the biggest tangent of a prime?" https://www.youtube.com/watch?v=A7eJb8n8zAw&t=1s.  In that video, looking for integers such that tan(N) > N boils down to finding N which are close to (K+1/2)*Pi.  This equivalent to finding rational approximations to Pi of the form (2*N)/(2*K+1).  Instead of brute forcing this, it occurred to me that the Continued Fraction approximation technique already produces the sequence of progressively closer rational approximations to a value.  No searching needed.

https://en.wikipedia.org/wiki/Approximations_of_%CF%80#Continued_fractions
https://en.wikipedia.org/wiki/Continued_fraction#Generalized_continued_fraction

Unfortunately, the formula PI = [3; 7,15,1,292,1,1,1,2,...] has no obvious formula.  But convieniently, the first 1000 Convergents (fractional approximations) are available in https://oeis.org/A002485 (numerator) and https://oeis.org/A002486 (demoninator).

Download the numerator sequence https://oeis.org/A002486/b002486.txt read them into some python code, and check for numerators of the form 2*N.  Then check N to see if it isprime().

Interestingly, line 86 looks like this:
86 2339618734654425141409627264213705772778073822

And that is EXACTLY 2x the prime mentioned in the video: 1,169,809,367,327,212,570,704,813,632,106,852,886,389,036,911

See piprime1.py for details.

It uses the Python package sympy to get the isprime() function: https://www.geeksforgeeks.org/python-sympy-isprime-method/.  https://docs.sympy.org/latest/modules/ntheory.html?highlight=isprime#sympy.ntheory.primetest.isprime 
It uses the Miller-Rabin test https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test.
And https://en.wikipedia.org/wiki/Baillie%E2%80%93PSW_primality_test


Standalone implimentations for different languages are available here:
https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Proved_correct_up_to_large_N

## Unfortunately, the first 1000 terms don't have another prime.

To go further, you have to generate more convergents.  Conveniently, the Continued Fraction terms are available here https://oeis.org/A001203.  Downloading the first 20000 values from https://oeis.org/A001203/b001203.txt

Running piprime2.py checks the values and finds one big one:

230835870782558831561617186504559084198719501221763995608082253627620752053749345488376393822837250198036536001853828659466202612019525543362322174085744303421231446484541625047630462908919109308644634605051209877750956648014568322183373423523622941806761765245932401727973436579786298208782013178059220103271409347616696556052706562092799953175234183483071403726145726928572372071037042523626350312132351311366806233135093893271182587352730075523143635168510803804031460442796778933680674070124730971307185688425634077096234482442639666385695677866015904370207368846631450100939158029908242779848800640038255592227473300237596577845602369215568916732445980431078426390412264603773550384039765410088966381694110344811198325354315338629604946794192217817288101344643511450133142277670683067655250506551517767422160650566385017503208608678491109517443585115317845289832567015746473548492179557935154400719019569904865219030736244089287736334048402066257337090606092966121806567484954460809024219605952851728610326005069




But this process gets a bit slow for terms beyond about 10000.  Running this out to 20000 takes hours and doesn't find anything.

## Next Steps

180 Million terms in the sequence are availble here: http://chesswanks.com/seq/cfpi/.  But it would take a long time to check those all.  Cmputing the Convergents is pretty fast, so you could run a bunch of searches in parallel, say by having K different computers generate convergents up to some starting point (say 20000*i for i in (1..K)) and only then check for primes for the next 20000 convergents.


Happy Hunting!

