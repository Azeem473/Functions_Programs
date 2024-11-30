# Create a function that accepts a dictionary and returns the key with the highest value.

def highest_value(data):
    return max(data, key=data.get)  
scores = {
    "Azeem": 85, "Usman": 92, "Talha": 88, "Mubashir": 95
    }
print("The key with the highest value is:", highest_value(scores))

