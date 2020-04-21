# Write a program to determine if a number, given on the command line, is prime.

# user input
num = int(input('Enter a number: '))

# prime number rules
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, 'is not a prime number.')
            break
        else:
            print(num, 'is a prime number.')
else:
    print(num, 'is not a prime number.')

# How can you optimize this program?
# Implement The Sieve of Eratosthenes, one of the oldest algorithms known (ca. 200 BC).