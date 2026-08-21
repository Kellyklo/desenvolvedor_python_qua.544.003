import os

from models import PessoaFisica,PessoaJuridica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="",endereco="")
    empresa = PessoaJuridica(razao_social="",nome_fantasia="",cnpj="",email="",telefone="",endereco="")

    limpar()

    # informa os valores do usuário
    usuario.nome = input("Informe o nome do usuário:").strip().title()
    usuario.cpf = input("Informe o CPF").strip()
    usuario.email = input("Informe o e-mail do usuário:").strip().lower()
    usuario.telefone = input("Informe o telefone do usuário:").strip()
    usuario.endereco = input("Informe o endereço do usuário:")

    limpar()

    # informar os valores da empresa
    empresa.razao_social = input("Informe o nome juridico da empresa: ").strip()
    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereco da empresa: ")

    #saida de dados
    usuario.exibir_dados()
    empresa.exibir_dados()


if __name__ == "__main__":
    main()
