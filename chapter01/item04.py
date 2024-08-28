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

print('Item 04: Prefer interpolated F-string over C-style format strings and str.format\n')

heading("Example 01")
a = 0b10111011
b = 0xc5f
print('Binary is %d, hex is %d' % (a, b))

heading("Example 02")
key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted)

heading("Example 03")
try:
    reordered_tuple = '%-10s - %.2f' % (value, key)
except:
    logging.exception('Expected')
else:
    assert False

heading("Example 04")
try:
    reordered_string = '%.2f = %-10s' % (key, value)
except:
    logging.exception('Expected')
else:
    assert False
 
heading("Example 05")
pantry = {
    ('avocados', 1.25),
    ('bananas', 2.5),
    ('cherries', 15),
}
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (i, item, count))
 
heading("Example 06")
for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count),
    ))
 
heading("Example 07")
template = '%s loves food. See %s cook.'
name = 'Max'
formatted = template % (name, name)
print(formatted)

heading("Example 08")
name = 'brad'
formatted = template % (name.title(), name.title())
print(formatted)

heading("Example 09")
key = 'my_var'
value = 1.234

old_way = '%-10s = %.2f' % (key, value)

new_way = '%(key)-10s = %(value).2f' % {
    'key': key, 'value': value,
}       # Original

reordered = '%(key)-10s = %(value).2f' % {
    'value': value, 'key': key,
}       # Swapped

#print(old_way)
#print(new_way)
#print(reordered)

print('assert old_way == new_way == reordered')
assert old_way == new_way == reordered

heading("Example 09")
name = 'Max'

template = '%s loves food. See %s cook.'
before = template % (name, name)        # Tuple

template = '%(name)s loves food. See %(name)s cook.'
after = template % {'name': name}

print('assert before == after')
assert before == after

heading("Example 10")
soup = 'lentil'
formatted = 'Today\'s soup is %(soup)s.' % {'soup': soup}
print(formatted)

heading("Example 11")
menu = {
    'soup': 'lentil',
    'oyster': 'kumamoto',
    'special': 'schnitzel',
}
template = ('Today\'s soup is %(soup)s, '
            'buy one get two %(oyster)s oysters, '
            'and our special entree is %(special)s.'
            )
formatted = template % menu
print(formatted)

heading("Example 12")
a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')

heading("Example 13")
key = 'my_var'
value = 1.234

formatted = '{} = {}'.format(key, value)
print(formatted)

heading("Example 14")
formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)

heading("Example 15")
print('%.2f%%' % 12.5)
print('{} replaces {{}}'.format(1.23))

heading("Example 15")
formatted = '{1} = {0}'.format(key, value)
print(formatted)

heading("Example 15")
formatted = '{0} loves food. See {0} cook'.format(name)
print(formatted)

heading("Example 16")
for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count),
    )

    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item.title(),
        round(count)
    )

    print('assert old_style == new_style')
    assert old_style == new_style

heading("Example 16")
formatted = 'First letter is {menu[oyster][0]!r}'.format(menu=menu)
print(formatted)

heading("Example 16")
old_template = (
    'Today\'s soup is %(soup)s, '
    'buy one get two %(oyster)s oysters, '
    'and our special entree is %(special)s.'
)
old_formatted = template % {
    'soup': 'lentil',
    'oyster': 'kumamoto',
    'special': 'schnitzel',
}

new_template = (
    'Today\'s soup is {soup}, '
    'buy one get two {oyster} oysters, '
    'and our special entree is {special}.'
)
new_formatted = new_template.format(
    soup='lentil',
    oyster='kumamoto',
    special='schnitzel',
)

#print(old_formatted)
#print(new_formatted)

print('assert old_formatted == new_formatted')
assert old_formatted == new_formatted

heading("Example 16")
key = 'my_var'
value = 1.234

formatted = f'{key} = {value:.2f}'
print(formatted)

heading("Example 17")
formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

heading("Example 18")
f_string = f'{key:<10} = {value:.2f}'

c_tuple = '%-10s = %.2f' % (key, value)

str_args = '{:<10} = {:.2f}'.format(key, value)

str_kw = '{key:<10} = {value:.2f}'.format(key=key, value=value)

c_dict = '%(key)-10s = %(value).2f' % {'key': key, 'value': value,}

print('assert c_tuple == c_dict == f_string')
assert c_tuple == c_dict == f_string
print('assert str_args == str_kw == f_string')
assert str_args == str_kw == f_string

heading("Example 19")
for i, (item, count) in enumerate(pantry):
    old_style = '#%d: %-10s = %d' % (
        i + 1,
        item.title(),
        round(count),
    )

    new_style = '#{}: {:<10s} = {}'.format(
        i + 1,
        item.title(),
        round(count),
    )

    f_string = f'#{i+1}: {item.title():<10s} = {round(count)}'

    #print(old_style)
    #print(new_style)
    #print(f_string)
#
    print('assert old_style == new_style == f_string')
    assert old_style == new_style == f_string

heading("Example 19")
for i, (item, count) in enumerate(pantry):
    print(f'#{i+1}: '
          f'{item.title():<10s} = '
          f'{round(count)}'
          )
