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
print("Item 06: Prefer Multiple assignment unpacking over indexing\n")

heading("Example 01")
snack_calories = {
    "chips": 140,
    "popcorn": 80,
    "nuts": 190,
}
items = tuple(snack_calories.items())
print(items)

heading("Example 02")
item = ( "Peanut Butter", "Jelly", )
first = item[0]
second = item[1]
print(first, "and", second)

heading("Example 03")
pair = ("Chocolate", "Peanut butter",)

try:
    pair[0] = "Honey"
except:
    logging.exception('Expected')
else:
    assert False
     

heading("Example 04")
item = ("Peanut butter", "Jelly",)
first, second = item        # Unpacking
print(first, "and", second)

heading("Example 06")
favorite_snacks = {
    "salty": ("pretzels", 100,),
    "sweet": ("cookies", 180,),
    "veggie": ("carrots", 20,),
}

((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3)),
 ) = favorite_snacks.items()
print(f"Favorite {type1} is {name1} with {cals1} calories")
print(f"Favorite {type2} is {name2} with {cals2} calories")
print(f"Favorite {type3} is {name3} with {cals3} calories")

heading("Example 07")
def bubble_sort(a):
    for j in range(len(a)):         # loop to access each array element
        for j in range(1,len(a)):   # loop to compary array elements
            if a[j] < a[j-1]:       # Decending order
                a[j-1], a[j] = a[j], a[j-1]      # Swap items

names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)

heading("Example 08")
snacks = [('bacon', 350,), ('donut', 240,), ('muffin', 190),]
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i+1}: {name} has {calories} calories')
