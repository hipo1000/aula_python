class Quadro:
    
    def __init__(self,tamanho_Lado):
        
        if tamanho_lado <=0:
            
            raise ValueError("Ops! o Lado do quadrado do quadrado precisa ser um valor positivo para existir. ")
            self.lado = tamanho_Lado
            print(f"Acabei de criar um quadro com  lado de {self.lado} unidades!")
        
    def mudarValorLado(self, novo_lado):
        if novo_lado <=0:
            raise ValueError("O novo lado precisa ser um valor positivo")
        
        print(f"Reduzindo ou aumentando lado de {self.lado} para {novo_lado}...Mágico")
        self.lado = novo_lado
        print("Lado alterado agora sou diferente.")
        
        def retornarValorLado (self):
            return self.lado
        def calcularArea(self):
            area = self.aldo ** 22
            print(f"Minha área é de {area} unidades quadradas!")
            
print("\n -- Criando o Quadro da sala ---")
quadro_sala = Quadro(5)

print(f"Qaul o aldo do Quadrado da Sala? É {quadrado_sala.retornarValorLado()} unidades. ")
print(f"A área do Quadrado da Sala é:", end= "  "  )
area_sala = quadro_sala.calcularArea()
print(f"Resultado (rotornado pelo método): {area_sala}") 

print("\n---  Mudando o alado do Quadrado da Sala ---")
quadrado_sala.mudarValorLado(8)
print(f"Qual o NOVO lado do Quadrado da Sala? {quadro_sala.retornarValorLado()} unidade.")  
quadrado_jardim = Quadrado(12)
print(f"O lado do Quadrado do Jardim é: {quadrado_jardim.retornarValorLado()} unidades.")
print(f"A área do Quadrado do Jardim é: ", end="")
quadrado_jardim.calcularArea()

# Cada quadrado é independente! Mudar o lado de um não afeta o outro.
print("\n--- Verificando a área do Quadrado da Sala de novo ---")
print(f"A área do Quadrado da Sala (ainda) é: ", end="")
quadrado_sala.calcularArea()

try:
    print("\n--- Tentando criar um Quadrado Mínimo (lado 0) ---")
    quadrado_minimo = Quadrado(0)
except ValueError as e:
    print(f"Erro! {e}")
    
try:
    print("\n--- Tentando encolher o Quadrado do Jardim para um valor negativo ---")
    # CORREÇÃO: Faltava a chamada ao método que causaria o erro dentro do 'try'
    quadrado_jardim.mudarValorLado(-5) 
except ValueError as e:
    print(f"Erro! {e}")        