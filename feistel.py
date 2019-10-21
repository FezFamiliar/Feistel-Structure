#!/usr/bin/python
import random
from bitarray import bitarray





def padding(msg):

    a = bitarray(endian='big')
    a.frombytes(msg.encode('ascii'))
    while len(a) % 64 != 0:
        a.append(0)

    return a


def Feistel_struct(msg,key):
    

    left = [None] * 16
    right = [None] * 16

    left[0]  = msg[0:32]
    right[0] = msg[32:64]


    for i in range(1,16):
        left[i] = right[i - 1]
        right[i] = left[i - 1]  ^ f(right[i - 1],key)


    left = [int.from_bytes(word.tobytes(),byteorder='little') for word in left]
    right = [int.from_bytes(word.tobytes(),byteorder='little') for word in right]
    return format(left[15],'0x') + format(right[15],'0x')





   

def f(msg,key):
    r  = random.randrange(key%32,32)
    s = bitarray(r)
    while len(s) % 32 != 0:
        s.append(0)

    for x in range(key):
       msg |= s


    return msg

message = 'fox'
secretKey = 3000



print(Feistel_struct(padding(message),secretKey))

