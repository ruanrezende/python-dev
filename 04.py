listafuncionarios = []

def cadastrarfuncionario(codigo):

 print('Você selecionou a opção de Cadastrar funcionario')

 print('O código da funcionario é: {:0>3}'.format(codigo))

 nome = input('Entre com o nome da funcionario:')

 setor = input('Entre com o setor da funcionario:')

 salario = float(input('Entre com o salario R$ da funcionario:'))

 dicionariofuncionarios = {'codigo'   : codigo,

                        'nome' : nome,

                        'setor': setor,

                        'salario': salario}

 listafuncionarios.append(dicionariofuncionarios.copy())

def consultarfuncionario():

 while True:

   try:

     print('Você Selecionou a Opção de Consultar funcionarios')
     opConsultar = int(input('Entre com a opção desejada\n1- Consultar Todas as funcionarios\n2- Consultar funcionarios por Código\n3- Consultar funcionarios por setor\n4- Retornar\n-->'))

     if opConsultar == 1:
       print('-' * 20)

       for funcionarios in listafuncionarios:

           for key, value in funcionarios.items():

             print('{} : {}'.format(key,value))

           print('-' * 20)

     elif opConsultar == 2:

       print('Você Selecionou a Opção funcionarios por Código')

       entrada = int(input('Digite o Código: '))

       print('-' * 20)

       for funcionarios in listafuncionarios:

         if(funcionarios['codigo'] == entrada):

           for key, value in funcionarios.items():

             print('{} : {}'.format(key,value))

           print('-' * 20)

     elif opConsultar == 3:

       print('Você Selecionou a Opção funcionarios por setor')

       entrada = input('Digite o setor: ')

       print('-' * 20)

       for funcionarios in listafuncionarios:

         if(funcionarios['setor'] == entrada):

           for key, value in funcionarios.items():

             print('{} : {}'.format(key,value))

           print('-' * 20)

     elif opConsultar == 4:
       break

     else:
       print('Por favor digite somente o que pede')
       continue

   except ValueError:
     print('Por Favor pare de digitar números que não existe...')
     continue

def removerfuncionario():
   print('Você Selecionou o Remover funcionario')
   entrada = int(input('Digite o Código da funcionario que irá remover: '))

   for funcionarios in listafuncionarios:

     if(funcionarios['codigo'] == entrada):
       listafuncionarios.remove(funcionarios)

   else:

     print('Você removeu o código.')

print('Bem-vindo ao Controle de Funcionários do (coloque seu nome aqui')
registrofuncionarios = 0

while True:

   try:
     opcao = int(input('Digite a opção desejada:\n1- Cadastrar funcionarios\n2- Consultar funcionarios\n3- Remover funcionarios\n4- Sair\n-->'))

     if opcao == 1:
       registrofuncionarios = registrofuncionarios + 1
       cadastrarfuncionario(registrofuncionarios)

     elif opcao == 2:
       consultarfuncionario()

     elif opcao == 3:
       removerfuncionario()

     elif opcao == 4:
       print('Programa finalizado')

       break

     else:
       print('Digite somente uma das opções do MENU')

       continue

   except ValueError:
       print('Pare de digitar números que não existe...')