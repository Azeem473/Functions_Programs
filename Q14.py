# Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.

def convert_temperature(value, to_scale):
    if to_scale == 'F':
        return value * 9 / 5 + 32  
    elif to_scale == 'C':
        return (value - 32) * 5 / 9  
    else:
        return "Invalid scale! Use 'C' or 'F'."

print(convert_temperature(20, 'F'))  
print(convert_temperature(70, 'C'))  

