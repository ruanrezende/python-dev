print("Bem-Vindo a Sorveteria do Ruan Rezende")
print("----------------------------------------------Cardápio---------------------------------------------")
print("| Código  | Descrição            | Tamanho P (500ml)  | Tamanho M (1000ml)  | Tamanho G (1000ml)  |")
print("|   TR    | Sabores Tradicionais |       R$ 6,00      |       R$ 10,00      |      R$ 18,00       |")
print("|   ES    | Sabores Especiais    |       R$ 7,00      |       R$ 12,00      |      R$ 21,00       |")
print("|   PR    | Sabores Premium      |       R$ 8,00      |       R$ 14,00      |      R$ 24,00       |")
print("---------------------------------------------------------------------------------------------------")

tamanho = ["P", "M", "G"]
codigos = {"TR": [6.00, 10.00, 18.00],

          "ES": [7.00, 12.00, 21.00],

          "PR": [8.00, 14.00, 24.00]}
compra = []

while True:

  tamanhoEscolhido = input("Insira o TAMANHO do pote desejado (P/M/G): ")
  saborEscolhido = input("Insira o CÓDIGO do sabor desejado (TR/ES/PR): ")

  if tamanhoEscolhido in tamanho and saborEscolhido in codigos:
    pedido = codigos[saborEscolhido][tamanho.index(tamanhoEscolhido)]
    compra.append(pedido)

    print("Pedido adicionado!")
    algo_mais = input ("Deseja pedir algo mais?"
                          "\nDigite S para sim ou N para não. ")

    if algo_mais == "S":
      continue
    else:
      break

  else:
    print("!!!!!  TAMANHO ou CÓDIGO INVÁLIDO(S) !!!!!")
    continue

print ("Valor total a ser pago é:", "R$",sum(compra))