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
print('Item 12: Avoid striding ans slicing in a single expression\n')

heading("Example 01")
x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

heading("Example 02")
y = b'mongoose'
z = y[::-1]
print(y)
print(z)

heading("Example 03")
x = '寿司'
y = x[::-1]
print(y)

heading("Example 04")
try:
    w = '寿司'
    x = w.encode('utf-8')
    y = x[::-1]
    z = y.decode('utf-8')
except:
    logging.exception('Expeted')

heading("Example 05")
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',]

print(f'x[::2]       # {x[::2]}')
print(f'x[-2::-2]    # {x[-2::-2]}')
print(f'x[-2:2:-2]   # {x[-2:2:-2]}')
print(f'x[2:2:-2]    # {x[2:2:-2]}')

heading("Example 06")
y = x[::2]   # {x[::2]}')
z = y[1:-1]  # {y[1:-1]}')

print(x)
print(y)
print(z)
