def move(n,x,y):
    print ('move ' ,n , 'from ', x,' to ',y)

def hannuo(n,a,b,c):

    if n==1:
        move(1,a,c)
    else:
        hannuo(n-1,a,c,b)
        move(n,a,c)
        hannuo(n-1,b,a,c)
        
hannuo(3,'a','b','c')
