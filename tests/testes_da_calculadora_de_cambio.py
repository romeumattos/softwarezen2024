from unittest import TestCase
import src.calculadora_de_cambio as calc

class TestesDaCalculadoraDeCambio(TestCase):

    def teste_exemplo(self):
        valor = 1
        taxa = 2
        resultado_esperado = 2

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_casa_decimal(self):
        valor = 2
        taxa = 4.334
        resultado_esperado = 8.67

        resultado_obtido = calc.converter(valor, taxa)

        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_valor_arrendodado(self):
        valor = 2
        taxa = 4.334
        resultado_esperado = 8.67

        resultado_obtido = calc.converter(valor, taxa)
                
        self.assertEqual(resultado_obtido, resultado_esperado)