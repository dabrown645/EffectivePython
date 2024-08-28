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
print('Item 09: Avoid else blocks after for and while loops\n')

heading("Example 01")
for i in range(3):
    print('Loop', i)
else:
    print('Else block!')

heading("Example 02")
for i in range(3):
    print('Loop', i)
    if i == 1:
        break
else:
    print('Else block')

heading("Example 03")
for x in []:
    print('Never runs')
else:
    print('For Else block!')

heading("Example 04")
while False:
    print('Never runs')
else: print('While Esle block!')

heading("Example 05")
a = 4
b = 9

for i in range(2, min(a, b) +1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
else:
    print('Coprime')

heading("Example 06")
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

print('assert coprime(4, 9)')
assert coprime(4, 9)
print('assert not coprime(3, 6)')
assert not coprime(3, 6)

heading("Example 07")
def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

print('assert coprime_alternate(4, 9)')
assert coprime_alternate(4, 9)
print('assert not coprime_alternate(3, 6)')
assert not coprime_alternate(3, 6)

