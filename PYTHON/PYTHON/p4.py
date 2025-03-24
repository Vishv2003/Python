# Reverse a String Without Using Built-in Functions
#Reverses a given string without using Python's built-in [::-1] slicing or .reverse() methods.
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str 
    return reversed_str
print(reverse_string("VISHV NAVADIYA"))  
