# *-* coding:utf-8 *-*

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

    def add_column(self, name, kind, description=''):
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        relationship = Relationship(name, self, to, on)
        self._references = relationship

    def add_recerenced(self, name, bt, on):
        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)

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
    print(Column('IdEmpreendimento', 'bigint'))
    print(PrimaryKey(table,'IdEmpreendimento', 'bigint'))
