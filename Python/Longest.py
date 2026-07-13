def long_string(s):
    longest = ""
    current = ""
    for char in s:
        if char.isalpha():
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = ""
    if len(current) > len(longest):
        longest = current
    return longest
word = input("Enter a string: ")
longest_word = long_string(word)
print(f"The longest word in the string is: '{longest_word}'")