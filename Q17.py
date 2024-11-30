# Write a function that takes a list and removes all duplicate elements.

def remove_duplicates(input_list):
    return list(set(input_list))

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(unique_list)  

