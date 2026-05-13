#In this code i have to find the prime number , User gives any number to the system and code checks it is prime or not 
def prime(num):
    if num <=1:
        print("Not a prime number")
        return
    for i in range(2,num):
        if num % i == 0:
            print("Not a prime number")
            return
    print("Prime number")
prime(int(input("Enter a number: ")))
