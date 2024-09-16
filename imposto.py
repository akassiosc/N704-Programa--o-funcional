import unittest
   
# Função Lambda para calcular imposto sobre valor adicional
calcular_imposto = lambda valor: (valor - 1000) * 0.5 if valor > 1000 else 0

# List Comprehension para aplicar o imposto a uma lista de valores
def calcular_impostos_total(valores):
    return sum([calcular_imposto(valor) for valor in valores])

# Closure para aplicar um desconto no imposto total
def aplicar_desconto(desconto):
    def desconto_imposto(imposto):
        return imposto * (1 - desconto)
    return desconto_imposto

# Função de alta ordem que aplica uma função a todos os elementos de uma lista
def aplicar_funcao_em_lista(lista, funcao):
    return [funcao(item) for item in lista]

# Uso das funções no programa principal
if __name__ == "__main__":
    num_produtos = int(input("Quantos produtos você deseja calcular? "))
    valores = []
    for _ in range(num_produtos):
        valores.append(float(input("Digite o valor do produto: ")))

    total_impostos = calcular_impostos_total(valores)
    desconto_final = aplicar_desconto(0.1)
    total_com_desconto = desconto_final(total_impostos)

    print(f"O valor total do imposto a ser pago, após desconto, é de R$ {total_com_desconto:.2f}")
    
 
# Testando aplicações
class TestCalculoImposto(unittest.TestCase):
         
    def test_valor_maior_1000_com_desconto(self):
        desconto_final = aplicar_desconto(0.1)
        imposto_com_desconto = desconto_final(calcular_imposto(1500))
        self.assertEqual(imposto_com_desconto, 225)
        # Para um produto de 1500, o imposto seria 250 e com 10% de desconto, o imposto é 225
        
    def test_valor_menor_1000(self):
        self.assertEqual(calcular_imposto(800), 0)  
        # Produto com valor menor que 1000 não paga imposto
        
    def test_calculo_total_impostos(self):
        valores = [800, 1500, 2000]
        total_impostos = calcular_impostos_total(valores)  # Aplicando 10% de desconto
        desconto_final2 = aplicar_desconto(0.1)
        total_com_desconto2 = desconto_final2(total_impostos)
        self.assertEqual(total_com_desconto2, 675)
        # Impostos:
        # Produto 1 (800): 0
        # Produto 2 (1500): 225 (desconto aplicado)
        # Produto 3 (2000): 450 (desconto aplicado)
        # Total = 0 + 225 + 450 = 675
        
if __name__ == "__main__":
    unittest.main()
