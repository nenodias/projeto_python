# *-* coding:utf-8 *-*
import unittest
from domain import DataTable, Column

class DataTableTest(unittest.TestCase):

    def setUp(self):
        try:
            self.table = DataTable('Teste')
            # método que sempre será executado a cada "troca de testes" independente de algum erro não tratado ocorrer no setUp
            self.addCleanup(self.my_cleanup, ('cleanup executado'))
            self.out_file = open()
        except Exception as ex:
            pass

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

    def test_add_relationship(self):
        a_table = DataTable('A')
        col = a_table.add_column('BId', 'bigint')
        b_table = DataTable('B')
        b_table.add_column('BId', 'bigint')
        a_table.add_references('B', b_table, col)

        self.assertEqual(1, len(a_table.references))
        self.assertEqual(0, len(a_table.referenced))

    def test_add_reverse_relationship(self):
        a_table = DataTable('A')
        col = a_table.add_column('BId', 'bigint')
        b_table = DataTable('B')
        col = b_table.add_column('BId', 'bigint')
        b_table.add_referenced('A', a_table, col)

        self.assertEqual(1, len(b_table.referenced))
        self.assertEqual(0, len(b_table.references))

    def my_cleanup(self, msg):
        ''' Método que faz liberação de recursos, permitindo que ocorra erros dentro do setUp '''
        print(msg)

    def tearDown(self):
        ''' Método que faz liberação de recursos, porém não é executado caso um erro não seja tratado no setUp '''
        pass
        #print('Nunca Executado')

class ColumnTest(unittest.TestCase):

    def test_validate_bigint(self):
        self.assertTrue(Column.validate('bigint', 100))
        self.assertTrue(not Column.validate('bigint', 10.0))
        self.assertTrue(not Column.validate('bigint', "Texto"))

    def test_validate_numeric(self):
        self.assertTrue(Column.validate('numeric', 10.0))
        self.assertTrue(Column.validate('numeric', 100))
        self.assertTrue(not Column.validate('numeric', "Texto"))

    def test_validate_varchar(self):
        self.assertTrue(Column.validate('varchar', "Texto"))
        self.assertTrue(not Column.validate('varchar', 100))
        self.assertTrue(not Column.validate('varchar', 10.0))