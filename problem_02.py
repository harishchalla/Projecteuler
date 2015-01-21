problem2:

# Find the sum of all the even-valued terms in the Fibonacci sequence

#which do not exceed four million.



limit=4000000

sum=0

a=1

b=1

while b<limit:

 if b % 2==0:

    sum = sum + b

 h=a+b

 a=b

 b=h

print sum