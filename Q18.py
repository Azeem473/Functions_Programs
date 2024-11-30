#  Create a function that takes a string and counts the frequency of each character.

def count_char_frequency(input_string):
    char_frequency = {}

    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

text = "hello world"
result = count_char_frequency(text)
print(result)
