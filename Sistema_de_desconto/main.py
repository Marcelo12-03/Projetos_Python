valor = float(input("Digite o valor da compra: "))

if valor >= 1000:
    desconto = valor * 0.15
    valor_com_desconto = valor - desconto
    print("O valor atual da compra é: R$", valor_com_desconto)
    print("O desconto aplicado é: R$", desconto)

elif valor >= 500:
    desconto = valor * 0.10
    valor_com_desconto = valor - desconto
    print("O valor atual da compra é: R$", valor_com_desconto)
    print("O desconto aplicado é: R$", desconto)

elif valor >= 100:
    desconto = valor * 0.05
    valor_com_desconto = valor - desconto
    print("O valor atual da compra é: R$", valor_com_desconto)
    print("O desconto aplicado é: R$", desconto)

else:
    print("Não há desconto disponível para o valor da compra.")