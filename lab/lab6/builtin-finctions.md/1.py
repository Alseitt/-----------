# BUILTIN FUNCTIONS

# # 1. Write a Python program with builtin function to multiply all the numbers in a list

# from functools import reduce  #reduce function is used to apply a function to all elements in a list iteratively and return a single result.
# numbers = [2, 3, 4, 5]

# result = reduce(lambda x, y: x * y, numbers) #lambda is an anonymous function that takes two arguments
# print(result)


# # 2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

# string = input("Enter a string: ")

# num_upper = sum(1 for char in string if char.isupper())

# num_lower = sum(1 for char in string if char.islower())

# print("Number of uppercase letters:", num_upper)
# print("Number of lowercase letters:", num_lower)


# 3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.

# def is_palindrome(string):
#     string = ''.join(char.lower() for char in string if char.isalnum())  #char.isalnum checks if string is alphanumeric(contains letters and numbers)
#     return string == string[::-1] #reverse string

# string = input("Enter a string: ")

# if is_palindrome(string):
#     print(string, "is a palindrome")
# else:
#     print(string, "is not a palindrome")


# 4. Write a Python program that invoke square root function after specific milliseconds.
# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858


# import math 
# import time

# num = int(input('Enter a number:'))
# ms = int(input('Enter the number of milliseconds to wait:'))

# time.sleep(ms / 1000)  #sleep stops the function for some milliseconds to execute (divides by 1000 to convert sec to millisec)

# sqrt_num = math.sqrt(num)

# print(f"Square root of {num} after {ms} milliseconds is {sqrt_num}")


# 5. Write a Python program with builtin function that returns True if all elements of the tuple are true.

# my_tuple1 = (True, True, True, True)
# my_tuple2 = (False, False, True, True)

# all_tuple1 = all(my_tuple1)
# all_tuple2 = all(my_tuple2)

# print(all_tuple1)
# print(all_tuple2)  
