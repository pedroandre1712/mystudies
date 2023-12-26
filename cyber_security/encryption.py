class Ceaser:
    def __init__(self,word, n):
        self.word = word
        self.n = n
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
    def encryption(self):
        new_Word = ""

        for x in self.word:
            if x not in self.alfabeto:
                new_Word+=x

            if self.alfabeto.find(x)+self.n > len(self.alfabeto):
                new_Word += self.alfabeto[self.alfabeto.find(x)+self.n-len(self.alfabeto)]

            else:
                new_Word += self.alfabeto[self.alfabeto.find(x)+self.n]

        return new_Word
    
    def decryption(self):

        new_Word = ""

        for x in self.word:

            if x not in self.alfabeto:
                new_Word+=x

            if self.alfabeto.find(x)-self.n < 0:
                new_Word += self.alfabeto[self.alfabeto.find(x)-self.n+len(self.alfabeto)]

            else:
                new_Word += self.alfabeto[self.alfabeto.find(x)-self.n]
                
        return new_Word

teste = Ceaser("ZARATRUSTA", 2)
print(teste.encryption())
print(teste.decryption())