#Creator CS 12/12/2022

def is_palindrome(word):
    # Reverse the word
    reversed_word = word[::-1]

    # Check if the reversed word is the same as the original word using if statements
    if reversed_word == word:
        # If it is return True
        return True
    else:
        #  return False
        return False

# Test the function 
print(is_palindrome("racecar"))  #True
print(is_palindrome("hello"))  #False
print(is_palindrome("a"))  #True
print(is_palindrome(""))  #True
