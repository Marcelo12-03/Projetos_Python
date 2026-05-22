#Mini_Banco.py

saldo = 1000

while True:
   print("\nBem-vindo ao Mini Banco!")

   print("1. Ver saldo")
   print("2. Depositar")
   print("3. Sacar")
   print("4. Sair")
   opcao = input("Escolha uma opção: ")
    
   if opcao == "1":
        print(f"Seu saldo é R${saldo:.2f}")

   elif opcao == "2":
     valor = float(input("Digite o valor a ser depositado: "))
     if valor > 0:
       saldo += valor
       print(f"Deposito deR${valor:.2f} realizado com sucesso!")
     else:
            print("Valor inválido. O depósito deve ser maior que zero.")
       
   elif opcao =="3":
        valor = float(input("digiteo valor a ser sacado: "))
        if valor > 0 and valor <= saldo:
         saldo -= valor
         print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
         print("Valor inválido. O saque deve ser maior que zero e menor ou igual ao saldo.")
   elif opcao == "4":
        print("Obrigado por usar o Mini Banco!")
        break
else:
        print("Opção inválida. Por favor, escolha uma opção válida.")