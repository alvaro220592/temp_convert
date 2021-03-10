def conv(T):
    return T * 1.8 + 32

temp_c_list = []

length = int(input('Insira a quantidade de temperaturas a converter\n'))

while len(temp_c_list) < length:
    temp_c_list.append(float(input('Insira\n')))

print(temp_c_list)

for i in map(conv, temp_c_list):
    print(i)
