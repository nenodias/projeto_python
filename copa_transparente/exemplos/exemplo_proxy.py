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

    def __setattr__(self, attr_name, value):
        print('Acessando o atributo ',attr_name)
        if hasattr(self, attr_name):
            print('Atributo ',attr_name,' existe')
            # O Return vai bloquear alterações
            return 
        super(DataTable, self).__setattr__(attr_name, value)

    def __getattribute__(self, name):
        print('Caindo no __getattribute__')
        #Esse cara é mais baixo nível que o próprio getter e setter, que é usado no __getattr__ e setattr
        return super(DataTable, self).__getattribute__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

tabela = DataTable(name='TabelaBacana', data=[3, 2, 1] )
proxy = Proxy(tabela)
print(proxy.__dict__)
tabela.name = "LOL"
print(proxy.name)
