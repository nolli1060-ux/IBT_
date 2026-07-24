def is_palindrome(s):
    s = s.lower()

    cleaned_string = s.replace(" ", "")
    reversed_string = cleaned_string[::-1]

    if cleaned_string == reversed_string:
        return True
    else:
        return False

user_input = input("Enter a word:")

if is_palindrome(user_input):
    print("It's a palindrome")
else:
    print("it's not a palindrome")