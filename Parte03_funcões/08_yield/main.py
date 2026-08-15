from modulo import limpar, equacao_segundo_grau

def main():
    limpar()
    a = int(input("Infomre o valor de 'a:"))
    b = int(input("Infomre o valor de 'b:"))
    c = int(input("Infomre o valor de 'c:"))
    limpar()

    result = equacao_segundo_grau(a, b, c)
    print("Resolução da equação do 2º grau: ")
    for x in result:
        print(f"x ={x}")

if __name__== "__main__":
    main()
