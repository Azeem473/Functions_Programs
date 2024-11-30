# Write a function to check whether a string is a palindrome.

def palindrome_string(str):
    is_string = str.replace(" ", "").lower()
    return is_string == is_string[::-1]
text = "Was it a car or a cat I saw"
print(f"Is the string a palindrome? {palindrome_string(text)}")
