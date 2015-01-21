# this is the sum of all the multiples of 3 0r 5 below 1000
import time

print "The sum of all the multiples of 3 or 5 below 10!\n"

total = 0

for value in range(1,10):

    if value % 3 == 0 or value % 5 == 0:

         #total = total + value

          total += value

    print total

    time.sleep(0.75)

print "The sum of all the multiples of 3 or 5 below 1000!\n"

total = 0

for value in range(1,1000):

    if value % 3 == 0 or value % 5 == 0:

         #total = total + value

          total += value

    print total