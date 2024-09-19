from unittest import TestCase
import src.calculadora_de_cambio as calc

class TestesDaCalculadoraDeCambio(TestCase):

    def teste_casa_decimal(self):
        valor = 2.23
        taxa = 4.34890

        resultado_obtido = calc.converter(valor, taxa)
        
        tem_duas_casas_decimais = (resultado_obtido * 100) % 1 == 0

        self.assertTrue(tem_duas_casas_decimais)
        
    def teste_valor_arredondado(self):
        valor = 2.23
        taxa = 4.34890
        resultado_esperado = 9.69

        resultado_obtido = calc.converter(valor, taxa)
                
        self.assertEqual(resultado_obtido, resultado_esperado)