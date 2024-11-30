# Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b  
    return (a)  
num1 = 56
num2 = 98
print(f"The GCD of {num1} and {num2} is:", gcd(num1, num2))

