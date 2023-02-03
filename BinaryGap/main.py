import solution1
import solution2
import solution3
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
        time_list = []
        solution_list = []
        # timer seconds as float
        t1 = timer()
        solution_list.append(solution1.binary_gap(e))
        t2 = timer()
        solution_list.append(solution2.binary_gap(e))
        t3 = timer()
        solution_list.append(solution3.binary_gap(e))
        t4 = timer()
        time_list.append(t2-t1)
        time_list.append(t3-t2)
        time_list.append(t4-t3)
        print("#" * 10)
        print(f"binary_gap for {e} = {bin(e)}")
        print(f"s1: gap size {solution_list[0]} in secs as float {time_list[0]}")
        print(f"s2: gap size {solution_list[1]} in secs as float {time_list[1]}")
        print(f"s3: gap size {solution_list[2]} in secs as float {time_list[2]}")
        # index of the best solution, + 1 is the solution id, since index of solution 1 is 0
        print(f"solution{min(range(len(time_list)), key=time_list.__getitem__) + 1} is faster.")
        if (len(set(solution_list)) > 1):
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
