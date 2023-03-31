from bs4 import BeautifulSoup
import requests
import random


def avaliadorDeComentarios():
    status = True
    y = 1
    filmesStr = []

    url = "https://www.adorocinema.com/filmes-todos/"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')

    filmes = doc.findAll('h2', attrs={'class': "meta-title"})

    print("Filmes mais populares atualmente:")
    for i in filmes:
        filme = i.find('a', attrs={'class': "meta-title-link"})
        formatacao = f"{y}º: {filme.string}"
        y += 1
        filmesStr.append(filme.string)
        print(formatacao)

    while status:
        aleatorio = round(random.randint(0, len(filmesStr) - 1))
        pergunta = input("\nGostaria que escolhessemos um para você assistir? (S/n) ")
        if pergunta == "S" or pergunta == "s":
            print(f"\n{filmesStr[aleatorio]}")
            print("Aprecie o filme, espero que goste da escolha.")
            status = False
        elif pergunta == "N" or pergunta == "n":
            print("\nAprecie um filme de sua escolha")
            status = False
        else:
            print("\nTem certeza que escolheu uma alternativa válida? (S/N)")


avaliadorDeComentarios()
