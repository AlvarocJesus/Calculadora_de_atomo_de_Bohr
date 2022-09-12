from time import sleep

# Exibe integrantes dos grupos
print("""
----------INTEGRANTES----------
Alvaro Coelho Jesus 22221002-3
""")

# Exibe descriçao do projeto
print('')

def message():
  input("""
------------------------------
Digite ENTER para continuar com os cálculos
------------------------------
""")

def quanticNumber(n):
  print(f'Numero quantico: {n}')

while True:
  print("\n-----------------Menu-----------------")
  print("""Indique a sua entrada:
1 - Numero quântico
2 - Numero quântico inicial e numero quântico final
3 - Numero quântico e frequência ou comprimento de onda do fóton absorvido
4 - Numero quântico e frequência ou comprimento de onda do fóton emitido

0 - Sair
  """)
  option = int(input())

  if option == 0:
    sleep(1)
    print('Ate a proxima... (^.^) 👉️👈️')
    sleep(1)
    break
  elif option == 1:
    n = int(input('Digite o valor do numero quântico: '))
    quanticNumber(n)
    message()
  elif option == 2:
    n = int(input('Digite o valor do numero quântico: '))
    quanticNumber(n)
    message()
  elif option == 3:
    n = int(input('Digite o valor do numero quântico: '))
    quanticNumber(n)
    message()
  elif option == 4:
    n = int(input('Digite o valor do numero quântico: '))
    quanticNumber(n)
    message()