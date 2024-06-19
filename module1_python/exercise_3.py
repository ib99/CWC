# Exercise 3
# Copy and paste from Slack when ready

# Exercise 3: Working with different variable types for proficiency
# in type-specific operators and methods

# INSTRUCTIONS ---------------------------------------------------------
# PART 1. First read and try out all the basic operations
# PART 2. Then implement the two functions defined below to pass asserts
# ----------------------------------------------------------------------

# =================
# PART 1
# =================

# STRING EXERCISES
# 1. Create a string variable with the value "Patient status: Stable" and print it
patient_status = "Patient status: Stable"
print(patient_status)

# 2. Use slicing to print only "Stable" from the string
print(patient_status[15:])

# 3. Convert the whole string to uppercase and print the result
print(patient_status.upper())

# 4. Find the index of the colon in the string and print it
print(patient_status.index(':'))

# 5. Replace "Stable" with "Critical" and print the new string
print(patient_status.replace("Stable", "Critical"))

# INTEGER EXERCISES
# 1. Create an integer variable with the value 120 representing heart rate and print it
heart_rate = 120
print(heart_rate)

# 2. Subtract 20 from the heart rate and print the result
print(heart_rate - 20)

# 3. Multiply the heart rate by 2 to simulate stress test conditions and print the result
print(heart_rate * 2)

# 4. Divide the heart rate by 4 using both normal and floor division, print the results
print(heart_rate / 4)
print(heart_rate // 4)

# 5. Calculate the power of 2 of the heart rate and print the result
print(heart_rate**2)

# # FLOAT EXERCISES
# 1. Create a float variable with the value 36.6 representing body temperature in Celsius and print it
body_temperature = 36.6
print(body_temperature)

# 2. Round the body temperature to one decimal place and print it
print(round(body_temperature, 1))

# 3. Add 0.5 to the body temperature to simulate a fever and print the result
print(body_temperature + 0.5)

# 4. Multiply the body temperature by 1.8 and add 32 to convert to Fahrenheit and print the result
print(body_temperature * 1.8 + 32)

# 5. Find the floor value of the body temperature and print it
import math

print(math.floor(body_temperature))

# LIST EXERCISES
# 1. Create a list of systolic blood pressure readings [120, 110, 115, 108, 112] and print the list
blood_pressure_readings = [120, 110, 115, 108, 112]
print(blood_pressure_readings)

# 2. Append the reading 119 to the list and print the updated list
blood_pressure_readings.append(119)
print(blood_pressure_readings)

# 3. Slice the list to get the last three readings and print them
print(blood_pressure_readings[-3:])

# 4. Pop the last item of the list and print the popped item and the updated list
popped_reading = blood_pressure_readings.pop()
print(popped_reading)
print(blood_pressure_readings)

# 5. Sort the list in ascending order and print it
blood_pressure_readings.sort()
print(blood_pressure_readings)

# DICTIONARY EXERCISES
# 1. Create a dictionary {'name': 'John Doe', 'age': 30, 'allergies': ['Peanuts', 'Penicillin']} and print it
patient_record = {
    'name': 'John Doe',
    'age': 30,
    'allergies': ['Peanuts', 'Penicillin']
}
print(patient_record)

# 2. Add a new key 'blood_type' with the value 'O+' and print the dictionary
patient_record['blood_type'] = 'O+'
print(patient_record)

# 3. Print the value of the 'name' key from the dictionary
print(patient_record['name'])

# 4. Change the 'age' to 31 and print the updated dictionary
patient_record['age'] = 31
print(patient_record)

# 5. Remove the 'allergies' key from the dictionary and print the updated dictionary
del patient_record['allergies']
print(patient_record)

# BOOLEAN EXERCISES
# 1. Create a boolean variable set to True representing a patient's test result as positive and print it
test_result_positive = True
print(test_result_positive)

# 2. Use the not operator to invert the test result and print the result
print(not test_result_positive)

# 3. Compare two boolean variables (True for test positive and False for test negative) using the == operator and print the result
print(True == False)

# 4. Use the and operator to evaluate a test being positive and symptoms being severe (True and False) and print the result
print(True and False)

# 5. Use the or operator to evaluate a test being positive or symptoms being mild (True and False) and print the result
print(True or False)

# # =================
# # Part 2
# # =================

def create_patient_object(dob, sex_at_birth, allergies, dx_and_tx):
  # TODO: Implement this function body to pass assert set 1 below
  patient = {
    'dob': dob,
    'sex_at_birth': sex_at_birth,
    'allergies': allergies,
    'dx_and_tx': dx_and_tx,
  }
  return patient

def add_medications_for_conditions(patient):
  # TODO: Implement this function body to pass assert set 2 below
  patient['dx_and_tx']['eczema'].append('hydrocortisone')
  patient['dx_and_tx']['asthma'].append('albuterol')
  return patient

# --------------------------------------
# DO NOT CHANGE THE CODE BELOW THIS LINE
# --------------------------------------

# Assert set 1
dx_tx = {'asthma': [], 'eczema': []}
patient = create_patient_object('2016-05-04', 'F', None, dx_tx)

assert patient['dob'] == '2016-05-04'
assert patient['sex_at_birth'] == 'F'
assert set(patient['dx_and_tx'].keys()) == set(['asthma', 'eczema'])
assert patient['allergies'] is None

print('All assertions passed for set 1')

# Assert set 2
add_medications_for_conditions(patient)

assert patient['dx_and_tx']['eczema'][0] == 'hydrocortisone'
assert patient['dx_and_tx']['asthma'][0] == 'albuterol'

print('All assertions passed for set 2')
