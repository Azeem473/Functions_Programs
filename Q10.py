# Create a function that takes a list of integers and returns the sum of all even numbers.

def even_number(num):
     return sum(num for num in num if num % 2 == 0)
list = [10,3,6,9,8]
print("The sum of even numbers is:", even_number(list))

