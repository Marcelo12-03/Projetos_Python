nota1 = int (input("Digite a primeira nota: "))
nota2 = int (input("Digite a segunda nota: "))
nota3 = int (input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("O aluno foi aprovado com a média: ", media)

else:
    print("O aluno foi reprovado com a média: ", media)