'''
Desafio
Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, que realizar chamadas para outros usuários. Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do usuário, suponha o custo de $0.10 por minuto. Você pode criar um método fazer_chamada que vai permitir que o usuário faça a chamada, ele vai receber o destinatario e duracao como parâmetros. Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar o método deduzir_saldo para deduzir o valor do saldo do plano e depois retorne uma mensagem adequada como mostra no exemplo a baixo.

Entrada
Número do usuário, número do telefone, saldo inicial, número do destinatário e a duração da chamada em minutos.

Saída
Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.
'''

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        self.plano.custo_chamada(duracao)
        if self.plano.saldo < self.plano.custo:
            return "Saldo insuficiente para fazer a chamada."
        self.plano.verificar_saldo(self.plano.saldo)
        return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.saldo:.2f}"

class Plano:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def custo_chamada(self, duracao):
        self.duracao = duracao
        self.custo = self.duracao * 0.10

    def verificar_saldo(self, saldo):
        self.saldo = saldo
        self.saldo -= self.custo

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo):
        super().__init__(nome, numero, Plano(saldo))

nome = input()
numero = input()
saldo = float(input())

usuario_pre_pago = UsuarioPrePago(nome, numero, saldo)
destinatario = input()
duracao = int(input())

print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
