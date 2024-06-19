# Exercise 4
# Build a tool for checking drug-drug and drug-allergy interactions

# The most common type of decision you will make programming is
# how to organize data and logic.
# What logic should be grouped together?
# What data should be grouped together?
# What data and logic should be grouped together?
# What should be kept separate?

# There are many tradeoffs to consider
# Clarity and maintainability: what is easiest to understand?
#  (both for others and for your future self)
# Performance: what is faster? Fewer operations, less resource use

# Our exercise is to build a drug-drug and drug-allergy interaction
# checking tool

# What data is involed?
# 1. drugs
# 2. allergies
# 3. patients (who may have allergies and may take medications)

# What logic is involved?
# 1. Given two drugs, identify their interactions
# 2. Given a drug and an allergy, identify their interactions
# 3. For a given patient, reconcile drugs to identify potential
# deprescribing

# Now let's create new types (new "classes") that organize the data
# we need and the logic

## my notes:
## method as a function attached to a class
## class is another word for type: int, str, list, dict, etc

# ------------------------------------------------------------------------
# INTRO TO CLASSES: https://chatgpt.com/share/5a459bde-1577-41b4-b4a7-af5e3dc73f4e
# -------------------------------------------------------------------------


class Medication:
  DRUG_CLASS = ''
  DRUG_NAME = ''
  INTERACTING_DRUG_CLASSES = []
  INTERACTING_DRUG_NAMES = []

  @classmethod
  def interacts_with(cls, other_medication):
    if other_medication.DRUG_CLASS in cls.INTERACTING_DRUG_CLASSES:
      return True
    if other_medication.DRUG_NAME in cls.INTERACTING_DRUG_NAMES:
      return True
    return False


# Now let's define specific medications. In the real world, drug databases
# are extremely complex and include many different relationships
# covering brand and generic associations, crosswalk tables to
# map different terminology sets like NDC and RxNorm and SNOMED-CT
# and many drug database vendors (it's all proprietary) also offer
# dosing information, validation ranges, and clinical decision support


class Warfarin(Medication):
  DRUG_CLASS = 'Anticoagulant'
  DRUG_NAME = 'Warfarin'
  INTERACTING_DRUG_CLASSES = ['NSAID', 'Antibiotic', 'Antifungal']
  INTERACTING_DRUG_NAMES = ['Aspirin']


class Aspirin(Medication):
  DRUG_CLASS = 'NSAID'
  DRUG_NAME = 'Aspirin'
  INTERACTING_DRUG_CLASSES = ['Anticoagulant', 'Corticosteroid']
  INTERACTING_DRUG_NAMES = ['Warfarin']


class Ibuprofen(Medication):
  DRUG_CLASS = 'NSAID'
  DRUG_NAME = 'Ibuprofen'
  INTERACTING_DRUG_CLASSES = ['Anticoagulant', 'Corticosteroid']
  INTERACTING_DRUG_NAMES = ['Warfarin']


class Lisinopril(Medication):
  DRUG_CLASS = 'ACE Inhibitor'
  DRUG_NAME = 'Lisinopril'
  INTERACTING_DRUG_CLASSES = ['Potassium-sparing Diuretics']
  INTERACTING_DRUG_NAMES = ['Spironolactone']


class Spironolactone(Medication):
  DRUG_CLASS = 'Potassium-sparing Diuretic'
  DRUG_NAME = 'Spironolactone'
  INTERACTING_DRUG_CLASSES = ['ACE Inhibitor']
  INTERACTING_DRUG_NAMES = ['Lisinopril']


class Simvastatin(Medication):
  DRUG_CLASS = 'Statin'
  DRUG_NAME = 'Simvastatin'
  INTERACTING_DRUG_CLASSES = [
      'Macrolide Antibiotic', 'Calcium Channel Blocker'
  ]
  INTERACTING_DRUG_NAMES = ['Clarithromycin']


class Clarithromycin(Medication):
  DRUG_CLASS = 'Macrolide Antibiotic'
  DRUG_NAME = 'Clarithromycin'
  INTERACTING_DRUG_CLASSES = ['Statin']
  INTERACTING_DRUG_NAMES = ['Simvastatin']


class Keflex(Medication):
  DRUG_CLASS = 'Cephalosporin'
  DRUG_NAME = 'Keflex'
  INTERACTING_DRUG_CLASSES = []
  INTERACTING_DRUG_NAMES = []


# Assert set 1
# Let's be sure we have interactions working as expected
assert Warfarin.interacts_with(Aspirin)
assert Simvastatin.interacts_with(Clarithromycin)
assert Lisinopril.interacts_with(Spironolactone)


# Now let's define a base allergy class
class Allergy:
  DRUG_CLASS = ''
  DRUG_NAME = ''

  @classmethod
  def interacts_with(cls, medication):
    if cls.DRUG_CLASS == medication.DRUG_CLASS:
      return True
    if cls.DRUG_NAME == medication.DRUG_NAME:
      return True
    return False


# And a specific allergy
class CephalosporinAllergy(Allergy):
  DRUG_CLASS = 'Cephalosporin'


# Assert Set 2
assert CephalosporinAllergy.interacts_with(Keflex)


class Patient:

  def __init__(self, medications, allergies):
    # This is a special method, __init__, called "the constructor"
    # it's called automatically when the class is instantiated
    self.medications = medications
    self.allergies = allergies

  ##method is a function that's attached to a class

  # --------------------------------------------------------------------------
  # BEGIN: Exercise 4 coding starts here -------------------------------------

  def is_allergic_to_med(self, medication):
    # TODO: Implement is_allergic_to_med
    # pass
    for allergy in self.allergies:
      if allergy.interacts_with(medication):
        return True
    return False

  def interactions_in_med_list(self):
    # TODO: Implement interactions_in_med_list
    # HINT: Order doesn't matter with interactions, so use sets, not lists
    # HINT: You may have an empty set, or a set of sets
    # HINT: Look at assert set 3
    interactions = {}  #empty set to store interactions
    for x in range(len(self.medications)
                   ):  #outer loop, iterates through each medication one by one
      for y in range(
          x + 1, len(self.medications)
      ):  #inner loop, starts from the next medication (x + 1) to avoid self-comparison
        med1 = self.medications[x]
        med2 = self.medications[y]
        #checking for interactions between med1 and med2
        if med1.interacts_with(med2):
          if med1 not in interactions:
            interactions[med1] = set()
          if med2 not in interactions:
            interactions[med2] = set()
          interactions[med1].add(
              med2)  #adds med2 to list of interactions for med1
          interactions[med2].add(
              med1)  #adds med1 to list of interactions for med2
    return interactions

  def potential_stop_list(self):
    # TODO: Implement potential_stop_list
    # HINT: Work with sets
    potential_stop_list = set()
    for med in self.medications:
      if self.is_allergic_to_med(med):
        potential_stop_list.add(med)
      for other_med in self.medications:
        if med != other_med and med.interacts_with(other_med):
          potential_stop_list.add(med)
    return potential_stop_list


# END: Exercise 4 coding starts here ---------------------------
# --------------------------------------------------------------------------

# Now let's create a patient with specific meds and allergies, and see
# what we can do to identify interactions and produce a potential stop list
medications = [
    Warfarin, Aspirin, Ibuprofen, Lisinopril, Spironolactone, Simvastatin,
    Clarithromycin, Keflex
]
allergies = [CephalosporinAllergy]
patient = Patient(medications, allergies)
interactions = patient.interactions_in_med_list()
potential_stop_list = patient.potential_stop_list()

# Assert set 3
assert patient.is_allergic_to_med(Keflex)
assert not patient.is_allergic_to_med(Aspirin)
assert interactions.issuperset({Warfarin, Aspirin})
assert interactions.issuperset({Simvastatin, Clarithromycin})
assert interactions.issuperset({Lisinopril, Spironolactone})
assert Keflex in potential_stop_list

print('all good...so far')
