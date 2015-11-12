# *-* coding:utf-8 *-*

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
        self._data = []

    def add_column(self, name, kind, description):
        pass

class Column:
    """ Representa uma coluna em um DataTable 

        Essa classe contém as informações de uma coluna e deve validar um dado de acordo com o tipo de dado configurado no construtor

        Atributes:
            nome: Nome da Coluna
            kind: Tipo do dado (varchar, bigint, numeric)
            description: Descrição
    """
    def __init__(self,name, kind, description):
        """construtor

            Args:
                nome: Nome da Coluna
                kind: Tipo do dado (varchar, bigint, numeric)
                description: Descrição
        """
        self._name  = name
        self._kind = kind
        self._description = description
