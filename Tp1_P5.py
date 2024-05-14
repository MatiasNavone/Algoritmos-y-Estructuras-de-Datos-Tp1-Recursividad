#Desarrollar una función que permita convertir un número romano en un número decimal.

def valor(rom_num):
    Romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(rom_num) == 0:
        return 0
    elif len(rom_num) == 1:
        return Romano[rom_num[0]]
    else:
        if Romano[rom_num[0]] < Romano[rom_num[1]]:
            return Romano[rom_num[1]] - Romano[rom_num[0]] + valor(rom_num[2:])
        else:
            return Romano[rom_num[0]] + valor(rom_num[1:])

rom_num = input("Ingrese un numero romano: ").upper()
dec_num = valor(rom_num)
print("El numero decimal equivalente a", rom_num, "es:", dec_num)
