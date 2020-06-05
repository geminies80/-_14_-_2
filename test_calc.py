import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')

    def test_oper_pos(self):
        """ Возведение в степень"""
        self.assertEqual(calc_me(4, 2,"^"), 16)
    
    def test_oper_neg(self):
        """Негативный, возведение в степень"""
        self.assertEqual(calc_me(0, -3,"^"), "ERROR: ZeroDivisionError!")        
    
    def test_without_perem(self):
        """Функция calc.me без переменной Number 1"""
        self.assertEqual(calc_me(None,3,"-"), "ERROR: send me Number1")

    def test_without_perem_2(self):
        """Функция calc.me без переменной Number 2"""
        self.assertEqual(calc_me(3, None,"-"), "ERROR: send me Number2")
    
    def test_input_1(self):
        """Символьные переменные"""
        self.assertEqual(calc_me("m", 9,"-"), 'ERROR: it is not supported')
    
    def test_input_2(self):
        """Символьные переменные"""
        self.assertEqual(calc_me(9,"m","-"), 'ERROR: it is not supported')

    def test_input_3(self):
        """Символьные переменные"""
        self.assertEqual(calc_me("m", "m","-"), 'ERROR: it is not supported')

if __name__ == '__main__':
    unittest.main(verbosity=2)