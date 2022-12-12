#Creator CS 12/12/2022

def count_a(word):
    count = 0
   
    # Use a for loop
    for char in word:
        # Check if the letter is an 'a' or an 'A'
        if char == 'a' or char == 'A':
            count += 1

    # Return the final count
    return count

