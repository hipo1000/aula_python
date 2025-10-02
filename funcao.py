"""Exercício com Funções

Crie uma função que multiplica todos os argumentos

Não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crir uma função fala se um número par ou ímpar
Rerne se o npumero é par ou ímpar

"""


def multiply(*args):
    
    result=1
    
    for number in args:
    
        result*=number
        
    return result

print(multiply(2,3,4))

def par_impar(number):  
    
    if number % 2== 0:
        print('Number is pair')
    else: 
        print('Number odd')
    return number
    
print(par_impar(2))
print(par_impar(3))