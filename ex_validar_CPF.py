"""
    CPF: 746.824.890-70
    Colete asoma dos 9 primeiros dígitos do CPF
    multiplicando cada um dos valores por uma
    contagem regressiva começando de 10
    
    ex: 746.824.980.-70(746824890)
    10 9  8  7  6  5  4  3  2  
    7  4  6  8  2  4  8  9  0 
    70 36 48 56 12 20 32 27 0 
    
    Somar todos os resultados
    70+36+48+3+12+20+20+27+0 = 301
    Multiplicar o resultado anterior por 10
    301 * 10 = 3010
    Obter o restp da divisão da conta anterior por 11
    3010 % 11 = 7
    Se p resultado anterior for maior que 9:
    Resultado é 0
    Contrário disso: 
    resultadoo é o valorr da conta
    
    o primeiro digito do CPF é 7
"""
import random


nove_digitos= ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

    contador_regressivo_1 = 10



# 1. Definição da variável 'cpf_completo' 
cpf_completo = '746.824.890-70' 

# 2. Uso da variável para substituir os caracteres e tirar espaço
cpf_ = cpf_completo.replace('.', ' ').replace('-', ' ')
cpf1 = cpf_.split()
cpf  = ''.join(cpf1)
nove_digitos= ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito_1 in nove_digitos:
    
    resultado_digito_1 += int(digito_1) *contador_regressivo_1
    contador_regressivo_1-=1
digito_1=(resultado_digito_1 *10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


"""
    CPF: 746.824.890-70
    Colete asoma dos 9 primeiros dígitos do CPF
    MAis o primeiro digito
    multiplicando cada um dos valores por uma
    contagem regressiva começando de 11
    
    ex: 746.824.980.-70(746824890)
    11 10  9  8  7  6  5  4  3  2  
    7   4  6  8  2  4  8  9  0  7
    77 40 54 64 14 24 40 36 0  14
    
    Somar todos os resultados
    7+ 40+ 54+ 64+ 14+ 24+ 40+ 36+ 0+ 14 = 363
    Multiplicar o resultado anterior por 10
    363 * 10 = 3630
    Obter o restp da divisão da conta anterior por 11
    3630 % 11 = 0
    Se p resultado anterior for maior que 9:
    Resultado é 0
    Contrário disso: 
    resultadoo é o valorr da conta
    
    o primeiro digito do CPF é 0
"""

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2+= int(digito) * contador_regressivo_2
    contador_regressivo_2-=1
digito_2= (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

print(novo_cpf)