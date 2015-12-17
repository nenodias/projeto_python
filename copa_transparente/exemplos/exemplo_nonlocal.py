# *-* coding:utf-8 *-*
import os
from decimal import Decimal

def make_counter(count):
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def make_count():
    acc = []
    def counter(val):
        acc.append(val)
        return acc
    return counter

count = make_counter(2)
print( count() )
print( count() )
count = make_count()
print( count(1) )
print( count(4) )