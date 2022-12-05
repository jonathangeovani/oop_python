class Pessoa():
    def __init__(self):
        self.nome = 'João'
        self.idade = 25
        self.profissao = 'software engineer'
    def apresenta(self):
        print('Meu nome é ' + self.nome + ', tenho ' + str(self.idade) + ' anos de idade e trabalho como ' + self.profissao + '.')

pessoa = Pessoa()
print(pessoa.nome)
print(pessoa.idade)
print(pessoa.profissao)
pessoa.apresenta()