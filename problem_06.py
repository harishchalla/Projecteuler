#probmlem 6


# What is the difference between the sum of the

#squares and the square of the sums?

limit = 100

sumv = 0

sumr = 0

for i  in range(1,limit):

 sumr = sumr + i

 sumv = sumv + i*i

val1 = sumr * sumr

val2 = sumv

val = val1-val2

print val