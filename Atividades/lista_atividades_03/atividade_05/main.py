def fibonacci(n):
    """Função recursiva que retorna o n-ésimo termo de Fibonacci"""
    # Caso base
    if n <= 1:
        return n
    # Caso recursivo
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print("--- Sequência de Fibonacci ---")
    
    num = int(input("Informe um número inteiro: "))
    
    if num < 0:
        print("Por favor, informe um número >= 0")
    else:
        print(f"\nSequência de Fibonacci até o termo {num}:")
        
        for i in range(num + 1):
            print(fibonacci(i), end=" ")
    
    print("\n\nFim do programa.")

if __name__ == "__main__":
    main()