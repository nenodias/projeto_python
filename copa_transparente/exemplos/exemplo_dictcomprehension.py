# *-* coding:utf-8 *-*
import os
from decimal import Decimal

total = Decimal('0')

schema = ('NumDocumento', 'ValContrato')

def dec(element, index):
    try:
        return Decimal(element[index])
    except:
        return Decimal('0')

with open(os.getcwd()+'/data/data/ExecucaoFinanceira.csv', 'r') as data_file:
    splited_data = [ line.strip().split(';') for line in data_file ]
    data = [ (element[2], dec(element, 12) ) for element in splited_data if len(element) > 2 ]
    result = [ { key:value for key, value in zip(schema, element) } for element in data ]

    for info_dict in result:
        print('{}'.format(info_dict) )

print('Total gasto: {}'.format( total ) )