#!/bin/python3

import os

os.system('clear')

while True:

  ndex = int(input("Ndex: "))

  page = int(ndex / 9)
  slot = ndex % 9

  if slot == 0:
    slot = 9
  else:
    page = page + 1

  print(f'Page: {page}')
  print(f'Slot: {slot}')
  print()
    

