class Caesar:
    def __init__(self,word, n):
        self.word = word
        self.n = n
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUWXYZ"

    def encryption(self):
        new_Word = ""

        for x in self.word:

            # Teste para caracteres que nao pertencem ao alfabeto
            if x not in self.alfabeto:
                new_Word+=x

            # Teste para índices maiores do tamanho do alfabeto 
            if self.alfabeto.find(x)+self.n > len(self.alfabeto):
                new_Word += self.alfabeto[self.alfabeto.find(x)+self.n-len(self.alfabeto)]

            #
            else:
                new_Word += self.alfabeto[self.alfabeto.find(x)+self.n]

        return new_Word
    
    def decryption(self):

        new_Word = ""

        for x in self.word:

            # Teste para caracteres que nao pertencem ao alfabeto
            if x not in self.alfabeto:
                new_Word+=x

            # Teste para índices menores que 0 
            if self.alfabeto.find(x)-self.n < 0:
                new_Word += self.alfabeto[self.alfabeto.find(x)-self.n+len(self.alfabeto)]

            else:
                new_Word += self.alfabeto[self.alfabeto.find(x)-self.n]

        return new_Word

teste = Caesar("ZARATRUSTA", 2)
print(teste.encryption())
print(teste.decryption())