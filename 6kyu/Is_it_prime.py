#In this code i have to find the prime number , User gives any number to the system and code checks it is prime or not
# The biggest part of this program is its concept how may i though and how may i calculate the prime numbers
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
