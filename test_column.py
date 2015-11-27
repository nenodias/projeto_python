import unittest
from domain import *

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

if __name__ == '__main__':
    unittest.main()