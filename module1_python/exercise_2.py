# Exercise 2: Easier to use dosing calculator
# User story: "As an exasperated parent, I want to provide
# input in one simple phrase, so it's easy"

def determine_form(phrase):
  # determine whether user wants tablets or liquid
  # return one of those values
  if 'tablet' in phrase:
    return 'tablet'
  elif 'liquid' in phrase:
    return 'liquid'
  else:
    return 'unknown'

def determine_basis(phrase):
  # determine whether dosing is based on age or weight
  if 'pound' in phrase or 'lb' in phrase:
    return 'weight'
  else:
    return 'age'

def extract_basis_value(phrase):
  # assumption: the only numeric characters are the basis value
  # extract them!
  digits = '0123456789'  
  basis_value = ''
  for char in phrase:
    if char in digits:
      basis_value = basis_value + char # or += char for short
  return int(basis_value)

def dosing_for_tablet_given_age(age):
  age = int(float(age))
  if age < 2:
    return 'Too young'
  if age < 4:
    return '1 tablet'
  if age < 6:
    return '1.5 tablets'
  if age < 9:
    return '2 tablets'
  if age < 11:
    return '2.5 tablets'
  elif age == 11:
    return '3 tablets'
  elif age == 12:
    return '4 tablets'
  return 'Too old'

def dosing_for_liquid_given_age(age):
  # you'd have your control flow from exercise 1
  age = int(float(age))
  if age < 2:
      return '4 mL'
  if age < 4:
      return '5 mL'
  if age < 6:
      return '7.5 mL'
  if age < 9:
      return '10 mL'
  if age < 11:
      return '12.5 mL'
  elif age == 11:
      return '15 mL'
  elif age == 12:
      return '20 mL'
  return 'Too old'

def dosing_for_tablet_given_weight(weight):
  weight = int(float(weight))
  if weight < 24:
    return 'Too young'
  if weight < 36:
      return '1 tablet'
  if weight < 48:
      return '1.5 tablets'
  if weight < 60:
      return '2 tablets'
  if weight < 72:
      return '2.5 tablets'
  if weight < 96:
      return '3 tablets'
  else:
    return 'Too old'

def dosing_for_liquid_given_weight(weight):
  weight = int(float(weight))
  if weight < 12:
    return 'Too light'
  if weight < 18:
    return '2.5 mL'
  if weight < 24:
    return '4 mL'
  if weight < 36:
      return '5 mL'
  if weight < 48:
      return '7.5 mL'
  if weight < 60:
      return '10 mL'
  if weight < 72:
      return '12.5 mL'
  if weight < 96:
      return '15 mL'
  else:
    return 'Too old'

def dosing(phrase):
  phrase = phrase.lower()
  form = determine_form(phrase)
  if form == 'unknown':
    return 'Unknown form, please specify either tablets or liquid'
  basis = determine_basis(phrase)
  basis_value = extract_basis_value(phrase)

  # Begin control flow
  if form == 'tablet':
    if basis == 'age':
      return dosing_for_tablet_given_age(basis_value)
    else:
      # dosing for tablet given weight
      return dosing_for_tablet_given_weight(basis_value)
      # pass
  else:
    if basis == 'age':
      return dosing_for_liquid_given_age(basis_value)
    else:
      # dosing for liquid given weight
      return dosing_for_liquid_given_weight(basis_value)
    #   pass
    # pass


# Your code needs to pass these tests
print('Testing: tablet for 2 y/o')
assert dosing('tablet for 2 y/o') == '1 tablet'
print('Testing: liquid for 2 year old')
assert dosing('liquid for 2 year old') == '5 mL'
print('Testing: liquid for 1y old')
assert dosing('liquid for 1y old') == '4 mL'
print('Testing: tablets for 1y')
assert dosing('tablets for 1y') == 'Too young'
print('Testing: tablets for 35 lbs')
assert dosing('tablets for 35 lbs') == '1 tablet'
print('Testing: liquid for 35 pounds')
assert dosing('liquid for 35 pounds') == '5 mL'
print('Testing: liquid for 18 pounds')
assert dosing('liquid for 18 pounds') == '4 mL'
print('Testing: tablets for 18lb')
assert dosing('tablets for 18lb') == 'Too young'

print('no errors, so far...')