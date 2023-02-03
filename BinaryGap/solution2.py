def binary_gap(n: int):
    # if (n < 0):
    #    n = -n
    n = abs(n)    
    binary_str = f"{n:b}" # return the binary string "1001" for n=9
    binary_str = binary_str.strip("0") # remove the leading and tailing 0, one string copy
    ''' 
    all intermediate 0s sequence with split("1"), between 11, returns "" for split
    max of "", "0", "000" will be "000"
    the max of "-", "", from "-1".split("1"), will be ["-", ""], need to negate the negative number
    '''
    max_gap_str = max(binary_str.split("1")) 
    return len(max_gap_str)