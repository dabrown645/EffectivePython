#!/usr/bin/env python3
#!/usr/bin/env PYTHONHASHSEED=1234 python3

# Copyright 2014-2019 Brett Slatkin, Pearson Education Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Reproduce book environment
import random
random.seed(1234)

import logging
from pprint import pprint
from sys import stdout as STDOUT

# Write all output to a temporary directory
import atexit
import gc
import io
import os
import tempfile

TEST_DIR = tempfile.TemporaryDirectory()
atexit.register(TEST_DIR.cleanup)

# Make sure Windows processes exit cleanly
OLD_CWD = os.getcwd()
atexit.register(lambda: os.chdir(OLD_CWD))
os.chdir(TEST_DIR.name)

def close_open_files():
    everything = gc.get_objects()
    for obj in everything:
        if isinstance(obj, io.IOBase):
            obj.close()

atexit.register(close_open_files)

# My stuff to make things easer
def heading(title='Missing'):
    print(f'{title:-^30}')

# End my stuff
print('Item 10: Prevent repitition and assignment expressions\n')

heading("Example 01")
fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}

heading("Example 02")
def make_lemonade(count):
    print(f'Making {count} lemons into lemonaid')

def out_of_stock():
    print(f'Out of stock')

count = fresh_fruit.get('lemon', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

heading("Example 03")
if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

heading("Example 04")
def make_cider(count):
    print(f'Making cider with {count} apples')


count = fresh_fruit.get('apple', 0)
if count >= 4:
    make_cider(count)
else:
    out_of_stock()

heading("Example 05")
if (count := fresh_fruit.get('apple', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()

heading("Example 06")
def slice_bananas(count):
    print(f'Slicing {count} bananas')
    return count * 4

class OutOfBananas(Exception):
    pass


def make_smoothies(count):
    print(f'Making a smothie with {count} banana slices')

pieces = 0
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(pieces)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

heading("Example 07")
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

heading("Example 08")
pieces = 0
if (count := fresh_fruit.get('banana', 0)) >=2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

heading("Example 09")
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smooties = make_smoothies(pieces)
except OutOfBananas:
    out_fo_stock()

heading("Example 10")
count = fresh_fruit.get('apple', 0)
if count >= 4:
    to_enjoy = make_cider(count)
else:
    count = fresh_fruit.get('apple', 0)
    if count >= 4:
        pieces = slice_bananas(count)
        to_enjoy = make_smoothies(pieces)
    else:
        count = fresh_fruit.get('lemon', 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = 'Nothing'

print(to_enjoy)

heading("Example 11")
if (count := fresh_fruit.get('banana', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('apple', 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get('lemon', 0):
    to_enjoyu = make_lemonade(count)
else:
    to_enjoy = 'Nothing'

print(to_enjoy)

heading("Example 12")
FRUIT_TO_PICK = [
    {'apple': 1, 'banana': 3},
    {'lemon': 2, 'lime': 5},
    {'orange': 3, 'melon': 2},
]

def pick_fruit():
    if FRUIT_TO_PICK:
        return FRUIT_TO_PICK.pop(0)
    else:
        return []

def make_juice(fruit, count):
    return [(fruit, count)]

bottles = []
while fresh_fruit:
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit()

print(bottles)

heading("Example 13")
FRUIT_TO_PICK = [
    {'apple': 1, 'banana': 3},
    {'lemon': 2, 'lime': 5},
    {'orange': 3, 'melon': 2},
]

bottles = []
while True:         # loop
    fresh_fruit = pick_fruit()
    if not fresh_fruit:     # And a half
        break
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print(bottles)

heading("Example 14")
FRUIT_TO_PICK = [
    {'apple': 1, 'banana': 3},
    {'lemon': 2, 'lime': 5},
    {'orange': 3, 'melon': 2},
]

bottles = []
while fresh_fruit := pick_fruit():
    batch = make_juice(fruit, count)
    bottles.extend(batch)

print(bottles)

