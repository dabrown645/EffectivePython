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
print('Item 14: Sort by complex criteria using the key parameeter\n')

heading("Example 01")
numbers = [93, 86, 11,68, 70,]
numbers.sort()
print(numbers)

heading("Example 02")
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25),
]

heading("Example 03")
try:
    tools.sort
except:
    logging.expection('Expected')

heading("Example 04")
print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted:  ', tools)

heading("Example 05")
tools.sort(key=lambda x: x.weight)
print('Sorted:  ', tools)

heading("Example 06")
places = ['home', 'work', 'New York', 'Paris',]
places.sort()
print('Case sensitive    :', places)
places.sort(key=lambda x: x.lower())
print('Case insensitive  :', places)

heading("Example 07")
power_tools= [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

heading("Example 08")
saw = (5, 'circular saw')
jackhammer = (40, 'jackhammer')
assert not ( jackhammer < saw )

heading("Example 09")
drill = (4, 'drill')
sander = (4, 'sander')
assert drill[0] == sander[0]
assert drill[1] < sander[1]
assert drill < sander

heading("Example 10")
power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

heading("Example 11")
power_tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
print(power_tools)

heading("Example 12")
try:
    power_tools.sort(key=lambda x: (x.weight, -x.name), reverse=True)
except:
    logging.exception('Expected')
else:
    assert False

heading("Example 13")
power_tools.sort(key=lambda x: x.name)
power_tools.sort(key=lambda x: x.weight, reverse=True)
print(power_tools)

heading("Example 14")
power_tools.sort(key=lambda x: x.name)
print(power_tools)

power_tools.sort(key=lambda x: x.weight, reverse=True)
print(power_tools)
