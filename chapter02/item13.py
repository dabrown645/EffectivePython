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
print('Item 13: Prefer catch-all unpacking over slicing\n')

heading("Example 01")
car_ages = [ 0, 9, 4, 8, 7, 20, 19, 1, 6, 15, ]
car_ages_decending = sorted(car_ages, reverse=True)
try:
    oldest, second_oldest = car_ages_decending
except:
    logging.exception('Expected')
else:
    assert False

heading("Example 02")
oldest = car_ages_decending[0]
second_oldest = car_ages_decending[1]
others = car_ages_decending[2:]
print(oldest, second_oldest, others)

heading("Example 03")
oldest, second_oldest, *others = car_ages_decending
print(oldest, second_oldest, others)

heading("Example 04")
oldest, *others, youngest = car_ages_decending
print(oldest, youngest, others)

*others, second_youngest, youngest = car_ages_decending
print(youngest, second_youngest, others)

heading("Example 05")
try:
    source = """*others = car_ages_decending"""
    eval(source)
except:
    logging.exception('Expected')
else:
    assert False

heading("Example 06")
try:
    source = """first, *middle, *second_middle, last = [1, 2, 3, 4]"""
    eval(source)
except:
    logging.exception('Expected')
else:
    assert False

heading("Example 07")
car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC',),
    'Airport': ('Skyline', 'Viper', 'Gremiln', 'Nova',)
}

((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = car_inventory.items()
print(f'Best at {loc1} is {best1}, {rest1}')
print(f'Best at {loc2} is {best2}, {rest2}')

heading("Example 08")
short_list = [1, 2]
first, second, *rest = short_list
print(first, second, rest)

heading("Example 09")
it = iter(range(1,3))
first, second = it
print(f'{first} and {second}')

heading("Example 10")
def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')
    for i in range(100):
        yield ('2019-03-25', 'Honda', 'Fit', '2010', '$3400')
        yield ('2019-03-26', 'Ford', 'F150', '2008', '$2400')

list(generate_csv())

heading("Example 11")
all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV Header: ', header)
print('Row count:  ', len(rows))
