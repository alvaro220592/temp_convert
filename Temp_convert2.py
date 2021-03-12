"""Temp_conver2t.py: Converte uma lista de temperaturas inseridas pelo usuário de Celsius para Fahrenheit - Praticando tratamento de erros"""

__author__  = "Álvaro"

def conversor():

    def conv(T):
        """Função de conversão de Celsius para Fahrenheit:"""
        return T * 1.8 + 32

    print('\n=====================================================\n'
            ' Conversor de temperaturas - Celsius para Fahrenheit\n'
            '=====================================================\n'
            )

    def ask_qtde():

        value_error_msg = 'ERRO: Insira apenas números ou pressione Ctrl+c para sair'

        def ask_temp():
            while True:
                try:
                    i = 1
                    while len(temp_c_list) < qtde:
                        if qtde == 1:
                            temp_c_list.append(float(input(f'\nInsira a temperatura\n')))
                        else:
                            temp_c_list.append(float(input(f'\nInsira a {i}ª temperatura\n')))
                        i += 1
                except ValueError:
                    print(value_error_msg)
                    continue

        while True:
            try:
                qtde = int(input('\nQuantas temperaturas você deseja converter para Fahrenheit?\n'))
                if qtde == 0:
                    print('Ok, saindo...')
                    exit()
            except ValueError:
                print(value_error_msg)
                continue
            except KeyboardInterrupt:
                print('\nExecução interrompida pelo usuário.')
                exit()
            else:
                temp_c_list = []

                ask_temp()

                temp_f_list = []
                for i in map(conv, temp_c_list):
                    temp_f_list.append(i)

                print('\nResultado:')
                for indice, valor in enumerate(temp_f_list):
                    if qtde == 1:
                        print(f'Temperatura: {temp_c_list[indice]}°C = {valor:.1f}°F')
                    else:
                        print(f'{indice + 1}ª temperatura: {temp_c_list[indice]}°C = {valor:.1f}°F')
                exit()
    ask_qtde()

conversor()
