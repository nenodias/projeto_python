# *-* coding:utf-8 *-*
import os

class Proxy:

    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, name):
        print('Acesso ao atributo {}'.format(name) )
        if hasattr(self.obj, name):
            return getattr(self.obj, name)
        else:
            raise Exception('Atributo desconhecido')

class DataTable:
    def __init__(self, name='', data=[]):
        self._name = name
        self._data = data

    @property
    def name(self):
        return self._name

tabela = DataTable(name='TabelaBacana', data=[3, 2, 1] )
proxy = Proxy(tabela)
print(proxy.__dict__)
print(proxy.name)
