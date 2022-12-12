#Creator CS 12/12/2022

def factorial(num):
    # set the product to 1
    product = 1

    # Use a for loop 
    for i in range(1, num+1):
        # Multiply each number by the product
        product *= i

    # Return the final product
    return product

# Test cases
print(factorial(1))  
print(factorial(3))  
print(factorial(5))  
print(factorial(0))  
