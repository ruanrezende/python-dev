def metragem_limpeza():

   print('-'*20, 'MENU 1 de 3 - Metragem da Limpeza','-'*20)

   while True:

       try:

           metragemL = int(input('Insira a metragem da casa: '))

           if (metragemL >= 30) and (metragemL <= 300):

               return 60 + 0.3 * metragemL

           elif (metragemL >= 300) and (metragemL <= 700):

               return 120 + 0.5 * metragemL

           else:

               print('Não aceitamos casas com metragem menor que 30m² ou maior que 700m²!!!')
               continue

       except ValueError:

           print('!'*20, 'Valores não inteiros não são aceitos','!'*20)


def tipo_limpeza():

   print('-'*20, 'MENU 2 de 3 - Tipo de Limpeza', '-'*20)

   while True:

       tipoL = input('Escolha qual o tipo de limpeza: \n'+

                     'B – Básica - Indicada para sujeiras semanais ou quinzenais \n' +

                     'C – Completa - Indicada para sujeiras antigas e/ou não rotineiras \n' +

                     'Insira a opção desejada: ')

       tipoL = tipoL.lower()
       tipoL = tipoL.strip()

       if tipoL == 'b':

           return 1.00

       elif tipoL == 'c':

           return 1.30

       else:

           print('!'*30 , 'Opção inválida', '!'*30)
           continue


def adicional_limpeza():

   print('-'*20, 'MENU 3 de 3 - Adicional de Limpeza', '-'*20)

   acumulador = 0

   while True:

       adicinalL = input('Deseja mais algum adicional? \n' +

                         '0 - Não desejo mais nada (Encerrar) \n' +

                         '1 - Passar 10 peças de roupa - R$ 10.00 \n' +

                         '2 - Limpeza de um forno/micro-ondas - R$ 12.00 \n' +

                         '3 - Limpeza de uma geladeira/freezer - R$ 20.00 \n' +

                         'Insira a opção desejada: ')


       if adicinalL == '0':
           return acumulador

       elif adicinalL == '1':
           acumulador = acumulador + 10
           continue

       elif adicinalL == '2':
           acumulador = acumulador + 12
           continue

       elif adicinalL == '3':
           acumulador = acumulador + 20
           continue

       else:
           print('!'*30,'Opção inválida', '!'*30)


def borda(s1):

   tam = len(s1)

   if tam:

       print('+','-' * tam, '+')

       print('|', s1, '|')

       print('+','-' * tam, '+')


borda('          Bem-vindo ao Programa de Serviços de Limpezas do Ruan Rezende          ')

print('*'*100)


metragem = metragem_limpeza()

print(metragem)


tipo = tipo_limpeza()

print(tipo)


adicinal = adicional_limpeza()

print(adicinal)


total = (metragem * tipo) + adicinal


print('Valor total ficou: R$ {:.2f} (Metragem: R$ {:.2f} + Tipo de Limpeza R$ {:.2f} + Adicional R$ {:.2f})' .format(total, metragem, tipo, adicinal))


borda('Obrigado pela preferência!')