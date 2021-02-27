from __future__ import annotations
import pickle
from table import Table
from time import sleep, localtime, strftime
import os
from btree import Btree
import shutil
from misc import split_condition

'''
Database class contains tables.
'''

'''
Test the Hash index
'''

'''
1) python3 -i smallRelationsInsertFile.py
3) db = Database("smdb", load=True)
4) db.show_table('student')
'''



lst = ['Comp. Sci.', 'History', 'Finance', 'Physics', 'Elec. Eng.', 'Biology', 'Music']


for el in lst:
    sum = 0
    string_len = len(el)
    print ("\n", el)
    # print (string_len)
    for val in [ord(c) for c in el]:
        # print (val)
        sum = sum + val
    b = sum % string_len
    b = b ** string_len
    print (sum, " -> ", b)
