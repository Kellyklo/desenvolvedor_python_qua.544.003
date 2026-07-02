# declaração de variáveis
nome = input("informe seu nome do aluno:").title()
nota = float(input("informe nota do aluno:").replace(",", "."))

# verifiva se a nota é válida
if nota >= 0 and nota <= 10:
    if nota >= 7: 
        print(f"{nome} está aprovado.")
    elif nota >= 5:
        print(f"{nome} está recuperação.")
    else:
        print(f"{nome} está reprovado.")
else:
    print(f"Nota de {nome} inválida.")
