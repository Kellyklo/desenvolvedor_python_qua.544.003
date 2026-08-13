import json
import os

alunos = []

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Informa dados")
    print("2 - sair do programa")
    opcao = input("Informe a opcao: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            aluno = {}
            notas = [0,0,0]

            aluno['nome'] = input("Informe o nome do aluno: ").strip().title()
            for i in range(len(notas)):
                notas[i] = float(input("informe {i+1}ª nota: ").replace(",","."))
            aluno['notas'] = notas
            aluno['media'] = sum(notas)/len(notas)
            aluno['resultado'] = "aprovado" if aluno['média'] >=7 else "reprovado"
            alunos.append(aluno)
            with open("atividade_03/arquivo.json","w",encoding="utf-8")as f:
                json.dump(alunos, f)
        case "2":
            break
        case _:
           print("Opção invalida.")
           continue 