#desafio calculadora lower()"muda os caracteres ma minusculo"startswith(s)"Verifica se o que vc está preenchendo é uma stringEm resumo, o pass é como um "faça nada" que preenche um espaço onde a sintaxe do Python exige um comando, mas onde você não quer ou não pode adicionar um código real ainda."

while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    
    # 1. Variável de validação de números
    # É melhor inicializar como False, e só mudar para True se a conversão der certo.
    numeros_validos = False
    
    try:
        num_1_float = float(numero1)
        # 2. Corrigido: a variável para o segundo número estava com o mesmo nome do primeiro.
        num_2_float = float(numero2)
        numeros_validos = True
    # 3. Tratamento de erro mais específico (ValueError)
    except ValueError:
        # A variável já é False, então não precisamos fazer nada aqui.
        pass
    
    # 4. A verificação 'is None' não é a ideal. Usamos 'not' para verificar se a validação falhou.
    if not numeros_validos:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    # Adicionamos a lógica que faltava para a calculadora
    resultado = 0.0
    if operador == '+':
        resultado = num_1_float + num_2_float
    elif operador == '-':
        resultado = num_1_float - num_2_float
    elif operador == '*':
        resultado = num_1_float * num_2_float
    elif operador == '/':
        # 5. Adicionamos a validação de divisão por zero.
        if num_2_float == 0:
            print('Não é possível dividir por zero.')
            continue
        resultado = num_1_float / num_2_float
    
    print(f'O resultado é: {resultado}')
    
    # 6. Corrigido: 'startswith' precisa de uma string para comparar (ex: 's').
    # A linha duplicada no final também foi removida.
    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    
    # 7. A condição 'if sair:' é suficiente, pois a variável já é True ou False.
    if sair:
        break