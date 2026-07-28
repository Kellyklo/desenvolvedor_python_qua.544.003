#Programa Bilheteria de Cinema
name = input("digite seu nome: ")
idade = int(input("Informe a idade: "))
# Lista de Filmes
filmes = {1: {"name": "A volta dos que não foram", "idade": 0}, 2: {"name": "A roda quadrada", "idade": 12}, 3: {"name": "As tranças do reo careca", "idade": 14}, 4: {"name": "Poeira em alto mar", "idade": 16}, 5: {"name": "A vingança do frango assado", "idade": 18}}

# mostrar os filmes em cartaz
while true:
    print("\name filmes em cartaz")
    for num, info in filmes.itens(): classificacao = "livre" if info["idade"] == 0 else f"{info["idade"]} anos"
    print(f"{num} - {info["name"]} ({classificacao})")

#usuario escolhe a sala/filme
try: escolha = int(input("\n digite o número do filme que deseja assistir:"))
except ValueError:
    print("opção invalida! digite apenas o número.")
continue

#Verificar se o filme Existe
if escolha not in filmes:
    print("filme inválido! escolha um número da lista.")
continue

Filme_escolhido = filmes[escolha]

#Verificar idade mínima
if idade >= filme_escolhido["idade"]:
    print(f"\nEntrada permitida! Bom filme: {filme_escolhido["name"]}")

#Gravar bilhete em arquivo e encerrar
    whith open("bilhete.txt, "w", encoding="utf-8") as arquivo:
    Bilhete.write("bilhete\n")
    name.write(f"name:{name}\n")
    idade.write(f"idade:{idade} anos\n")
    Filme.write(f"filme: {filme_escolhido["nome"]}\n")
    Classificacao.write(f"classificação: {filme_escolhido["idade"]} anos\n")
    print("bilhete gravado em "bilhete.txt. Aproveite o  filme!")
break
          
#Encerra o programa
else:
print(f"\nEntrada Negada! Você precisa ter no mínimo {filme_escolhido["idade"]} anos para assistir "{filme_escolhido["name"]}".")
print("escolha outro filme.")