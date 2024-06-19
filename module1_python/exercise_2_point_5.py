# Exercise 2.5 
# More practice with types and type methods
# Exercise file for basic Python variable types

# STRING EXERCISES
# 1. Create a string variable with the value "Hello, world!" and print it
hello_world = "Hello, healthcare!"
print(hello_world)

# 2. Use slicing to print only "world" from the string
print(hello_world[7:12])

# 3. Convert the whole string to uppercase and print the result
print(hello_world.upper())

# 4. Find the index of the comma in the string and print it
print(hello_world.index(','))

# 5. Replace "Hello" with "Goodbye" and print the new string
print(hello_world.replace("Hello", "Goodbye"))

# INTEGER EXERCISES
# 1. Create an integer variable with the value 10 and print it
integer_variable = 10
print(integer_variable)

# 2. Add 5 to the integer and print the result
print(integer_variable + 5)

# 3. Multiply the integer by 3 and print the result
print(integer_variable * 3)

# 4. Divide the integer by 2 using both normal and floor division, print the results
print(integer_variable / 2)
print(integer_variable // 2)

# 5. Calculate the power of 2 of the integer and print the result
print(integer_variable ** 2)

# FLOAT EXERCISES
# 1. Create a float variable with the value 3.14159 and print it
float_variable = 3.14159
print(float_variable)

# 2. Round the float to two decimal places and print it
print(round(float_variable, 2))

# 3. Add 2.5 to the float and print the result
print(float_variable + 2.5)

# 4. Multiply the float by 2 and print the result
print(float_variable * 2)

# 5. Find the floor value of the float and print it
import math
print(math.floor(float_variable))

# LIST EXERCISES
# 1. Create a list of numbers [1, 2, 3, 4, 5] and print the list
numbers_list = [1, 2, 3, 4, 5]
print(numbers_list)

# 2. Append the number 6 to the list and print the updated list
numbers_list.append(6)
print(numbers_list)

# 3. Slice the list to get the last three items and print them
print(numbers_list[-3:])

# 4. Pop the last item of the list and print the popped item and the updated list
popped_item = numbers_list.pop()
print(popped_item)
print(numbers_list)

# 5. Sort the list in descending order and print it
numbers_list.sort(reverse=True)
print(numbers_list)

# DICTIONARY EXERCISES
# 1. Create a dictionary {'name': 'Claudia', 'age': 25} and print it
person_dictionary = {'name': 'Federico', 'age': 55}
print(person_dictionary)

# 2. Add a new key 'occupation' with the value 'Nurse' and print the dictionary
person_dictionary['occupation'] = 'Engineer'
print(person_dictionary)

# 3. Print the value of the 'name' key from the dictionary
print(person_dictionary['name'])

# 4. Change the 'age' to 26 and print the updated dictionary
person_dictionary['age'] = 26
print(person_dictionary)

# 5. Remove the 'occupation' key from the dictionary and print the updated dictionary
del person_dictionary['occupation']
print(person_dictionary)

# BOOLEAN EXERCISES
# 1. Create a boolean variable set to True and print it
boolean_variable = True
print(boolean_variable)

# 2. Use the not operator to invert the boolean value and print the result
print(not boolean_variable)

# 3. Compare two boolean variables (True and False) using the == operator and print the result
print(True == False)

# 4. Use the and operator to evaluate True and False and print the result
print(True and False)

# 5. Use the or operator to evaluate True and False and print the result
print(True or False)
