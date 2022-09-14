from cmath import sqrt
from time import sleep

# Estamos utilizando o sistema internacional de medidas

# Constantes:
h = 4.136e-15 # Constante de planck (eV)
c = 3e8 # Velocidade da luz (m/s)
el = 8.854e-12 # Constante dielétrica (C^2/(N*(m^2)))
e = -1.602e-19 # Carga do elétron (C)
mE = 9.11e-31 # Massa do elétron (Kg)

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
    r = (n**2)*(5.29e-11) # raio da órbita de ordem n
    v = (1/el)*((e**2)/(2*n*h)) # velocidade orbital
    k = 13.6/(n**2) # energia cinética
    u = -27.2/(n**2) # energia potencial
    energia = -13.6/(n**2) # energia total
    comprimento = h/(v*mE) # comprimento de onda de uma partícula

    print(f'Raio: {r}\nVelocidade: {v}\nComprimento de onda: {comprimento}\nEnergia Cinética: {k}\nEnergia Potencial: {u}\nEnergia Total: {energia}')

def emiteAbsorveAtomo(ni, nf):
    energiaFoton = (-13.6/((nf**2)))-(-13.6/(ni**2))
    freq = energiaFoton / h
    comprimentoF = c/freq

    print(f'Energia do Fotón: {energiaFoton}\nComprimento de onda do fóton: {comprimentoF}\nFrequência: {freq}')

def absorveAtomo(i,n,j,fc):
    if (i == 1):
        # Conta para n inicial
        if (j == 1):
            # Conta para frequencia
            energia = h * fc
            energiaFinal = (-13.6/(n**2)) + energia
            nf = sqrt((13.6/energiaFinal))
            print(f'Numero quântico final: {nf}')
        else:
            # Conta para comprimento de onda
            energia = (h*c)/fc
            energiaFinal = (-13.6/(n**2)) + energia
            nf = sqrt((13.6/energiaFinal))
            print(f'Numero quântico final: {nf}')
    else:
        # Conta para n final
        if (j == 1):
            # Conta para frequencia
            energia = h * fc
            energiaFinal = (-13.6/(n**2)) - energia
            nf = sqrt((13.6/energiaFinal))
            print(f'Numero quântico inicial: {nf}')
        else:
            # Conta para comprimento de onda
            energia = (h*c)/fc
            energiaFinal = (-13.6/(n**2)) - energia
            nf = sqrt((13.6/energiaFinal))
            print(f'Numero quântico inicial: {nf}')

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
    propriedadesAtomo(n)
    message()
  elif option == 2:
    n = int(input('Digite o valor do numero quântico: '))
    quanticNumber(n)
    message()
  elif option == 3:
    i = int(input("Informe se irá utilizar o N° quânico final ou inicial (Digite 1 para Inicial e 2 para Final): "))
    n = int(input('Digite o valor do numero quântico: '))
    j = int(input("Informe se irá utilizar o frequência ou comprimento de onda do fóton (Digite 1 para Frequência e 2 para Comprimento): "))
    fc = float(input("Digite o valor: "))

    absorveAtomo(i, n, j, fc)
    message()
  elif option == 4:
    n = int(input('Digite o valor do numero quântico: '))
    quanticNumber(n)
    message()
