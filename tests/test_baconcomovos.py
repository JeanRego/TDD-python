"""
TDD - Teste Drive Development(desenvolvimento desenvolvido a teste)

Red
Parte 1 -> Criar teste e ver falhar

Green
Parte 2 -> Criar o teste e ver passar

Refactor

Parte 3 -> Melhorar o codigo 
"""
try:
    import sys
    import os
    
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise 

import unittest
from baconcomovos import bacon_com_ovos

class TestaBacoComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_erro_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('pio')
            
    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15,30,45,60)
        saida = 'Bacon com ovos'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), 
                    saida, msg=f'"{entrada}" nao retornou "{saida}"')
                
    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1,2,4,8)
        saida = 'Passar fome'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), 
                    saida, msg=f'"{entrada}" nao retornou "{saida}"')
                
    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3,6,9,12)
        saida = 'Bacon'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), 
                    saida, msg=f'"{entrada}" nao retornou "{saida}"')
                
    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multiplo_de_5(self):
        entradas = (5,10,20,25)
        saida = 'Ovos'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), 
                    saida, msg=f'"{entrada}" nao retornou "{saida}"')
            
if __name__ == '__main__':
    unittest.main(verbosity=2)