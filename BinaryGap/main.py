import solution1
import solution2
import sys
from timeit import default_timer as timer

def main():
    print(sys.byteorder)
    # input is a python buildin function
    # 0bXXX is the binary representation of number
    # 0xYYYYY is the hex representtion of number
    # sys.maxsize returns the max int value (32bit, 2^32 -1 with zero)
    # max negative int is -sys.maxsize-1 (32bit), but it switch to long automatically 
    l = [8, 9, 15, 100, int(0b1000010001),int(0b10101101011100111111), int(0b1010110101101010101111100110001111) , 0, -9, -8, sys.maxsize, -sys.maxsize-1, -sys.maxsize - 9]
    has_warning = False
    waring_list = []
    for e in l:
        # timer seconds as float
        t1 = timer()
        s1_gap = solution1.binary_gap(e)
        t2 = timer()
        s2_gap = solution2.binary_gap(e)
        t3 = timer()
        time_1 = t2-t1
        time_2 = t3-t2
        print("#" * 10)
        print(f"binary_gap for {e} = {bin(e)}")
        print(f"s1: gap size {s1_gap} in secs as float {time_1}")
        print(f"s2: gap size {s2_gap} in secs as float {time_2}")
        print(f"{'solution1' if (time_1 < time_2) else 'solution2'} is faster.")
        if (s1_gap != s2_gap):
            has_warning = True
            waring_list.append(e)
            print("WARNING: different solution found.")
            
    if (has_warning):
        print("="* 10)
        print("WARNING: solutions has different result detected!!!")
        print(waring_list)
    else:
        print("==pass"* 10)
        print("Same results for all solution implementations.")


if __name__ == "__main__":
    main()
