import os
import math

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def potencia():
    """Calcula base elevado ao expoente"""
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = base ** expoente
    print(f"\n{base}^{expoente} = {resultado}")

def raiz_quadrada():
    """Calcula a raiz quadrada de um número"""
    num = float(input("Digite um número: "))
    if num < 0:
        print("Erro: Não existe raiz quadrada de número negativo nos reais.")
    else:
        resultado = math.sqrt(num)
        print(f"\nRaiz quadrada de {num} = {resultado:.2f}")

def volume_paralelepipedo():
    """Calcula volume: comprimento x largura x altura"""
    print("\n--- Volume Paralelepípedo ---")
    c = float(input("Digite o comprimento: "))
    l = float(input("Digite a largura: "))
    a = float(input("Digite a altura: "))
    volume = c * l * a
    print(f"\nVolume = {volume:.2f}")

def volume_cilindro():
    """Calcula volume: pi * raio² * altura"""
    print("\n--- Volume Cilindro ---")
    r = float(input("Digite o raio: "))
    h = float(input("Digite a altura: "))
    volume = math.pi * (r ** 2) * h
    print(f"\nVolume = {volume:.2f}")