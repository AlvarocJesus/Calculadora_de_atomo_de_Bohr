# Estamos utilizando o sistema internacional de medidas

# Constantes:
from math import sqrt
from time import sleep


h = 4.136e-15  # Constante de planck (eV)
c = 3e8  # Velocidade da luz (m/s)
el = 8.854e-12  # Constante dielétrica (C^2/(N*(m^2)))
e = -1.602e-19  # Carga do elétron (C)
mE = 9.11e-31  # Massa do elétron (Kg)

# Exibe integrantes dos grupos
print("""
----------INTEGRANTES----------
Alvaro Coelho Jesus 22.221.002-3
Fernando Shiraishi 22.221.014-8
Vinicius Alves Pedro 22.221.036-1
""")

# Exibe descrição do projeto:
print('')


def message():
  input("""
------------------------------
Digite ENTER para continuar com os cálculos
------------------------------
""")


def propriedadesAtomo(n):
  r = (n**2)*(5.29e-11)  # raio da órbita de ordem n
  v = (1/el)*((e**2)/(2*n*h))  # velocidade orbital
  k = 13.6/(n**2)  # energia cinética
  u = -27.2/(n**2)  # energia potencial
  energia = -13.6/(n**2)  # energia total
  comprimento = h/(v*mE)  # comprimento de onda de uma partícula

  print(f'Raio: {r:.3}\nVelocidade: {v:.3}\nComprimento de onda: {comprimento:.3}\nEnergia Cinética: {k:.3}\nEnergia Potencial: {u:.3}\nEnergia Total: {energia:.3}')


def emiteAbsorveAtomo(ni, nf):
  energiaFoton = (-13.6/((nf**2)))-(-13.6/(ni**2))
  freq = energiaFoton / h
  comprimentoF = c/freq

  print(
    f'Energia do Fotón: {energiaFoton:.3}\nComprimento de onda do fóton: {comprimentoF:.3}\nFrequência: {freq:.3}')


def absorveAtomo(i, n, j, fc):
  if (i == 1):
    # Conta para n inicial
    if (j == 1):
      # Conta para frequência
      energiaFoton = h * fc
      energiaFinal = (-13.6/(n**2)) + energiaFoton
      divisao = (13.6/abs(energiaFinal))
      nf = sqrt(divisao)
      print(f'Numero quântico final: {nf:.3}')
    else:
      # Conta para comprimento de onda
      energiaFoton = (h*c)/fc
      energiaFinal = (-13.6/(n**2)) + energiaFoton
      nf = sqrt(13.6/abs(energiaFinal))
      print(f'Numero quântico final: {nf:.3}')
  else:
    # Conta para n final
    if (j == 1):
      # Conta para frequência
      energiaFoton = h * fc
      energiaFinal = (-13.6/(n**2)) - energiaFoton
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'Numero quântico inicial: {nf:.3}')
    else:
      # Conta para comprimento de onda
      energiaFoton = (h*c)/fc
      energiaFinal = (-13.6/(n**2)) - energiaFoton
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'Numero quântico inicial: {nf:.3}')

def emiteAtomo(i, n, j, fc):
  if (i == 1):
    # Conta para n inicial
    if (j == 1):
      # Conta para frequencia
      energia = h * fc
      print(f'Numero quântico inicial: {energia}')
      energiaFinal = (-13.6/(n**2)) + energia
      print(f'Numero quântico inicial: {energiaFinal}')
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'Numero quântico final: {nf:.3}')
    else:
      # Conta para comprimento de onda
      energia = (h*c)/fc
      energiaFinal = (-13.6/(n**2)) - energia
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'Numero quântico final: {nf:.3}')
  else:
    # Conta para n final
    if (j == 1):
      # Conta para frequencia
      energia = h * fc
      print(f'Numero quântico inicial: {energia}')
      energiaFinal = (-13.6/(n**2)) - energia
      print(f'Numero quântico inicial: {energiaFinal}')
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'Numero quântico inicial: {nf:.3}')
    else:
      # Conta para comprimento de onda
      energia = (h*c)/fc
      print(f'Numero quântico inicial: {energia}')
      energiaFinal = (-13.6/(n**2)) + energia
      print(f'Numero quântico inicial: {energiaFinal}')
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'Numero quântico inicial: {nf:.3}')

while True:
  print("\n-----------------Menu-----------------")
  print("""Indique a sua entrada:
1 - Propriedades do átomo de Hidrogênio
2 - Emissão/Absorção de fóton pelo Hidrogênio
3 - Absorção de fóton pelo Hidrogênio
4 - Emissão de fóton pelo Hidrogênio
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
    propriedadesAtomo(n)
    message()
  elif option == 2:
    ni = int(input('Digite o valor do numero quântico inicial: '))
    nf = int(input('Digite o valor do numero quântico final: '))
    emiteAbsorveAtomo(ni, nf)
    message()
  elif option == 3:
    print("""Informe se irá utilizar o frequência ou comprimento de onda do fóton:
1 - Numero quântico inicial
2 - Numero quântico final
""")
    i = int(input("Opção de entrada desejada: "))
    n = int(input('Digite o valor do numero quântico: '))
    print("""Informe se irá utilizar o frequência ou comprimento de onda do fóton:
1 - Frequência
2 - Comprimento""")
    j = int(input("Opção de entrada desejada: "))
    fc = float(input("Digite o valor: "))

    absorveAtomo(i, n, j, fc)
    message()
  elif option == 4:
    print("""Informe se irá utilizar o frequência ou comprimento de onda do fóton:
1 - Numero quântico inicial
2 - Numero quântico final
""")
    i = int(input("Opção de entrada desejada: "))
    n = int(input('Digite o valor do numero quântico: '))
    print("""Informe se irá utilizar o frequência ou comprimento de onda do fóton:
1 - Frequência
2 - Comprimento""")
    j = int(input("Opção de entrada desejada: "))
    fc = float(input("Digite o valor: "))

    emiteAtomo(i, n, j, fc)
    message()
