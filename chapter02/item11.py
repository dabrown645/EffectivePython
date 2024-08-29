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
print('Item 11: Know how to slice sequences\n')

heading("Example 01")
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',]
print('a:            ', a)
print('Middle two:   ', a[3:5])
print('All but ends: ', a[1:7])

heading("Example 02")
print(a[:5])
assert a[:5] == a[0:5]
print(a[5:])
assert a[5:] == a[5:len(a)]

heading("Example 03")
print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])

heading("Example 04")
first_twenty_items = a[:20]
last_twenty_items = a[-20:]

print(first_twenty_items)
print(last_twenty_items)
try:
    print(a[20])
except:
    logging.exception('Expected')


heading("Example 05")
b = a[3:]
print('Before:     ', b)
b[1]=99
print('After:      ', b)
print('No_change:  ', a)

heading("Example 06")
print('Before: ', a)
print(a[2:7])
a[2:7] = [99, 22, 14]
print('After:  ', a)

print('Before: ', a)
print(a[2:3])
a[2:3] = [47, 11]
print('After   ', a)

heading("Example 07")
b = a[:]
print(a[:])
print(b)
assert b ==a and b is not a

heading("Example 08")
b = a
print('Before a: ', a)
print('Before b: ', b)
a[:] = [101, 102, 103,]
print('After a:  ', a)
print('After b:  ', b)
