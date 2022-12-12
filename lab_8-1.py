#Creator Cs 12/2/2022

def find_sum(n):
    total = 0

    for i in range(1, n+1):
        total += i # Add each number to the sum
    return total # Return the final sum

n = int(input("Enter an integer: "))

result = find_sum(n) # Call the function 

print(result) # Print the result to see the final sum
