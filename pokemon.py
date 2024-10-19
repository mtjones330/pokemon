#!/bin/python3

import os

os.system('clear')

while True:

  ndex = int(input("Ndex  : "))

  page = int(ndex / 9)
  slot = ndex % 9

  if slot == 0:
    slot = 9
  else:
    page = page + 1

  binder = 1

  if (page > 100):
    binder = 2
    page -= 100

  print(f'Binder: {binder}')
  print(f'Page  : {page}')
  print(f'Slot  : {slot}')
  print()


