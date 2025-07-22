import unittest
from TODO_number_to_words import number_to_words

class TestInvalidInput(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(number_to_words(None), None)
    def test_num_str(self):
        self.assertEqual(number_to_words('eyy'), None)

    def test_num_vir(self):
        self.assertEqual(number_to_words(123.4), None)

    def test_range_min(self):
        self.assertEqual(number_to_words(0), None)

    def test_range_max(self):
        self.assertEqual(number_to_words(4000), None)

class TestOneToNineteen(unittest.TestCase):
    def test_1(self):
        self.assertEqual(number_to_words(1), 'one')
    def test_9(self):
        self.assertEqual(number_to_words(9), 'nine')

class TestCompounds_20_99(unittest.TestCase):
    def test_20(self):
        self.assertEqual(number_to_words(20), 'twenty')
    def test_21(self):
        self.assertEqual(number_to_words(21), 'twenty one')