# *-* coding:utf-8 *-*
import os
from decimal import Decimal

def greater(fixed_val):
    def _greater(val):
        return val > fixed_val
    return _greater

greater_100k = greater(1000)

print( greater_100k(999) )
print( greater_100k(999 + 2) )