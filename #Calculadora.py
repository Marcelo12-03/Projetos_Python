#Calculadora.py

def soma(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b
def main():
    print("Bem-vindo á calculadora!")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == "1":
        resultado = soma(num1, num2)
        print(f"O resultado da soma é: {resultado}")
    elif escolha == "2":
        resultado = subtrair(num1, num2)
        print(f"O resultado da subtração é: {resultado}")
    elif escolha == "3":
        resultado = multiplicar(num1, num2)
        print(f"O resultado da multiplicação é: {resultado}")
    elif escolha == "4":
        resultado = dividir(num1, num2)
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Opção inválida!")