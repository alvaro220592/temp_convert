"""temp_convert.py: Converte uma lista de temperaturas inseridas pelo usuário de Celsius para Fahrenheit"""

__author__  = "Álvaro"

def conv(T):
"""Função de conversão de Celsius para Fahrenheit:"""
    return T * 1.8 + 32

# Lista que receberá as temperaturas em °C:
temp_c_list = []

# Apresentação do programa:
print('\n====================================================\n'
        ' Conversor de temperaturas - Celsius para Fahrenheit\n'
        '====================================================\n'
        )

# Quantidade de teperaturas que serão inseridas pelo usuário
qtde = int(input('Quantas temperaturas você deseja converter para Fahrenheit?\n'))

# Enquanto o tamanho da lista de temperaturas em °C for menor que a 
# quantidade inserida, o programa pedirá por uma nova temperatura
i = 1
while len(temp_c_list) < qtde:
    temp_c_list.append(float(input(f'\nInsira a {i}ª temperatura\n')))
    i += 1

# Lista que receberá as temperaturas já convertidas para °F
temp_f_list = []

# Cada elemento na lista de temperaturas em °C, submetido à função map, 
# que aplica a função de conversão nos mesmos, será agregado à lista de 
# temperaturas em °F
for i in map(conv, temp_c_list):
    temp_f_list.append(i)

print('\nResultado:')

'''
Para cada índice e valor na lista de temperaturas em °F, serão mostradas, tanto as inseridas em °C pelo usuário, quanto as convertidas em °F. Obs: para a listagem das temperaturas em °C, em suas indexações foram usados os mesmos índices da lista de temperaturas em °F, pois os números são iguais
'''
for indice, valor in enumerate(temp_f_list):
    print(f'{indice + 1}ª temperatura: {temp_c_list[indice]}°C = {valor:.1f}°F')
