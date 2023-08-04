def fib_l(cnt):
    if cnt<=1:
        return cnt
    return(fib_l(cnt-1) + fib_l(cnt-2))