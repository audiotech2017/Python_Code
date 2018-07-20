
import time

t1 = time.time()

max = 10000000000000
ListNum = []
for num in range(2,max):
    for i in  range(2,num):
        if num%i == 0:
            j = num/i
            break
    else:
        for x in range (2,num):
            if num == 2**x - 1:
                t2 = time.time()
                t0 = t2 - t1
                t1 = t2
                print ('Duration = %d' %t0, num, '是质数', '%d = 2 ** %x - 1' %(num,x))
                break




