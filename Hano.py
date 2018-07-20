def my_print (x):
    print (x)

def move(n,a,b,c):
    my_print((n, a,'-->',c))
    if n == 1:
        pass
    else: (move(n-1,a,c,b)) or (move(n-1,b,a,c))

move(3,'a','b','c')
