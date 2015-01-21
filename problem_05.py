#Problem5:

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 in Python

def gcd(x, y): # Greatest Common Divisor

    while y != 0:

        (x, y) = (y, x % y)

    return x

def lcm(a,b): #and Least Common Multiple

    return a * b / gcd(a,b)


v = 1

for i in range(1, 20):#the smallest number that can be divided by each of the numbers from 1 to 20 without any remainder

     n = lcm(v,i)



print n