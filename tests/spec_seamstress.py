import unittest
from should_dsl import should, should_not
from seamstress import Seamstress


class TestSeamstress(unittest.TestCase):
    
    def setUp(self):
        self.seamstress = Seamstress(1, 'Maria', 650, 'zig-zag')

    def test_seamstress_initialization(self):
        (Seamstress, 1, 'Maria', -56, 'zig-zag') |should| throw(ValueError)
        self.seamstress.register |should| equal_to(1)
        self.seamstress.name |should| equal_to('Maria')
        self.seamstress.minimum_value |should| equal_to(650)
        self.seamstress.hability |should| equal_to('zig-zag')

    def 