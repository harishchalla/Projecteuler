import math
def isprime(total):
    prime = 1
    if total % 2 == 0:
        prime = 0
        return prime
    x = 3
    while x <= math.sqrt(total):
        if total % x == 0:
            prime = 0
            break
        x+=2
    return prime
var = 2
i = 3
while i < 2000000:
    if isprime(i) == 1:
        var+=i
    i+=1
print "Summation of Primes below 2 millions:",var
