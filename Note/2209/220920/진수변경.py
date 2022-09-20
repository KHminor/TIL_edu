# a = 3
# print(f'{a:04b}')
# key = 0~F
hex_to_bin = {hex(i).replace('0x','').upper():f'{i:04b}' for i in range(16)}
print(hex_to_bin)