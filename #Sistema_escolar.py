#Sistema_escolar.py


faltas = int(input("DIgite o numero de faltas por bimestre do aluno: "))

if faltas >= 30:
    print("O aluno foi reprovado por faltas")
else:
    print("O aluno nao foi reprovado por faltas")

nota_1 = float(input("Digite a primeira nota do bimestre: "))
nota_2 = float(input("Digite a segunda nota do bimestre: "))
nota_3 = float(input("Digite a terceira nota do bimestre: "))
media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print("O aluno foi aprovado com media: ", media)
elif media >=5 and media < 7:
    print("O aluno esta de recuperacao com media: ", media)
else:
    print("O aluno foi reprovado com media: ", media)

aprovacao = (faltas < 30) and (media >= 7)

if aprovacao:
    print("O aluno foi aprovado")
else:
    print("O aluno foi reprovado")