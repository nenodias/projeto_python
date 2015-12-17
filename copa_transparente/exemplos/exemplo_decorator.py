# *-* coding:utf-8 *-*
import os

def uma_funcao():
    print('uma função')

def outra_funcao(func):
    print('outra função')
    func()

outra_funcao(uma_funcao)

def uma_funcao_com_args(param):
    print('uma funcao param {}'.format(param) )

def outra_funcao_com_args(func, *args):
    print('irei chamar {}'.format(func.__name__))
    return func(*args)

outra_funcao_com_args( uma_funcao_com_args, [ 1,2,3 ] )
outra_funcao_com_args( sum, [1, 2, 3] )

def trace_call(func):
    def inner(*args, **kwargs):
        print('Função executada: {} args: {}'.format( func.__name__, args ) )
        return func(*args, **kwargs)
    return inner

@trace_call
def add(x, y):
    return x + y

x = add(5, 1)
print(x)

class trace_function():
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print('Função executada: {} args: {}'.format( self.f.__name__, args ) )
        return self.f(*args, **kwargs)

@trace_function
def sub(x, y):
    return x - y

x = sub(5, 1)
print(x)