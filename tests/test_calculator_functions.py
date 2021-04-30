import unittest
from Python_Classes.calculator_functions import add
from Python_Classes.calculator_functions import subtract
from Python_Classes.calculator_functions import multiply
from Python_Classes.calculator_functions import divide


class calculatorFunctionTest(unittest.TestCase):
    def test_add_result(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-8, -3), -11)
        self.assertEqual(add(-10, 3), -7)
        self.assertEqual(add(250000, 30000), 280000)

    def test_add_result_type(self):
        self.assertIsInstance(add(2, 3), int)
        self.assertIsInstance(add(-5, -3), int)
        self.assertIsInstance(add(-2000, 30000), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            add(4, "me")

    def test_subtract_result(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(-10, -5), -5)
        self.assertEqual(subtract(-20, 3), -23)
        self.assertEqual(subtract(-150000, -200000), 50000)

    def test_subtract_result_type(self):
        self.assertIsInstance(subtract(10, 3), int)
        self.assertIsInstance(subtract(-10, -5), int)
        self.assertIsInstance(subtract(-20, 3), int)

    def test_subtract_non_int_type(self):
        with self.assertRaises(TypeError):
            subtract(5, "we")

    def test_multiply_result(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(-6, 2), -12)
        self.assertEqual(multiply(-12, -12), 144)

    def test_multioly_result_type(self):
        self.assertIsInstance(multiply(10, 2), int)
        self.assertIsInstance(multiply(-5, 2), int)
        self.assertIsInstance(multiply(-6, -2), int)

    def test_multiply_non_int_type(self):
        with self.assertRaises(TypeError):
            multiply('2', '2')

    def test_divide_result(self):
        self.assertEqual(divide(4, 2), 2)

    def test_divide_result_type(self):
        self.assertIsInstance(divide(4, 2), int)
        self.assertIsInstance(divide(6,2), int)
        self.assertIsInstance(divide(10,5), int)

    def test_divide_non_int_type(self):
        with self.assertRaises(TypeError):
            divide('2', '2')


if __name__ == '__main__':
    unittest.main()
