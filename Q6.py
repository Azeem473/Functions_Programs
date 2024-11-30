# Write a function to count the vowels in a given string.

def count_vowels(str):
    vowels = "a,e,i,o,u"
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Azeeem"))
    
