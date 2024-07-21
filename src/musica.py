class Musica():
    def __init__(self, nome, cantor, genero):
        self.nome = nome
        self.cantor = cantor
        self.genero = genero

    def __str__(self):
        return f"{self.nome.ljust(10)} | {self.cantor.ljust(10)} | {self.genero}"