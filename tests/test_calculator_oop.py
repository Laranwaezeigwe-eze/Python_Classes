import unittest
from Python_Classes.calculator_oop import Calculator



class calculatorOopTest(unittest.TestCase):
    def test_add_result(self):
        self.assertEqual(Calculator.add(2,3),5)
        self.assertEqual(Calculator.add(-8, -3), -11)
        self.assertEqual(Calculator.add(-10, 3), -7)
        self.assertEqual(Calculator.add(250000, 30000), 280000)

    def test_add_result_type(self):
        self.assertIsInstance(Calculator.add(2, 3), int)
        self.assertIsInstance(Calculator.add(-5, -3), int)
        self.assertIsInstance(Calculator.add(-2000, 30000), int)

    def test_add_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.add(4, "me")

    def test_subtract_result(self):
        self.assertEqual(Calculator.subtract(10, 3), 7)
        self.assertEqual(Calculator.subtract(-10, -5), -5)
        self.assertEqual(Calculator.subtract(-20, 3), -23)
        self.assertEqual(Calculator.subtract(-150000, -200000), 50000)

    def test_subtract_result_type(self):
        self.assertIsInstance(Calculator.subtract(10, 3), int)
        self.assertIsInstance(Calculator.subtract(-10, -5), int)
        self.assertIsInstance(Calculator.subtract(-20, 3), int)

    def test_subtract_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.subtract(5, "we")

    def test_multiply_result(self):
        self.assertEqual(Calculator.multiply(2, 2), 4)
        self.assertEqual(Calculator.multiply(-6, 2), -12)
        self.assertEqual(Calculator.multiply(-12, -12), 144)

    def test_multiply_result_type(self):
        self.assertIsInstance(Calculator.multiply(10, 2), int)
        self.assertIsInstance(Calculator.multiply(-5, 2), int)
        self.assertIsInstance(Calculator.multiply(-6, -2), int)

    def test_multiply_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.multiply('4', '2')

    def test_divide_result(self):
        self.assertEqual(Calculator.divide(4, 2), 2)

    def test_divide_result_type(self):
        self.assertIsInstance(Calculator.divide(4, 2), int)
        self.assertIsInstance(Calculator.divide(6, 2), int)
        self.assertIsInstance(Calculator.divide(10, 5), int)

    def test_divide_non_int_type(self):
        with self.assertRaises(TypeError):
            Calculator.divide('2', 7)


if __name__ == '__main__':
    unittest.main()
