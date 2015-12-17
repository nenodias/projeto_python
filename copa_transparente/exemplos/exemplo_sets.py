# *-* coding:utf-8 *-*
import os
from decimal import Decimal

def get_id_and_value(info, lower):
    value = Decimal(info[5])
    if value > lower:
        return info[2], value
    return None, Decimal(0)

all_companies = set()

intervals = [
            (Decimal('1000000000'), set()),
            (Decimal('500000000'), set()),
            (Decimal('100000000'), set()),
            (Decimal('10000000'), set()),
            (Decimal('1000000'), set()),
            (Decimal('100000'), set()),
            (Decimal('10000'), set()),
            (Decimal('1000'), set()),
            ]

for lower, companies in intervals:
    with open(os.getcwd()+'/data/data/ExecucaoFinanceira.csv', 'r') as data:
        for line in data:
            line = line.replace('\n', '')
            company_id, contract_value = get_id_and_value( line.strip().split(';'), lower )
            if company_id and not company_id in all_companies:
                companies.add(company_id)
            all_companies.add(company_id)

for lower, companies in intervals:
    print('{} empresas receberam mais de {}'.format(len(companies), lower) )
print('{} empresas no total'.format( len(all_companies) ) )


conjunto = set([1, 2, 3, 4, 5]) & set([2, 4])
print( conjunto )
conjunto = set([1, 2, 3, 4, 5]) | set([6, 7])
print( conjunto )
conjunto = set([1, 2, 3, 4, 5]).isdisjoint( set([6, 7]) )
print( conjunto )
conjunto = set([1, 2, 3, 4, 5]) > set([2, 4])
print( conjunto )
conjunto = set([1, 2]) < set([1, 2, 3, 4, 5])
print( conjunto )
conjunto = set([1, 2, 3]) - set([1, 3])
print( conjunto )
conjunto = set([1, 2, 3]) ^ set([2, 3])
print( conjunto )