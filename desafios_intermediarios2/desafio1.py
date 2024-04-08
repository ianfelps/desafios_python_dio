'''
Desafio
Você foi contratado pela empresa DIO Robots para programar um robô capaz de classificar números em uma das seguintes categorias: negativo, positivo ou zero. Para isso, você deve criar uma função de classificação que receba um número como parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

O programa deve ser executado continuamente, permitindo que o usuário insira vários números. Quando ele quiser encerrar a execução, deverá digitar um número igual a zero. A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente. Ao final da execução, o programa deverá exibir a quantidade de números positivos, negativos e zeros que foram inseridos.

Entrada:
A entrada deve receber valores inteiros.
- numero: valor inteiro que pode ser positivo, negativo ou zero. Lembrando que a entrada zero deve encerrar o programa.

Saída:
O código deverá retornar uma mensagem (string) informando se o número é positivo ou não. Ao receber o valor 0, ele deverá encerrar o e informar quantos números foram positivos e negativos.
'''

def classificar_numero():
    p = 0
    n = 0

    while True:
        numero = int(input())
        if numero > 0:
            print('positivo!')
            p += 1
        elif numero < 0:
            print('negativo!')
            n += 1
        elif numero == 0:
            print(f'{p} numeros positivos, {n} numeros negativos.')
            break

if __name__ == "__main__":
    classificar_numero()