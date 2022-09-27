# Estamos utilizando o sistema internacional de medidas

# Constantes:
from math import sqrt
from time import sleep


h = 4.136e-15  # Constante de planck (eV*s)
hJoule = 6.6262e-34  # Constante de planck (J*s)
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
print("""
Este código desenvolvido na linguagem Python explora as propriedades dos níveis específicos de energia do átomo de hidrogênio. 
Para a utilização do programa, primeiramente deve-se escolher entre as opções mostradas, respondendo com o número correspondente 
ao cálculo desejado, e então as entradas requeridas, que variam de acordo com a opção. Desse modo, o programa é capaz de calcular 
o nível quântico (a partir do nível inicial ou final), a frequência, e o comprimento de onda do fóton que está sendo absorvido 
ou emitido durante a transição.

Series do Hidrogênio:
Lyman => n° Final = 1 e n° Inicial > 1
Balmer => n° Final = 2 e n° Inicial > 2
Paschen => n° Final = 3 e n° Inicial > 3
Brackett => n° Final = 4 e n° Inicial > 4
Pfund => n° Final = 5 e n° Inicial > 5
""")


def message():
  input("""
-------------------------------------------
Digite ENTER para continuar com os cálculos
-------------------------------------------
""")

def propriedadesAtomo(n):
  r = (n**2)*(5.29e-11)  # raio da órbita de ordem n
  v = (1/el)*((e**2)/(2*n*hJoule))  # velocidade orbital
  k = 13.6/(n**2)  # energia cinética
  u = -27.2/(n**2)  # energia potencial
  energia = -13.6/(n**2)  # energia total
  comprimento = abs(hJoule/(v*mE))  # comprimento de onda de uma partícula

  print(f'\nRaio: {r:.3} m\nVelocidade: {v:.3} m/s\nComprimento de onda: {comprimento:.3} m\nEnergia Cinética: {k:.3} eV\nEnergia Potencial: {u:.3} eV\nEnergia Total: {energia:.3} eV')

def emiteAbsorveAtomo( ni, nf):
  energiaNInicial = (-13.6/(ni**2))
  energiaNFinal = (-13.6/((nf**2)))

  energiaFoton = energiaNFinal- energiaNInicial
  freq = abs(energiaFoton / h)
  comprimentoF = c/freq

  print(
    f'\nEnergia do Fotón: {energiaFoton:.4} eV\nComprimento de onda do fóton: {comprimentoF:.4} m\nFrequência: {freq:.4} Hz')

def absorveAtomo(i, n, j, fc):
  if (i == 1):
    # Conta para n inicial
    if (j == 1):
      # Conta para frequência
      energiaFoton = h * fc
      energiaFinal = (-13.6/(n**2)) + energiaFoton
      divisao = (13.6/abs(energiaFinal))
      nf = sqrt(divisao)
      print(f'\nN° quântico final: {nf:.3}')
    else:
      # Conta para comprimento de onda
      energiaFoton = (h*c)/fc
      energiaFinal = (-13.6/(n**2)) + energiaFoton
      nf = sqrt(13.6/abs(energiaFinal))
      print(f'\nN° quântico final: {nf:.3}')
  else:
    # Conta para n final
    if (j == 1):
      # Conta para frequência
      energiaFoton = h * fc
      energiaFinal = (-13.6/(n**2)) - energiaFoton
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'\nN° quântico inicial: {nf:.3}')
    else:
      # Conta para comprimento de onda
      energiaFoton = (h*c)/fc
      energiaFinal = (-13.6/(n**2)) - energiaFoton
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'\nN° quântico inicial: {nf:.3}')

def emiteAtomo(i, n, j, fc):
  if (i == 1):
    # Conta para n inicial
    if (j == 1):
      # Conta para frequencia
      energia = h * fc
      energiaFinal = (-13.6/(n**2)) - energia
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'\nN° quântico final: {nf:.3}')
    else:
      # Conta para comprimento de onda
      energia = (h*c)/fc
      energiaFinal = (-13.6/(n**2)) - energia
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'\nN° quântico final: {nf:.3}')
  else:
    # Conta para n final
    if (j == 1):
      # Conta para frequencia
      energia = h * fc
      energiaFinal = (-13.6/(n**2)) + energia
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'\nN° quântico inicial: {nf:.3}')
    else:
      # Conta para comprimento de onda
      energia = (h*c)/fc
      energiaFinal = (-13.6/(n**2)) + energia
      nf = sqrt((13.6/abs(energiaFinal)))
      print(f'\nN° quântico inicial: {nf:.3}')

while True:
  print("\n-----------------Menu-----------------")
  print("""Indique o seu cálculo:
1 - Propriedades do átomo de Hidrogênio 
2 - Energia / Comprimento de Onda / Frequência (Emissão/Absorção de fóton)
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
    print("""Informe se irá utilizar número quântico inicial ou final:
1 - N° quântico inicial
2 - N° quântico final
""")
    i = int(input("Opção de entrada desejada: "))
    n = int(input('Digite o valor do numero quântico: '))
    print("""\nInforme se irá utilizar o frequência ou comprimento de onda do fóton:
1 - Frequência [Hz]
2 - Comprimento [m]
""")
    j = int(input("Opção de entrada desejada: "))
    fc = float(input("Digite o valor: "))

    absorveAtomo(i, n, j, fc)
    message()
  elif option == 4:
    print("""Informe se irá utilizar o número quântico inicial ou final:
1 - N° quântico inicial
2 - N° quântico final
""")
    i = int(input("Opção de entrada desejada: "))
    n = int(input('Digite o valor do numero quântico: '))
    print("""\nInforme se irá utilizar o frequência ou comprimento de onda do fóton:
1 - Frequência [Hz]
2 - Comprimento [m]
""")
    j = int(input("Opção de entrada desejada: "))
    fc = float(input("Digite o valor: "))

    emiteAtomo(i, n, j, fc)
    message()
