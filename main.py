import fibo
def write_otherfile(filename,list):
    with open(filename, 'w' ) as file:
        for i in list:
            file.write(str(i) + '\n')

fiblist=[i for i in range(11)]
for i in range(11):
    fiblist[i]=fibo.fib_l(i)
for j in range(11):
    print(fibo.fib_l(j))
filename ="output.txt"
write_otherfile(filename,fiblist)