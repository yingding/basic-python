# Intro

maximal sequence of consecutive zeros 

* 9 is represented in bits '0b1001' a binary gap between the leading 1 and least significat 1 is 2, since there is two zeros in between the two 1s.
* 1000010001 with gap 4 zeros and gap 3 zeros, so the gap is the max which is 4
* 1111 no gap
* 1000 no gap
* -9 = '-0b1001' Gap = 2 zero

## using bit shift right
* Algo solution is in file `main.py`
* file `test.py` contains some useful method to get used with bitwise op and bitwise shift op and python buildin functions

Sketch of algo: 
1. get the least significant bit
2. bit shift right and repeat till the 0
3. cache the prevous and current least significant bit
4. cache the global and current binary gap sequence
5. use the information in previous and current least significant bit and cached current binary gap length to determin action
6. special case of negative number, the shift right will encounter the leading sign, so need to convert to positive number first. 


Notice:
* python has no sign bit
https://realpython.com/python-bitwise-operators/

## show the unicode value of char
```python3
ord('a')
```

## least significant bit
* `9` is represented with `0b1001`
* use a bitwise and `&` op to mask the last bit of an int number
```python3
>>> 9 & 1
1
```

## perform floor op with left bit shift
* left bit shift of 1 bit is `n >> 1` which is the same as floor operation `n // 2`

## Print binary format
```python3
>>> f'{6:08b}'
'00000110'
```

Reference: 
* very good intro regarding to binary shift and binary operation in pytion https://realpython.com/python-bitwise-operators/
* how to convert int to binary in python with bin function : https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python/10411108#10411108

