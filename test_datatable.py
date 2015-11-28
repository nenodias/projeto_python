# *-* coding:utf-8 *-*
import unittest
from domain import DataTable

class DataTableTest(unittest.TestCase):

    def setUp(self):
        try:
            self.table = DataTable('Teste')
            # método que sempre será executado a cada "troca de testes"
            self.addCleanup(self.my_cleanup, ('cleanup executado'))
            self.out_file = open()
        except Exception as ex:
            print(ex)

    def test_add_column(self):
        self.assertEqual(0, len(self.table._columns) )

        self.table.add_column('BId', 'bigint')
        self.assertEqual(1, len(self.table._columns) )

        self.table.add_column('value', 'numeric')
        self.assertEqual(2, len(self.table._columns) )

        self.table.add_column('desc', 'varchar')
        self.assertEqual(3, len(self.table._columns) )

    def test_add_column_invalid_type(self):
        self.assertRaises(Exception, self.table.add_column, ('col', 'invalid') )
        # Parametros ( tipo de execao esperada, metodo chamado, tupla com argumentos para o metodo )

    def test_add_column_invalid_type_fail(self):
        error = False
        try:
            self.table.add_column('col', 'invalid')
        except Exception:
            error = True
        if not error:
            self.fail('Chamada não gerou um erro do tipo Exception')

    def my_cleanup(self, msg):
        print(msg)

    def tearDown(self):
        print('Nunca Executado')
