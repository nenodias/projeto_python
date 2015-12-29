# *-* coding:utf-8 *-*
import os
'''
Caso queira ganhar os métodos adicionais append, reverse, extend, pop, remove e __iadd__
Para coleções mutáveis, extender MutableSequence
'''
from collections.abc import MutableSequence

class DataTable:
    def __init__(self, name='', data=[]):
        self._name = name
        self._data = data
        self._indice = 0


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    '''
        Define se determinado objeto está contido dentro dessa classe
    '''
    def __contains__(self, obj):
        return obj in self._data

    '''
        Define o comprimento dos dados contidos nessa classe
    '''
    def __len__(self):
        return len(self._data)

    '''
        Deve retornar um objeto iterável ( que implementa __next__ )
    '''
    def __iter__(self):
        return self

    '''
        Define que o objeto é um iterador, e caso o próximo seja o inicio da lista o StopIteration é lançado
    '''
    def __next__(self):
        try:
            elemento = self._data[self._indice]
        except IndexError as ie:
            self._indice = 0
            raise StopIteration
        self._indice += 1
        return elemento

    '''
        Define que o objeto é uma sequência, possui um indice
    '''
    def __getitem__(self, i):
        if isinstance(i, int) or isinstance(i, slice):
            return self._data[i]
        raise TypeError('Invalid index/slice object "{}"'.format( str(i) ) )

    def __setitem__(self, i, value):
        if isinstance(i, int):
            self._data[i] = value
        else:
            raise TypeError('Invalid index/slice object "{}"'.format( str(i) ) )

    def __delitem__(self, i):
        if isinstance(i, int):
            del self._data[i]
        else:
            raise TypeError('Invalid index/slice object "{}"'.format( str(i) ) )


tabela = DataTable(name='MinhaTabela', data=[1,3,4])
print('2 in tabela = ', 2 in tabela)
print('1 in tabela = ', 1 in tabela)
print('len(tabela) = ', len(tabela) )

for dado in tabela:
    print(dado)

print('tabela[1] = ', tabela[1])
print('tabela[1:3] = ', tabela[1:3])
tabela[0] = "texto"
print('tabela[0] = ', tabela[0])
del tabela[0]
print('tabela[0] = ', tabela[0])
print('len(tabela) = ', len(tabela) )