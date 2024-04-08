'''
Desafio
Você está trabalhando para uma empresa que utiliza extensivamente os serviços da AWS, e após algumas análises a equipe de segurança identificou que algumas senhas dos usuários no IAM são fracas e podem representar um risco à segurança dos dados da empresa. Para resolver esse problema, foi solicitado que você desenvolva um programa capaz de analisar as senhas dos usuários e fornecer uma validação de força com base em critérios predefinidos.

Requisitos de segurança para a senha:
- A senha deve ter no mínimo 8 caracteres.
- A senha deve conter pelo menos uma letra maiúscula (A-Z).
- A senha deve conter pelo menos uma letra minúscula (a-z).
- A senha deve conter pelo menos um número (0-9).
- A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.

Entrada
A entrada será uma única string representando a senha que precisa ser validada.

Saída
Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos de segurança ou não, juntamente com um feedback explicativo sobre os critérios considerados.
'''

def verificar_forca_senha(senha):

    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

    # Verificando se tem pelo menos uma letra maiuscula
    for letra in senha:
        if letra.isupper():
            tem_letra_maiuscula = True
            break

    # Verificando se tem pelo menos uma letra minuscula
    for letra in senha:
        if letra.islower():
            tem_letra_minuscula = True
            break

    # Verificando se tem pelo menos um número
    for letra in senha:
        if letra.isdigit():
            tem_numero = True
            break

    # Verificando se tem pelo menos um caractere especial
    for letra in senha:
        if not letra.isalnum():
            tem_caractere_especial = True
            break

    # Retornando o resultado
    if tem_letra_maiuscula and tem_letra_minuscula and tem_caractere_especial and tem_numero:
        return "Sua senha atende aos requisitos de seguranca. Parabens!"
    else:
        return "Sua senha nao atende aos requisitos de seguranca."

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)