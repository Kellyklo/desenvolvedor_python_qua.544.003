import os

from models import Pessoas

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()

    usuario = Pessoa(nome="",cpf="",email="",telefone="")

    usuario.nome =input("informe o nome:").strip().title()
    usuario.cfp =input("informe o CPF:").strip()
    usuario.email =input("informe o email:").strip().lower()
    usuario.telefone =input("informe o telefone:").strip()

    print(f"Nome:{usuario.nome}")
    print(f"CPF:{usuario.cpf}")
    print(f"E-mail:{usuario.email}")
    print(f"Telefone:{usuario.telefone}")


if __name__ == "__main__":
    main()