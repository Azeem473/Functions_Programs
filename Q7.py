# Create a function that takes a list of numbers and returns the largest number.

def find_largest_number(numbers):
    if not numbers:  
        return None  
    return max(numbers)  
my_list = [10, 25, 47, 3, 99, 67]
print("The largest number is:", find_largest_number(my_list))
