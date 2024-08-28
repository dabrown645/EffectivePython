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

print('Item 03: Know the differences between bytes and str')

# Example 1
heading("Example 01")
a = b'h\x65llo'
print(list(a))
print(a)


# Example 2
heading("Example 02")
a = 'a\u0300 propos'
print(list(a))
print(a)


# Example 3
heading("Example 03")
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))


# Example 4
heading("Example 04")
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))


# Example 5
heading("Example 05")
print(b'one' + b'two')
print('one' + 'two')


# Example 6
heading("Example 06")
try:
    b'one' + 'two'
except:
    logging.exception('Expected')
else:
    print("assert False")
    assert False


# Example 7
heading("Example 07")
try:
    'one' + b'two'
except:
    logging.exception('Expected')
else:
    assert False


# Example 8
heading("Example 08")
print("assert b'red' > b'blue'")
assert b'red' > b'blue'
print("assert 'red' > 'blue'")
assert 'red' > 'blue'


# Example 9
heading("Example 09")
try:
    print("assert 'red' > b'blue'")
    assert 'red' > b'blue'
except:
    logging.exception('Expected')
else:
    print("assert False")
    assert False


# Example 10
heading("Example 10")
try:
    print("assert b'blue' < 'red'")
    assert b'blue' < 'red'
except:
    logging.exception('Expected')
else:
    print("assert False")
    assert False


# Example 11
heading("Example 11")
print(b'foo' == 'foo')


# Example 12
heading("Example 12")
print(b'red %s' % b'blue')
print('red %s' % 'blue')


# Example 13
heading("Example 13")
try:
    print(b'red %s' % 'blue')
except:
    logging.exception('Expected')
else:
    print("assert False")
    assert False


# Example 14
heading("Example 14")
print('red %s' % b'blue')


# Example 15
heading("Example 15")
try:
    with open('data.bin', 'w') as f:
        f.write(b'\xf1\xf2\xf3\xf4\xf5')
except:
    logging.exception('Expected')
else:
    print("assert False")
    assert False


# Example 16
heading("Example 16")
with open('data.bin', 'wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')


# Example 17
heading("Example 17")
try:
    # Silently force UTF-8 here to make sure this test fails on
    # all platforms. cp1252 considers these bytes valid on Windows.
    real_open = open
    def open(*args, **kwargs):
        kwargs['encoding'] = 'utf-8'
        return real_open(*args, **kwargs)
    
    with open('data.bin', 'r') as f:
        data = f.read()
except:
    logging.exception('Expected')
else:
    print("assert False")
    assert False


# Example 18
heading("Example 18")
# Restore the overloaded open above.
open = real_open

with open('data.bin', 'rb') as f:
    data = f.read()

print("assert data == b'\xf1\xf2\xf3\xf4\xf5'")
assert data == b'\xf1\xf2\xf3\xf4\xf5'


# Example 19
heading("Example 19")
with open('data.bin', 'r', encoding='cp1252') as f:
    data = f.read()

print("assert data == 'ñòóôõ'")
assert data == 'ñòóôõ'

