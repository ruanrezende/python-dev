print("Bem vindo a Loja do Ruan Rezende")
valorProduto = float(input("Entre com o valor do produto: "))
quantProduto = int(input("Entre com o valor da quantidade: "))
if(quantProduto >= 0 and quantProduto < 11):
    valorTotal = valorProduto * quantProduto
    frete = 30.00;
    valorComFrete = valorTotal + frete
    print(f"O valor sem frete foi: R$ {valorTotal}")
    print(f"O valor com frete foi: R$ {valorComFrete} (frete de R$ {frete})")
elif(quantProduto >= 11 and quantProduto < 101):
    valorTotal = valorProduto * quantProduto
    frete = 60.00;
    valorComFrete = valorTotal + frete
    print(f"O valor sem frete foi: R$ {valorTotal}")
    print(f"O valor com frete foi: R$ {valorComFrete} (frete de R$ {frete})")
elif(quantProduto >= 101 and quantProduto < 1001):
    valorTotal = valorProduto * quantProduto
    frete = 120.00;
    valorComFrete = valorTotal + frete
    print(f"O valor sem frete foi: R$ {valorTotal}")
    print(f"O valor com frete foi: R$ {valorComFrete} (frete de R$ {frete})")
else:
    valorTotal = valorProduto * quantProduto
    frete = 240.00;
    valorComFrete = valorTotal + frete
    print(f"O valor sem frete foi: R$ {valorTotal}")
    print(f"O valor com frete foi: R$ {valorComFrete} (frete de R$ {frete})")