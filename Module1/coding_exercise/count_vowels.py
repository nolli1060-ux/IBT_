def count_vowels(s):

    s = s.lower()
    vowels = "aeiou"
    count = 0
    
    for char in s:
        if char in vowels:
            count += 1
    return count

user_word = input("Enter a word or sentence: ")
result = count_vowels(user_word)
print("Number of vowels:", result)