#Problem3:

# Find the largest prime factor of a composite number

value =600851475143

p = 2

while p * p < value:

     while value % p == 0:

         value = value / p

     print value

     p = p + 1

 

print"The largest prime factor of the number 600851475143"

print value