import math

# Binary value entry 1010 0101 0111 1011 1110 1100 
#        This is equal to 0xA5 7B EC 00
#
# Note, the '00' on the end is for the actual CRC

inputVal = 0b1101001101100000
divisor  = 0b1011000000000000
remainder= 0b0000000000000000

#print("inputVal = {:#018b}\ndivisor  = {:#018b}\n\n".format(inputVal,divisor))

remainder = inputVal

for i in range(0,12):
    print("inputVal = {:#018b}\ndivisor  = {:#018b}\n\n".format(remainder,divisor))
    # Need if statement since it needs to go to the next 1 in line
    remainder = remainder ^ divisor
    divisor = divisor>>1
"""    

# Padding of 3
val1 = 0b1101001101100000
val2 = 0b1011000000000000

tmp = val1 ^ val2

print("Dividee = {:#018b} \nDivider = {:#018b} \nRemainr = {:#018b}".format(val1, val2, tmp))

val1_next = tmp
val2_shift = val1<<1

tmp = val1_next ^ val2_shift

print("\n\nDividee = {:#018b} \nDivider = {:#018b} \nRemainr = {:#018b}".format(val1_next, val2_shift, tmp))

inputVal = 0b10100101011110111110110000000000

# Binary value for CRC-8 (8-bit) 0xD5 00 00 00 
#
# Note, past the first 8 bits, the rest of the zeroes are for padding to preform
# the operations

crcKey = 0b11010101000000000000000000000000
# This is equivalent to the polynomial x^8 + x^7 + x^6 + x^4 + x^2 + 1

# Temp binary value = 0x00 00 00 00
resultant = 0b00000000000000000000000000000000

for i in range(0,24):
    resultant = inputVal ^ crcKey
    inputVal = resultant
    crcKey>>1

    if (resultant>>8) == 0:
        break
print("CRC gives a remainder of {:1} with a final encoded product of {:2}".format(bin(inputVal<<24),bin(inputVal)))
"""