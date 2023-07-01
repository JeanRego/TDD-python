try:
    import sys
    import os
    
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '..'
            )
        )
    )
except:
    raise

import unittest
from divisao import divisao, divisao_com_resultado_inteiro

class TasteDivisao(unittest.TestCase):
    def test_divide_10_por_20_deve_retornar_0_5(self):
        self.assertEqual(divisao(10,20), 0.5)
        
    def test_divide_10_por_2_deve_retornar_5(self):
        self.assertEqual(divisao(10,2),5)
    
    def test_divide_e_retorna_resultado_inteiro(self):
        self.assertEqual(divisao_com_resultado_inteiro(10,20), 0)
        
    def test_divide_e_retorna_inteiro(self):
        self.assertEqual(divisao_com_resultado_inteiro(190190.15,9999999), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)