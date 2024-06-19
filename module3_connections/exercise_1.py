# Exercise 1 introduces the Python `requests` module, which manages
# the HTTP cycle of requests and responses. It also uses the FHIR API
# provided by Canvas Medical to illustrate relevant server capabilities

# Brief slides: https://docs.google.com/presentation/d/11h3FWkwP-qVnzNunTRuECnVV_E28B4-5lr12cNz9f_c/edit

# Through this exercise you may want to see data in the UI (user interface)
# IMPORTANT! There is NO PHI in this instance of Canvas donated to CWC
# To see data in the UI, use these credentials:
# url: https://collective.canvasmedical.com
# username: hheimlich
# password: galore-ocean-turnout
# That should be enough to find the patient you're looking for
# But if youn need UI help, check here https://canvas-medical.zendesk.com/hc/en-us

import json
import requests
import sys
import datetime

CANVAS_FHIR_BASE_URL = 'https://fumage-collective.canvasmedical.com'
BEARER_TOKEN = '6Lqhcz0H41awO24CJssfrqrUDOY7bQfn'
HEADERS = {
    'Authorization': f"Bearer {BEARER_TOKEN}",
    'Content-Type': 'application/json'
}


def count_patients_by_name(name):
  params = {'name': name}
  resp = requests.get(CANVAS_FHIR_BASE_URL + '/Patient',
                      headers=HEADERS,
                      params=params)
  print(f"Status returned: {resp.status_code}")
  result = resp.json()
  print(f"Found {result['total']} matching patients")
  return result['total']


def count_kids_under_18():
  # TODO: Use the search parameters to count kids under 18
  # Hint: You may use birthdate to filter rather than age
  # Hint: https://docs.canvasmedical.com/api/patient/#search
  # pass

  ## old way -> hard coded date
  # params = {'birthDate': '2006-01-01'}
  # resp = requests.get(CANVAS_FHIR_BASE_URL + '/Patient',
  #                     headers=HEADERS,
  #                     params=params)
  # print(f"Status returned: {resp.status_code}")
  # result = resp.json()
  # print(f"Found {result['total']} matching patients")
  # return result['total']

  ## new way
  # calculate 18 years ago from today
  today = datetime.date.today()
  eighteen_years_ago = today - datetime.timedelta(days=18 * 365)
  birthdate_filter = eighteen_years_ago.strftime('%Y-%m-%d')

  # search for patients with birthdate before 18 years ago usinng the    birthdate filter
  params = {'birthDate': f'>{birthdate_filter}'}
  resp = requests.get(CANVAS_FHIR_BASE_URL + '/Patient',
                      headers=HEADERS,
                      params=params)
  print(f"Status returned: {resp.status_code}")
  result = resp.json()
  print(f"Found {result['total']} matching patients")
  return result['total']


def count_seniors_65_and_over():
  # TODO: Use the search parameters to count seniors 65 and over
  # Hint: You may use birthdate to filter rather than age
  # Hint: https://docs.canvasmedical.com/api/patient/#search
  # pass

  today = datetime.date.today()
  eighteen_years_ago = today - datetime.timedelta(days=65 * 365)
  birthdate_filter = eighteen_years_ago.strftime('%Y-%m-%d')

  params = {'birthDate': f'>{birthdate_filter}'}
  resp = requests.get(CANVAS_FHIR_BASE_URL + '/Patient',
                      headers=HEADERS,
                      params=params)
  print(f"Status returned: {resp.status_code}")
  result = resp.json()
  print(f"Found {result['total']} matching patients")
  return result['total']


def count_patients_with_allergies_on_record():
  # TODO: Find the number of patients with at least 1 allergy on record
  # Hint: You may search for allergies first, and then count unique patients
  # Hint: https://docs.canvasmedical.com/api/allergen/#search
  # pass

  # search for allergies
  params = {}
  resp = requests.get(CANVAS_FHIR_BASE_URL + '/AllergyIntolerance',
                      headers=HEADERS,
                      params=params)
  print(f"Status returned: {resp.status_code}")
  result = resp.json()
  print(f"Found {result['total']} matching allergies")
  return result['total']


# Below this line, your only edits should be commenting asserts in and out
# assert count_patients_by_name('May') == 2
# assert count_patients_by_name('Tuesday') == 1
# assert count_patients_by_name('Test') > 10
# assert isinstance(count_kids_under_18(), int)
# assert isinstance(count_seniors_65_and_over(), int)
assert isinstance(count_patients_with_allergies_on_record(), int)
print('OK')
