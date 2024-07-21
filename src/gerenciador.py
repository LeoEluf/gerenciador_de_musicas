class Gerenciador():
    def __init__(self):
        self.musicas = []

    def add(self, musica):
        self.musicas.append(musica)
        print(f"Música {musica.nome} adicionada com sucesso!")

    def remove(self, nome):
        for musica in self.musicas:
            if musica.nome == nome:
                self.musicas.remove(musica)
                return print(f"Música {musica.nome} removida com sucesso!")

        print("Música não encontrada!")

    def list(self):
        if len(self.musicas) < 1:
            return print("Não há músicas disponíveis!")

        print("Lista de músicas disponíveis:")
        print(f"{'Nome'.center(10)} | {'Cantor'.center(10)} | {'Gênero'.center(10)}")
        for musica in self.musicas:
            print(musica)
