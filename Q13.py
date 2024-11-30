# Write a function that calculates the power of a number without using the ** operator

def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result  
    return result

base = 2
exponent = 3
print(f"{base} raised to the power of {exponent} is:", power(base, exponent))

base = 2
exponent = -3
print(f"{base} raised to the power of {exponent} is:", power(base, exponent))
