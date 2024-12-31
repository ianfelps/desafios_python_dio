'''
Descrição
O objetivo desse desafio é identificar e corrigir erros em um programa que verifica se duas palavras são anagramas. Anagramas são palavras que contêm as mesmas letras, mas em uma ordem diferente. O programa precisa exibir Verdadeiro se as palavras forem anagramas e Falso caso contrário. No entanto, o programa contém alguns erros de lógica e sintaxe que precisam ser corrigidos.
Uma opção para te ajudar durante o processo de depuração é o uso do GitHub Copilot, que pode sugerir correções de código.

Entrada
A entrada consistirá de duas palavras (A e B), fornecidas em uma única linha, separadas por um espaço. Por exemplo: ouvir virou.

Saída
O programa deve retornar uma mensagem indicando se as palavras são anagramas ou não:
- Verdadeiro (se as palavras forem anagramas).
- Falso (se as palavras não forem anagramas).
'''

def verificar_anagrama(palavra1, palavra2):
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    return sorted(palavra1) == sorted(palavra2)

def main():
    entrada = input().strip()

    palavras = entrada.split()
    
    palavra_a, palavra_b = palavras[0], palavras[1]

    if verificar_anagrama(palavra_a, palavra_b):
        print("Verdadeiro")
    else:
        print("Falso")

if __name__ == "__main__":
    main()