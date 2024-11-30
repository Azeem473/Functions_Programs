# Write a function to find the nth Fibonacci number

def fibonacci_number(num):
    if num == 1:
        return 0  
    elif num == 2:
        return 1  
    else:
        a, b = 0, 1
        for _ in range(2, num):  
            a, b = b, a + b
        return b
n = 5
print(f"The {n}th Fibonacci number is:", fibonacci_number(n))