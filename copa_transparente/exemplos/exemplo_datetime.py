# *-* coding:utf-8 *-*
import os
from decimal import Decimal
from datetime import date, datetime, timedelta

total = Decimal("0")

def get_value(info):
    try:
        start_str_date = info[8]
        end_str_date = info[9]
        start_date = datetime.strptime(start_str_date, '%d/%m/%Y')
        end_date = datetime.strptime(end_str_date, '%d/%m/%Y')
        date_diff = end_date - start_date
        if date_diff.days < 10:
            str_value = info[5]
            value = Decimal(str_value)
            return value
    except Exception as e:
        print(e)
        pass
    return Decimal('0')

with open(os.getcwd()+'/data/data/ExecucaoFinanceira.csv', 'r') as data:
    for line in data:
        total += get_value( line.strip().split(';') )

print('Total gasto com contratos de menos de 11 dias {}'.format(total) )

data_convertida = datetime.strptime('01/10/2015 10:30:55 520', '%d/%m/%Y %H:%M:%S %f')
diff = datetime.now() - data_convertida

print('diff.days ', diff.days )
dias = diff.total_seconds() / 60 / 60 / 24 #  minutes / hours / days
print('dias ', dias )

start_time = datetime.strptime('18:00', '%H:%M')
end_time = datetime.strptime('21:30', '%H:%M')
diff = end_time - start_time
print('diff.seconds ', diff.seconds )

birthday = datetime(2014, 1, 1 )
print('birthday', birthday)
next_birthday = birthday + timedelta(days=365)
print('next_birthday', next_birthday)