# *-* coding:utf-8 *-*
import os

class DataTable:
    def __init__(self, name='', data=[]):
        self._name = name
        self._data = data

    @property
    def name(self):
        return self._name

tabela1 = DataTable(name='TabelaLegal', data=[1, 2, 3 ] )
print(DataTable.__dict__.keys())

# setar attributo, objeto, nome do atributo, valor
setattr(tabela1, 'posicao', 2)

if hasattr(tabela1, 'posicao'):
    print(tabela1.posicao)

if hasattr(tabela1, 'name'):
    # Pegando um attributo de maneira dinâmica
    print( getattr(tabela1, 'name') )
