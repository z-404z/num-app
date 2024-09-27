def db(ip):
    dbb = bin(ip)[2:]
    print(f"{ip} in decimal is: {dbb} in binary.")

def dh(ip):
    dhh = hex(ip)[2:]
    print(f"{ip} in decimal is: {dhh} in hexadecimal.")
    
def dob(ip):
    obb = oct(ip)[2:]
    print(f"{ip} in decimal is: {obb} in octal.")

def bd(ip):
    try:
        bdd = int(ip, 2)
        print(f"{ip} in binary is: {bdd} in decimal.")
    except ValueError:
        print("Error: Input must be a binary number (only 0s and 1s).")

def bh(ip):
    decimal_value = int(ip, 2)
    hex_value = hex(decimal_value)[2:]
    print(f"{ip} in binary is: {hex_value} in hexadecimal.")

def bo(ip):
    decimal_value = int(ip, 2)
    octal_value = oct(decimal_value)[2:]
    print(f"{ip} in binary is: {octal_value} in octal.")

def hd(ip):
    decimal_value = int(ip, 16)
    print(f"{ip} in hexadecimal is: {decimal_value} in decimal.")

def hb(ip):
    decimal_value = int(ip, 16)
    binary_value = bin(decimal_value)[2:]
    print(f"{ip} in hexadecimal is: {binary_value} in binary.")

def ho(ip):
    decimal_value = int(ip, 16)
    octal_value = oct(decimal_value)[2:]
    print(f"{ip} in hexadecimal is: {octal_value} in octal.")

def od(ip):
    decimal_value = int(ip, 8)
    print(f"{ip} in octal is: {decimal_value} in decimal.")

def ob(ip):
    decimal_value = int(ip, 8)
    binary_value = bin(decimal_value)[2:]
    print(f"{ip} in octal is: {binary_value} in binary.")

def oh(ip):
    decimal_value = int(ip, 8)
    hex_value = hex(decimal_value)[2:]
    print(f"{ip} in octal is: {hex_value} in hexadecimal.")

print("---------------------------------------------------------------")
print("--------------- Hello in 'Z-404 APP' --------------------------")
print("---------------------------------------------------------------")
print("\n")

print("Enter a number: ")
ip = int(input())

while True:
    print("-----------------------------------")
    print("Press 'i' for more information")
    n = input()
    print("-----------------------------------")

    if n == 'i':
        print('To convert from Decimal to Binary press >> "db"')
        print('To convert from Decimal to Hexadecimal press >> "dh"')
        print('To convert from Decimal to Octal press >> "dob"')
        print("=============")
        print("=============")
        print('To convert from Binary to Decimal press >> "bd"')
        print('To convert from Binary to Hexadecimal press >> "bh"')
        print('To convert from Binary to Octal press >> "bo"')
        print("=============")
        print("=============")
        print('To convert from Hexadecimal to Decimal press >> "hd"')
        print('To convert from Hexadecimal to Binary press >> "hb"')
        print('To convert from Hexadecimal to Octal press >> "ho"')
        print("=============")
        print("=============")
        print('To convert from Octal to Decimal press >> "od"')
        print('To convert from Octal to Binary press >> "ob"')
        print('To convert from Octal to Hexadecimal press >> "oh"')

    x = input('Choose an operation: ')

    if x == 'db':
        db(ip)
    elif x == 'dh':
        dh(ip)
    elif x == 'dob':
        dob(ip)
    elif x == 'bd':
        binary_ip = input("Enter a binary number to convert: ")
        bd(binary_ip)
    elif x == 'bh':
        binary_ip = input("Enter a binary number to convert: ")
        bh(binary_ip)
    elif x == 'bo':
        binary_ip = input("Enter a binary number to convert: ")
        bo(binary_ip)
    elif x == 'hd':
        hex_ip = input("Enter a hexadecimal number to convert: ")
        hd(hex_ip)
    elif x == 'hb':
        hex_ip = input("Enter a hexadecimal number to convert: ")
        hb(hex_ip)
    elif x == 'ho':
        hex_ip = input("Enter a hexadecimal number to convert: ")
        ho(hex_ip)
    elif x == 'od':
        octal_ip = input("Enter an octal number to convert: ")
        od(octal_ip)
    elif x == 'ob':
        octal_ip = input("Enter an octal number to convert: ")
        ob(octal_ip)
    elif x == 'oh':
        octal_ip = input("Enter an octal number to convert: ")
        oh(octal_ip)
    else:
        print(", Please try again.")

    xx = input("Do you want to perform another conversion? (yes/no): ")
    if xx.lower() != 'yes':
        break
