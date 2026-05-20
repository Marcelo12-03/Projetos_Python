usuario_correto = input("Digite o seu usuario: ")
senha_correta = input("Digite sua senha: ")

cpf = input("Digite seu CPF: ")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ano_atual = int(input("Digite o ano atual: "))

print("\n=== LOGIN ===")

usuario = input("Digite o seu nome de usuario: ")
senha = input("Digite sua senha: ")

ano_nacimento = ano_atual - idade

if usuario_correto == usuario and senha_correta == senha:

    print("=== acesso liberado ===")
    print(f"Bem-vindo(a), {nome}!")

    print(f"Portador do CPF: {cpf}")
    print(f"Seu ano de nacimanento é: {ano_nacimento}")

else:
    print("=== acesso negado ===")
    print("O usuario ou senha esta incorreto.")
