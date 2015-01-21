#Problem 4:

#Find the largest palindrome made from the product of two 3-digit

#numbers.

def reverse(st):

    rev = ""

    for i in range(0 ,len(st)):

        rev += st[(len(st) -1) - i]

    return rev

def is_palindrome(i):

    return str(i) == reverse(str(i))



max=0



for i in range(100,999):

    for j in range(i+1,1000):

        p = i * j

        if is_palindrome(p) and p > max :

            max = p



print max