# Python 3.10
import sys
from timeit import default_timer as timer

def binary_gap(n: int):
    # shift doesn't work well on the negative number, negate it.
    # if (n < 0):
    #    n = -n
    n = abs(n)      
    max_gap = 0
    cur_gap = 0
    pre = 0
    cur = 0
    while n > 0:
        # bit mask of the least significant bit
        # for 0b10 is the 0, 0b10 is 2 , which is 2 to the power of 1
        cur = n & 1 
        if cur == 0 and pre == 1: # only if the previous significant bit is one start counting
            cur_gap += 1
        else:
            if cur == 0 and cur_gap > 0: 
                # in case of consecutive 0, increate the current gap sequence count only if the current gap is none zero
                cur_gap += 1    
            else: 
                if cur == 1 and pre == 0:
                    # if current gap large, update global
                    if (max_gap < cur_gap):
                        max_gap = cur_gap
                    # in case of switch from 0 binary to 1, always clean
                    cur_gap = 0
        n = n >> 1
        pre = cur
    return max_gap
 