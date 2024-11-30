# Write a function to flatten a nested list.

def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))  
        else:
            flattened.append(item)
    return flattened

nested = [1, [2, [3, 4]], [5, 6], 7]
flat = flatten_list(nested)
print(flat)  



