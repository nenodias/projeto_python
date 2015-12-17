# *-* coding:utf-8 *-*
import os
from decimal import Decimal

def get_generator():
    for i in range(10):
        yield i

for number in get_generator():
    print(number)

gerador = get_generator()
print( next(gerador) )
print( next(gerador) )
print( next(gerador) )