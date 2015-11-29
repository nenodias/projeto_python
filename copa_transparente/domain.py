# *-* coding:utf-8 *-*
from __future__ import unicode_literals

from decimal import Decimal


class Relationship:

    def __init__(self, name, _from, to, on):
        self._name = name
        self._from = _from
        self._to = to
        self._on = on


class DataTable:
    """Representa uma tabela de dados.

       Essa classe Representa uma tabela de dados do portal da transparência.
       Deve ser capaz de validar linhas inseridas de acordo com as colunas que possui.
       As linhas inseridas ficam registradas dentro dela.

       Atributes:
            nome: Nome da Tabela
            columns: [Lista de colunas]
            data: [Lista de dados]
    """
    def __init__(self, name):
        """construtor

           Args:
            name: Nome da Tabela
        """
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []

    def _get_name(self):
        print("Getter executado")
        return self._name

    def _set_name(self, _name):
        print("Setter executado")
        self._name = _name

    def _del_name(self):
        print("Delete executado")
        raise AttributeError("Não pode deletar esse atributo")

    name = property(_get_name, _set_name, _del_name)
    references = property(lambda self: self._references)
    referenced = property(lambda self: self._referenced)

    def add_column(self, name, kind, description=''):
        self._validate_kind(kind)
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)

    def _validate_kind(self, kind):
        if not kind in ('bigint', 'numeric', 'varchar'):
            raise Exception('Tipo Inválido')

class Column:
    """ Representa uma coluna em um DataTable

        Essa classe contém as informações de uma coluna e deve validar um dado de acordo com o tipo de dado configurado no construtor

        Atributes:
            nome: Nome da Coluna
            kind: Tipo do dado (varchar, bigint, numeric)
            description: Descrição
    """
    def __init__(self,name, kind, description=''):
        """construtor

            Args:
                nome: Nome da Coluna
                kind: Tipo do dado (varchar, bigint, numeric)
                description: Descrição
        """
        self._name  = name
        self._kind = kind
        self._description = description
        self._is_pk = False

    def _validate(kind, data):
        """
            staticmethod é quando é um método estático
            existe também o classmethod, que o primeiro argumento é a instância da classe
            ex:
            def _validate(cls, kind, name):
                pass

            validate = classmethod(_validate)
        """
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        if kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        if kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True
    validate = staticmethod(_validate)

    def __str__(self):
        _str = "Col: {} : {} {}".format(self._name, self._kind, self._description)
        return _str

class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=''):
        super().__init__(name, kind, description=description)
        self._is_pk = True

    def __str__(self):
        _str = super().__str__()
        return "{} - {}".format("PK", _str)

if __name__ == '__main__':
    table = DataTable("Empreendimento")
    table.name
    table.name = "Alerta"
    del table.name
    print(Column('IdEmpreendimento', 'bigint'))
    print(PrimaryKey(table,'IdEmpreendimento', 'bigint'))
