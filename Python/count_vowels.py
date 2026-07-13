def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
word = input("Enter a word: ")
vowel_count = count_vowels(word)
print(f"The word '{word}' contains {vowel_count} vowels.")
