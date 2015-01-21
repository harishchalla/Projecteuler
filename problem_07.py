#problem 7


#Find the 10001st prime

def main():

    val= 1

    number= 0

    y = False

    for i in range(3, 1000000, 2):

        for k in range(2, 1000, 1):

            if i%k==0:

                break

            if i < k*k:

                val+= 1

                if val==10001:

                    number= i

                    y= True

                break

        if y:

            break

    print("The 10001st prime number is:", number)

 

main()