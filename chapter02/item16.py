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
print('Item 16: Prefer get over in and KeyError to handle missing dictionary keys\n')

heading('Example 01')
counters = {
    'pempernicle': 2,
    'sourdough': 1,
}

key = 'wheat'

if key in counters:
    counter = counters[key]
else:
    counter = 0

counters[key] = counter + 1
print(counters)

heading('Example 02')
try:
    count = counters[key]
except KeyError:
    count = 0

counters[key] = count + 1
print(counters)

heading('Example 03')
key = 'rye'
count = counters.get(key, 0)
counters[key] = count + 1
print(counters)

heading('Example 04')
if key not in counters:
    counters[key] = 0
counters[key] += 1
print(counters)

if key in counters:
    counters[key] += 1
else:
    counters[key] = 0
print(counters)

key = 'potato'
try:
    counters[key] += 1
except KeyError:
    counters[key] = 1
print(counters)

heading('Example 05')
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}
key = 'brioche'
who = 'Elmer'

if key in votes:
    names = votes[key]
else:
    votes[key] = names = []

names.append(who)
print(votes)

heading('Example 06')
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}
key = 'brioche'
who = 'Elmer'

try:
    names = votes[key]
except KeyError:
    votes[key] = names = []

names.append(who)
print(votes)

heading('Example 07')
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}
key = 'brioche'
who = 'Elmer'

names = votes.get(key)
if names is None:
    votes[key] = names = []

names.append(who)
print(votes)

heading('Example 08')
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}
key = 'brioche'
who = 'Elmer'

if (names := votes.get(key)) is None:
    votes[key] = names = [] 

names.append(who)
print(votes)

heading('Example 09')
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}
key = 'brioche'
who = 'Elmer'

names = votes.setdefault(key,[])
names.append(who)
print(votes)

heading('Example 10')
data = {}
key = 'foo'
value = []
data.setdefault(key, value)
print('Before: ', data)
value.append('hello')
print('After:  ', data)

heading('Example 11')
