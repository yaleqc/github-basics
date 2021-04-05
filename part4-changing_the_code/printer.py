import os
import re

def regex_split_and_rejoin(string):
  split_string = re.split(r'_|\.', string)
  split_string.pop() # Remove .txt
  return " ".join(split_string)

def print_cell(name, contents):
  print('---\n')
  print(f'Name: {name}')
  print(f'Message: {contents}')
  print('\n---')

def main():
  for filename in os.listdir('people/'):
    with open(os.path.join('people/', filename), 'r') as f:
      name = regex_split_and_rejoin(filename)
      contents = f.read()
      print_cell(name, contents)

"""
  These are the names of the people who should be printed.
  seun omonije
  david pahl
"""
