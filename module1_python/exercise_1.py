# Exercise 1: More complete dosing calculator
# User story: "As an exasperated parent, I want to input
# either age or weight, because sometimes I don't know weight"
# User story: "As an exasperated parent, I want to get
# dosing for different forms and potencies"


def dosing(basis, basis_value, form):
  # dosing('age', 2, 'tablet'))
  # basis = either 'age' or 'weight'
  # basis_value = age (years) if basis is age, or weight (pounds)
  # Write your code here (and remove the "pass" placeholder)
  if basis == 'age':    
    basis_value = int(float(basis_value))
    if basis_value < 2:
      if form == 'liquid':
        return '4 mL'
      elif form == 'tablet':
        return 'Too young'
    if basis_value < 4:
      if form == 'liquid':
        return '5 mL'
      elif form == 'tablet':
        return '1 tablet'
    if basis_value < 6:
      if form == 'liquid':
        return '7.5 mL'
      elif form == 'tablet':
        return '1.5 tablets'
    if basis_value < 9:
      if form == 'liquid':
        return '10 mL'
      elif form == 'tablet':
        return '2 tablets'
    if basis_value < 11:
      if form == 'liquid':
        return '12.5 mL'
      elif form == 'tablet':
        return '2.5 tablets'
    elif basis_value == 11:
      if form == 'liquid':
        return '15 mL'
      elif form == 'tablet':
        return '3 tablets'
    elif basis_value == 12:
      if form == 'liquid':
        return '20 mL'
      return '4 tablets'
    return 'Too old'

  elif basis == 'weight':
    basis_value = int(float(basis_value))
    weight = basis_value
    if weight < 24:
      if form == 'liquid':
        return '4 mL'
      return 'Too young'
    if weight < 36:
      if form == 'liquid':
        return '5 mL'
      elif form == 'tablet':
        return '1 tablet'
    if weight < 48:
      if form == 'liquid':
        return '7.5 mL'
      elif form == 'tablet':
        return '1.5 tablets'
    if weight < 60:
      if form == 'liquid':
        return '10 mL'
      elif form == 'tablet':
        return '2 tablets'
    if weight < 72:
      if form == 'liquid':
        return '12.5 mL'
      elif form == 'tablet':
        return '2.5 tablets'
    if weight < 96:
      if form == 'liquid':
        return '15 mL'
      elif form == 'tablet':
        return '3 tablets'
    else:
      return 'Too old'
      
# print(dosing('weight', 2, 'tablet'))

# Your code needs to pass these tests
assert dosing('age', 2, 'tablet') == '1 tablet'
assert dosing('age', 2, 'liquid') == '5 mL'
assert dosing('age', 1, 'liquid') == '4 mL'
assert dosing('age', 1, 'tablet') == 'Too young'
assert dosing('weight', 35, 'tablet') == '1 tablet'
assert dosing('weight', 35, 'liquid') == '5 mL'
assert dosing('weight', 18, 'liquid') == '4 mL'
assert dosing('weight', 18, 'tablet') == 'Too young'

# Testing the function with the provided test cases
print(dosing('age', 2, 'tablet'))  # should return '1 tablet'
print(dosing('age', 2, 'liquid'))  # should return '5 mL'
print(dosing('age', 1, 'liquid'))  # should return '4 mL'
print(dosing('age', 1, 'tablet'))  # should return 'Too young'
print(dosing('weight', 35, 'tablet'))  # should return '1 tablet'
print(dosing('weight', 35, 'liquid'))  # should return '5 mL'
print(dosing('weight', 18, 'liquid'))  # should return '4 mL'
print(dosing('weight', 18, 'tablet'))  # should return 'Too young'