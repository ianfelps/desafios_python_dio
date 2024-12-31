'''
Descrição
Você está desenvolvendo uma calculadora de moda e se deparou com alguns erros no código. Seu objetivo é corrigir os problemas para que a calculadora funcione corretamente. No código original, há erros de lógica e de sintaxe que impedem de calcular a moda corretamente.
Uma opção para te ajudar durante o processo de depuração é o uso do GitHub Copilot, que pode sugerir correções de código.

Entrada
A entrada deve receber uma sequência de números inteiros separados por espaço. O programa deve ser capaz de processar esses números e contar quantas vezes cada valor aparece.

Saída
A saída deverá retornar o número que aparece com maior frequência (a moda).
'''

def calcular_moda(lista):
    frequencias = {}
    for num in lista:
        if num in frequencias:
            frequencias[num] += 1
        else:
            frequencias[num] = 1
    
    maior_frequencia = max(frequencias.values())
    modas = [num for num, freq in frequencias.items() if freq == maior_frequencia]
    
    return modas

entrada = input()
dados = list(map(int, entrada.split()))

modas = calcular_moda(dados)

if len(modas) > 1:
    print(" ".join(map(str, modas)))
else:
    print(modas[0])