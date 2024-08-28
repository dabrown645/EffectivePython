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

print("Item 05: Write helper functions instead of complex expressions\n")

from urllib.parse import parse_qs

heading("Example 01")
my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
print(repr(my_values))

print("Red:       ", my_values.get('red'))
print("Green:     ", my_values.get('green'))
print("Opacity:   ", my_values.get('opacity'))

heading("Example 02")
# Fore query string "red=5&blue=0&green-"
red = my_values.get("red", [""])[0] or 0
green = my_values.get("green", [""])[0] or 0
opacity = my_values.get("opacity", [""])[0] or 0

print(f"Red:         {red!r}")
print(f"Green:       {green!r}")
print(f"Opacity:     {opacity!r}")

heading("Example 03")
# Fore query string "red=5&blue=0&green-"
red = int(my_values.get("red", [""])[0] or 0)
green = int(my_values.get("green", [""])[0] or 0)
opacity = int(my_values.get("opacity", [""])[0] or 0)

print(f"Red:         {red!r}")
print(f"Green:       {green!r}")
print(f"Opacity:     {opacity!r}")

heading("Example 04")
def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    return default

print(f"Red:     {get_first_int(my_values, "red")}")
print(f"Green:   {get_first_int(my_values, "green")}")
print(f"Opacity: {get_first_int(my_values, "opacity")}")
