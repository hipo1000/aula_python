import os

lista = []

while True:
    print('Selecionar uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ') # Ajudando o usuário com a opção 'l'

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    
    elif opcao == 'a':
        
        indice_str = input('Escolha o índice para apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Não foi possível apagar este índice, pois o valor digitado não é um número válido.')
        except IndexError:
            print('Este índice não existe na lista.')
    
    elif opcao == 'l':
       
        
        # --- Bloco de código corrigido ---
        if len(lista) == 0:
            print('Nada para listar')
        else: # Adicionei um 'else' para manter a lógica clara
            for i, valor in enumerate(lista):
                print(i, valor)
        # ----------------------------------
       
    else:
        print('Por favor, escolha i, a ou l')