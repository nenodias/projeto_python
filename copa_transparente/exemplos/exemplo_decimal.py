# *-* coding:utf-8 *-*
import os
from decimal import Decimal

total = Decimal('0')

with open(os.getcwd()+'/data/data/ExecucaoFinanceira.csv', 'r') as data:
    for line in data:
        try:
            info = line.split(';')
            str_value = info[5]
            
            total += Decimal(str_value)
        except Exception as e:
            print('error {}'.format(line))
print('Total gasto: {}'.format(total))