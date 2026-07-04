# importação de biblioteca
import math

# tratamento de exceção
try:
   while True:
       # usuário informa valor do raio
       r = float(input("Informe o valor do raio em m²: ").
       replace(",","."))

       #calcula a área do cirulo
       area = math.pi*r**2

       # imprime na tela a área do circulo
       print(f"área do círculo: {area:.2f} m².")

       # usuário informa se deseja continuar ou não
       print("1 - calcular área de outro círculo")
       print("2 - saoe do programa")

       opcao = input("Informe sua opção: ").strip()

       match opcao:
           
           case "1":
                contiue
           case "2":
               break
           case _:
               print("Opção inválida.")
               continue
except Exception as e:
    print(f"Não foi possível calcular. {e}.")
