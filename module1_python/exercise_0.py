# Let's make it so we can get dosing for many kids
# And let's also add tests to make it safer
# To do both of the above, we'll rewrite as a function


def dosing(age):
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


# Assert that the actual output matches the expected output
# For the given input
assert dosing(0) == 'Too young'
assert dosing(1) == 'Too young'
assert dosing(2) == '1 tablet'
assert dosing(3) == '1 tablet'
assert dosing(4) == '1.5 tablets'
assert dosing(5) == '1.5 tablets'
assert dosing(6) == '2 tablets'
assert dosing(7) == '2 tablets'
assert dosing(8) == '2 tablets'
assert dosing(9) == '2.5 tablets'
assert dosing(10) == '2.5 tablets'
assert dosing(11) == '3 tablets'
assert dosing(11.9999) == '3 tablets'
assert dosing(12) == '4 tablets'
assert dosing(13) == 'Too old'

# This provides a command line experience
# Ready to answer many dosing questions without a restart

more_kids = True

# while more_kids:
#   age = input('Age? ')
#   print(dosing(age), end='\n\n')
#   keep_going = input('Another kid? [Y/n] ')
#   more_kids = keep_going != 'n'

## to handle blank input
while more_kids:
  age = input('Age? ').strip()
  if not age:
    print("Age input cannot be blank. Please try again.")
    continue
  print(dosing(age), end='\n\n')
  keep_going = input('Another kid? [Y/n] ').strip().lower()
  more_kids = keep_going != 'n'

# TODO: Handle blank input -> done
# TODO: Handle decimal input (3.6) -> already handles decimals
