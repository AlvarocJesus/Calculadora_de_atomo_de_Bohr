from time import sleep


print("""
----------INTEGRANTES----------
Alvaro Coelho Jesus 22221002-3
""")

def message():
  input("""
  ------------------------------
  Digite ENTER para continuar com os cálculos
  ------------------------------
  """)

while True:
  print()
  option = int(input())

  if option == 0:
    sleep(1000)
    print('Ate a proxima... (^.^)')
    sleep(1000)
  elif option == 1:
    print('A')
    message()
  elif option == 2:
    print('B')
    message()
  elif option == 3:
    print('C')
    message()
  elif option == 4:
    print('D')
    message()