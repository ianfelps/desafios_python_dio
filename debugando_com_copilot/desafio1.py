'''
Descrição
Você recebeu um código que faz a conversão de datas do formato "yyyy-mm-dd" para o formato "dd/mm/yyyy", mas ele contém erros de lógica e sintaxe. O objetivo desse desafio é debugar o código do template e corrigir o problema, fazendo com que ele converta corretamente datas do formato "yyyy-mm-dd" para o formato "dd/mm/yyyy".
Uma opção para te ajudar durante o processo de depuração é o uso do GitHub Copilot, que pode sugerir correções de código.

Entrada
A entrada será uma string representando uma data no formato "yyyy-mm-dd" (exemplo: 2024-12-25).

Saída
Deverá retornar a data convertida para o formato "dd/mm/yyyy". Se a entrada não estiver no formato correto, deve ser retornada a mensagem "Formato de data inválido."
'''

data_input = input()

def converter_para_dia_mes_ano(data_str):
    ano, mes, dia = data_str.split("-")
    return f"{dia}/{mes}/{ano}"  

if "-" in data_input:
    print(converter_para_dia_mes_ano(data_input))
else:
    print("Formato de data inválido")