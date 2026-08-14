import modulo as m


def main():
    m.limpar()

    nome = input("informe o nome:").strip().title()
    idade = int(input("informe a idade:"))

    print(f"{nome} {m.maioridade(idade)}")

if __name__ =="__main__":
    main()
