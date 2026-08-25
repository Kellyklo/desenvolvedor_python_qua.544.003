import os

from models import PessoaFisica, PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica(nome=**,cpf==**,email=**,telefone=**)
    empresa = PessoaJuridica(nome_fantasia=**,cnpj==**,email=**,telefone=**)

    limpar()

    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o cpf do usuário: ").strip()
    usuario.email = input("Informe o e-mail do usuário: ").strip().lower
    usuario.telefone = input("Informe o telefone do usuário: ").strip()

    print("Nome do usuarios:{usuario.nome}")
    print("CPF do usuarios:{usuario.cpf}")
    print("E-mail do usuarios:{usuario.email}")
    print("Telefone do usuarios: {usuario.telefone}")

    print("Nome do empresa: {empresa.nome_fantasia}")
    print("CNPJ do usuarios:{empresa.cnpj}")
    print("E-mail do usuarios:{empresa.email}")
    print("Telefone do usuarios:{empresa.telefone}")

    
    limpar()

    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
    usuario.cnpj = input("Informe o cnpj da empresa: ").strip()
    usuario.email = input("Informe o e-mail da empresa: ").strip().lower
    usuario.telefone = input("Informe o telefone da empresa: ").strip()
    
    limpar()
if __name__ == "__mai__":
    main()