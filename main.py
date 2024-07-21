from src.musica import Musica
from src.gerenciador import Gerenciador


def main():
    gerenciador = Gerenciador()
    run = True
    while run:
        ans = input("(add | remove | list | q) ")
        match ans.lower():
            case "add":
                nome = input("Qual o nome da música? ")
                cantor = input("Qual o cantor da música? ")
                genero = input("Qual o gênero da música? ")
                musica = Musica(nome, cantor, genero)
                gerenciador.add(musica)
            case "remove":
                if len(gerenciador.musicas) == 0:
                    print("Nâo há músicas para remover.")
                else:
                    gerenciador.remove(input("Qual música deseja remover? "))
            case "list":
                gerenciador.list()
            case "q":
                print("Finalizando programa!")
                run = False
            case default:
                print("Inválido!")


if __name__ == '__main__':
    main()
