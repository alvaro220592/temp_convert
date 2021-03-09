# Programa que recebe do usuário uma lista de temperaturas em Celsius 
# e retorna outra com os valores convertidos em Fahrenheit.
# Ainda sem tratamento de erros.


def fahr(T):
    # fórmula matemática para conversão:
    return T * 1.8 + 32


# Número de temperaturas que o usuário pretende converter
temp = int(input('Qtas temp em °C vc quer converter p/ °F?\n'))


# Lista vazia de temperaturas em °F
temps_f = []


# Enquanto o tamanho da lista de °F for menor que o nº de entradas determinado pelo usuário no início:
i = 0
while len(temps_f) < temp:
    # Os valores de entrada se agregarão à lista de °F
    temps_f.append(float(input(f'Digite a {i + 1}ª temp\n')))
    i += 1


# variável que recebe a função map, que executa a função 'fahr' em cada elemento da lista de entrada
temps_convert = list(map(fahr, temps_f))


print('Temperaturas convertidas:')


# Mostrando as temperaturasconvertidas:
for t in temps_convert:
    print(t)
