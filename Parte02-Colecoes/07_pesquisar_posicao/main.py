cidades = [
           "Brasília",
           "Rio de Janeiro",
           "Sãp Paulo",
           "Belo Horizonte",
           "Goiânia",
           "Manaus",
           "Fortaleza",
           "Florianópolis"
]

cidade = input("informe o nome da cidade a ser pesquisada: ").strip().title()

# mostra a posição do item na lista
if cidade in cidades:
    indice = cidades.index(cidade)
    print(f"Indice de {cidade} na lista é {indice}.")
else:
    print("Cidade não encontrada.")