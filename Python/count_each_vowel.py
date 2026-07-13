def count_each_vowel(string):
    vowels = "aeiouAEIOU"
    count = {vowel: 0 for vowel in vowels}
    
    for char in string:
        if char in vowels:
            count[char] += 1
            
    return count
word = input("Enter a word: ")
vowel_counts = count_each_vowel(word)
print(f"The word '{word}' contains the following vowel counts:")
for vowel, count in vowel_counts.items():
    print(f"  {vowel}: {count}")