# *-* coding:utf-8 *-*
import os

'''

Por definição no Python só existe um construtor,
caso exista a necessidade de vários construtores como no java
usa-se a convenção de argumentos nomeados / (argumentos padronizados)

ex: logo abaixo

class DataTable:
    def __init__(self, name='', data=[]):
        self.name = name
        self.data = data

# -------------------------------------------

class DataTable:
    def __init__(self, name):
        self.name = name

    def __init__(self, data):
        self.data = data

Desse jeito está errado,
sempre o último construtor declarado é o que vale

# -------------------------------------------

class DataTable:
    def __init__(self, name):
        self.name = name


Dessa forma o parâmetro name será obrigatório
Uma chamada sem ele resultaria em uma exception

'''
class Column:
    def __init__(self, name, kind, description=''):
        print(type(self))
        self._name = name
        self._kind = kind
        self._description = description

    '''
        Representação informal, utilizada quando o print
        ou o str passando o objeto são chamados
    '''
    def __str__(self):
        return "Coluna {}".format( self._name )

class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=''):
        Column.__init__(self, name, kind, description=description)
        self.is_pk = True

    @property
    def name(self):
        return self._name

class DataTable:
    def __init__(self, name='', data=[]):
        self._name = name
        self._data = data

    @property
    def name(self):
        return self._name

    '''
        Representação formal,
        o ideal desse metodo é que o objeto possa
        ser reciado a partir do resultado desse método
        (como um json, xml, csv, etc)
    '''
    def __repr__(self):
        return '{ name : %s, data : %s }'%(self._name, self._data)

    '''
        a comparação só vai considerar a propriedade nome, para
        considerar igual
    '''
    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        return 0


pk = PrimaryKey(None, 'PK', 'int')
print('Usando __str__: ', pk)

tabela1 = DataTable(name='ExecucaoFinanceira', data=[1,2])
tabela2 = DataTable(name='ExecucaoFinanceira', data=[])
str_tabela = str(tabela1)
print('Usando __repr__: ', str_tabela)

tabela3 = DataTable(name='ExecucaoProgramada', data=[])

print('tabela1 == tabela2 ? ', tabela1 == tabela2 )
print('tabela1 == tabela3 ? ', tabela1 == tabela3 )

'''
Sobrecarga de operadores lógicos

método      sinal
__eq__  <->   ==
__lt__  <->   <
__le__  <->   <=
__ne__  <->   !=
__gt__  <->   >
__ge__  <->   >=

Sobrecarga de operadores matemáticos

método      sinal
__add__ <->   +
__sub__ <->   -
__mul__ <->   *

'''

print( tabela1 + tabela2 )
