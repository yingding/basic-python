# Intro

maximal sequence of consecutive zeros 

* 9 is represented in bits '0b1001' a binary gap between the leading 1 and least significat 1 is 2, since there is two zeros in between the two 1s.
* 1000010001 with gap 4 zeros and gap 3 zeros, so the gap is the max which is 4
* 1111 no gap
* 1000 no gap
* -9 = '-0b1001' Gap = 2 zero

## Solution1: Using bit shift right
* Implementation is in file `solution1.py`
* file `test.py` contains some useful method to get used with bitwise op and bitwise shift op and python buildin functions

Sketch of algo: 
1. get the least significant bit
2. bit shift right and repeat till the 0
3. cache the prevous and current least significant bit
4. cache the global and current binary gap sequence
5. use the information in previous and current least significant bit and cached current binary gap length to determin action
6. special case of negative number, the shift right will encounter the leading sign, so need to convert to positive number first. 

## Solution2: use internal property that gap are enclosed by two 1s
* Implementation is in file `solution2.py`

Sketch of algo:
1. negate the negative number
2. use `f"{n:b}"` to output the string representation of binary number
3. tailer the leading and tailing 0, `strip("0")`
4. split the string by `1` with `split("1")`, between `1` and `1`, the split will be `` and empty string.
5. max the size of the string element in the splited list to find the max len `max(binary_str.split("1")`
6. return the `len(max(list))``

General idea
```python
n = abs(n)
list_gaps = f"{n:b}".strip('0').split('1')
len(max(list_gaps))
```

This string split solution has some copy over of string, since the binary representation of very large number is still in magnitude of 1000, the string `split` and `len` solution is faster than the binary shift solution.

## Solution 3, counting the sequence from the leading most significant bit
* Implementation is in file `solution1.py`

Sketch of Algo:
1. hit 1 by update the global max, and clear the local sequence of zero count
2. hit 0 by update the local sequence of zero count
3. since the binary string of integer always starts with zero, so the first zero can be considered as binary gap
4. WARNING: do not start from the tailing least significat bit, since the tailing bit will not always be 1, this simple algorithm will not work.

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
or
```python3
>>> bin(9)
'0b1001'
```

## split string into char
```python3
>>> print([a for a in "123"])
['1', '2', '3']
>>> print(list("123"))
['1', '2', '3']
```

## index max of a list
```python3
>>> list = [2,2,10]
>>> max(range(len(list)), key=list.__getitem__)
2
```

Reference: 
* very good intro regarding to binary shift and binary operation in pytion https://realpython.com/python-bitwise-operators/
* how to convert int to binary in python with bin function : https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python/10411108#10411108

