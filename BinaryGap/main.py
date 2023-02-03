# Python 3.10
import sys
from timeit import default_timer as timer

def binary_gap(n: int):
    # shift doesn't work well on the negative number, negate it.
    if (n < 0):
        n = -n
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
                if cur == 1 and pre == 0 and max_gap < cur_gap: 
                    # in case of switch from 0 binary to 1, check if the current binary gap is great than the global max binary gap
                    # update the global value and reset current binary gap if the last binary gap is large than the previous binary gap
                    max_gap = cur_gap
                    cur_gap = 0
        n = n >> 1
        pre = cur
    return max_gap

if __name__ == "__main__":
    print(sys.byteorder)
    # input is a python buildin function
    # 0bXXX is the binary representation of number
    # 0xYYYYY is the hex representtion of number
    # sys.maxsize returns the max int value (32bit, 2^32 -1 with zero)
    # max negative int is -sys.maxsize-1 (32bit), but it switch to long automatically 
    l = [8, 9, 15, int(0b1000010001), 0, -9, -8, sys.maxsize, -sys.maxsize-1, -sys.maxsize - 9]
    for e in l:
        # timer seconds as float
        start = timer()
        gap = binary_gap(e)
        end = timer()
        print(f"binary_gap for {bin(e)} is: {gap} in secs as float {end - start}")  
        # print(f"binary_gap for {bin(e)[2:]} is: {binary_gap(e)}")  