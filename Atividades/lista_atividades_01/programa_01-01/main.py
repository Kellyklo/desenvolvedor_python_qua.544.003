# declaração de variáveis
nome = input("Digite seu nome: ")
altura = float(input("Informo a sua altura:").replace (",","."))
peso = float(input("Informo seu peso:").replace (",",".")) 
imc = peso / (altura ** 2)

if imc < 16.5: resultado = "abaixo do peso"
elif 16.5 <= imc <25.9: resultado = "peso normal"
elif 26 <= imc <29.9: resultado = "sobrepeso"
elif 30 <= imc <35.9: resultado = "obesidade Grau 1"
elif 36 <= imc <39.9: resultado = "obesidade Grau 2"
elif 40 <= imc <45.9: resultado = "obesidade Grau 3"
else: resultado = "obesidade morbida"

print(f"Seu nome: {nome}")
print(f"Sua altura: {altura} m")
print(f"Sua peso:{peso} kg")
print(f"imc é: {imc:.2f}")
print(f"resultado: {resultado}")