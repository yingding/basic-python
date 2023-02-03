a = ord('a')
z = ord('z')

print(a)
print(z)

# show 26 chars in the english letter
print(z - a + 1)

a = 1
# shift left one is a x 2
print( a << 1)
# shift left two is a x 4
print( a << 2)

# a << n = a x (2 exp n)

# bit shift with a mask
# a byte has 8 bits, which is 255 as int number represented with 11111111
# while shifting the number 39 << 3 3 bits left shifted from 6 bits to 9 bits,
# to cut of the first 9th bit, use a bit marks of 255 with bit and operator 

print((39).bit_length())
print((255).bit_length())
print((39 << 3).bit_length())

print(( (39 << 3) & 255).bit_length())

# A bitwise rigth shift is a fast floor 
print(5 >> 1) # 2
print(5 // 2) # 2
print(5 / 2) # 2.5

# bit length of 9
print(f"bit length of 9 is: {(9).bit_length()}")

# create a binary string
a = 9
print(f"{a:b}")

# getting a bit at given position
def get_bit(value, bit_index):
    return value & (1 << bit_index)

# get the least significant bit
def get_normalized_bit(value, bit_index):
    # always masked with one bit
    return (value >> bit_index) & 1

# give the first/zero bit of number 9 which is 1
# the first bit is not 1 to shift but zero to shift
print(get_normalized_bit(9, 0))

print(0b10)
print(10)
print(0x10)

print(len("00000000000000000000000000000000000000000000000000000000000"))


