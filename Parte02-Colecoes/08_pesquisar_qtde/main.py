Paises = [
           "Brasil",
           "Estados Unidos",
           "México",
           "Argentina",
           "Brasil",
           "Argentina",
           "Fortaleza",
           "Arábia Sauditas",
           "Irã",
           "Brasil",
           "México",
           "Estados Unidos",
           "Brasil"
]

Pais = input("informe o nome da País a ser pesquisada: ").strip().title()

# aramazena a quantidade de ocorrências na lista
qtde = Paises.count(Pais)

print(f"{Pais} foi encontrado {qtde} vezes na lista.")