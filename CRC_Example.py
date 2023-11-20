#!/usr/bin/python
# 
# Written by    : Chris Anderson
# Date          : November 20, 2023
# Description   : This code is meant to provide some idea as to what is happening with CRC. While this is in Python, this could easily be convert to C to be
#                   used with the actual JANUS protocol system. There are several debug print statements. To get a better understanding of what the CRC is actually
#                   doing, uncomment these and run the script. It is helpful to pipe the output to a text file to be able to read it easier. 
#                   To do this, type:
#                           python3 CRC_Example.py > output.txt

import math

# Initial inputVal and divisor "key"

# inputVal would be the JANUS packet
inputVal = 0b11010011101100

# divisor is known to generate CRC bits to be appended to JANUS packet
divisor  = 0b1011



# This is set for how many CRC bits there will be appended to a packet
CRC_bits = 3

# Append zeroes to the ends for however many CRC bits there are
inputVal <<= CRC_bits
divisor <<= (inputVal.bit_length() - divisor.bit_length())

# Find how many bits there are in the new input value with appended bits
numberOfInfoBits = inputVal.bit_length()

# Shows initial values in output
#print("Initial values:\ninputVal = {num0:#{bitlen}b}\ndivisor  = {num1:#{bitlen}b}\n\n".format(num0=inputVal,bitlen=numberOfInfoBits, num1=divisor))


# Start at the most significant bit, and work our way down. (numberOfInfoBits-1)
for i in range(numberOfInfoBits, 1, -1):

# Once we get values in the CRC bits, we no longer need to continue the operations
    if i <= CRC_bits:
        break


# This print statement shows what range the inputVal falls into, not important to the actual processing
#    print("inputVal = {:1}\ni = ${:2} or #ofbits{:3}\ni+1 = {:4} or {:5}\n".format(inputVal,pow(2,i-1),i-1,pow(2,i),i))


# The divisor must XOR with the most significant bit of inputVal, so we check if it falls in the range of where 
#  divisor is.
    if inputVal in range(pow(2,i-1)+1, pow(2,i)):
        inputVal ^= divisor
        divisor >>=1
# If not, we simply shift right by 1
    else:
        divisor >>=1
# Not necessary, but can help to understand the actual operation that is happening.
#    print("inputVal = {num0:#{bitlen}b}\ndivisor  = {num1:#{bitlen}b}\n\n".format(num0=inputVal,bitlen=numberOfInfoBits, num1=divisor))




# The code needs to go back since it continues on before it can be stopped in the for loop
remainder = inputVal & pow(2,CRC_bits)-1

print("Remainder = {num2:#{bitlen}b}".format(bitlen=numberOfInfoBits, num2=remainder))


