# Create a function to check if a given number is prime.

def prime_numbers(num):
    if num <=1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
        return True
print(prime_numbers(7))
