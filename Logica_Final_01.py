#Desvendando o Código Secreto da Polkadot
 #1. Dado um intervalo de números inteiros, você deverá percorrer todos os números desse intervalo.
 #2. Se um número for múltiplo de 3, ele deverá ser somado ao total.
 #3. Se um número for múltiplo de 5, ele deverá ser subtraído do total.
 #4. Se um número for múltiplo de 3 e 5 ao mesmo tempo, ele deverá ser ignorado.
 #5. No final, o programa deverá exibir o valor total calculado, representando a segurança do fundo em DOT.

 #Criação e Dicas:
 #• Comece pedindo ao usuário dois números inteiros que definirão o intervalo.
 #• Utilize um laço de repetição for para percorrer os números do intervalo e aplicar as regras do desafio.
 #• Lembre-se de usar condicionais if, elif, e else para verificar as condições de múltiplos de 3, 5, e 3 e 5 juntos.
 #• Teste seu código com diferentes intervalos para garantir que ele funcione corretamente em todos os casos.
 #• Após concluir o desafio, poste o notebook no GitHub e inclua uma explicação no README.md sobre como seu código funciona.

def solicita_numero():
    while True:
        try:
            if numero_01 is None:
                numero = int(input("Insira o primeiro número: "))
            else:
                numero = int(input("Insira o segundo número: "))  
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def eh_multiplo(base, x):
    return x % base == 0

def percorrer_numeros(inicio, fim):
    total = 0    
    for i in range(inicio, fim +1):
        if eh_multiplo(3, i) and eh_multiplo(5, i):
            continue
        elif eh_multiplo(3, i):
            total += i
        elif eh_multiplo(5, i):
            total -= i
    return total

def intervalo_valido(inicio, fim):
  if (inicio <= fim):
    return True
  else:
    return False

def buscaCodigoSecretoPolkadot():
  codigoSecretoPolkadot = None
  numero_01 = None
  numero_02 = None
  numero_01 = solicita_numero()
  numero_02 = solicita_numero()
  intervalo = intervalo_valido(numero_01, numero_02)
  if intervalo :
    codigoSecretoPolkadot = percorrer_numeros(numero_01,numero_02 )

  if codigoSecretoPolkadot is not None:
    print(f"O Código Secreto da Polkadot é: {codigoSecretoPolkadot}")
  else:
    print("O Código Secreto da Polkadot não foi possível ser encontrado.")


buscaCodigoSecretoPolkadot()