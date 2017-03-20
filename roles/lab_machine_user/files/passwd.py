#!/usr/bin/python
import sys
from IPython.lib.security import passwd

# More info: https://ipython.org/ipython-doc/3/api/generated/IPython.lib.security.html
# This script is for creating passwd for jupython notebooks
print('Number of arguments:{} arguments.',  len(sys.argv))
print('Argument List:{}', str(sys.argv))

try:
    print passwd(str(sys.argv[1]))
except IndexError:
    print('Please specify password as argument')
