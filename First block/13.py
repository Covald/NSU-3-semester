"""
Перевод из одной системы счисления в другую
"""

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

Num = input("Enter num - ")
base, new_base = map(int, input("Enter base, new base - ").split())

print(convert_base(Num, new_base, base))