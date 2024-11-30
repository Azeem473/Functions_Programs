# Create a function to check if two strings are anagrams.

def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

print(anagrams("listen", "silent"))  
print(anagrams("hello", "world"))    



