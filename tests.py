import unittest
from domain import *

class ColumnTest(unittest.TestCase):
    def test_validate_bigint(self):
        self.assertTrue(Column.validate('bigint', 1000))

if __name__ == '__main__':
    unittest.main()