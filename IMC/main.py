altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso:"))

imc = peso / (altura ** 2)

print("O seu IMC é:", imc)

if imc < 18.5:
    print("Você está abaixo do peso.")
    
elif 18.5 <= imc < 25:
    print("Você está com o peso normal.")
    
else:
    print("Você está acima do peso.")