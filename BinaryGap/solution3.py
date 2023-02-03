def binary_gap(n: int):
    n = abs(n)
    N=f"{n:b}"
    b=0
    maxb=0
    # approaching from the leading 1, since the binary representation always begins with 1
    # hit one to clear the local gap, and update the global max,
    # while hit zero just count the local
    # Note, you shall not starting from the tailing zeros, since the tail are not always start with 1.
    for k in N:
        if int(k) == 0:
            b += 1
        elif int(k) == 1:
            maxb = max(b, maxb)
            b=0
    return maxb            