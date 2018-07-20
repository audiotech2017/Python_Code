
import time
t1 = time.time()

class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.available = []
        self.value = 0
    
def rownum(p,sudoku):
    row = []
    row = sudoku[p.y*9:(p.y+1)*9]
    row.remove(0)
    return row

    
def colnum(p,sudoku):
    col = []
    length = len(sudoku)
    for i in range (p.x, length ,9):
        col.append (sudoku[i])
    col.remove(0)
    return col

def blocknum(p,sudoku):
    block_x = p.x//3
    block_y = p.y//3
    block = []
    startpos = block_y*9*3 + block_x*3
    for i in range (startpos,startpos+3):
        block.append (sudoku[i])
    for j in range (startpos+9,startpos+3+9):
        block.append (sudoku[j])
    for k in range (startpos+9+9,startpos+3+9+9):
        block.append (sudoku[k])
    block.remove(0)
    return block
        
    
def initpointlist(sudoku):
    pointlist = []
    length = len(sudoku)
    for i in range(length):
        if sudoku[i] == 0:
            p = point(i%9,i//9)
            for j in range (1,10):
                area = blocknum(p,sudoku) + rownum(p,sudoku) + colnum(p,sudoku)
                if j not in area:
                    p.available.append (j)
            pointlist.append (p)

    return pointlist
            
def validatepos(p,sudoku):
    if p.value ==0:
        return False
    area = blocknum(p,sudoku) + rownum(p,sudoku) + colnum(p,sudoku)
    if p.value not in area:
        return True
    else:
        return False
    
def tryinsert(p,sudoku):
    availnum = p.available
    for value in availnum:
        p.value = value
        if validatepos(p,sudoku) == True:
           sudoku[p.y*9+ p.x] = p.value
           #print ('this is the Point List', len(pointlist))
           if len(pointlist) <= 0:
               print('This is the Image After Changes')
               showsudoku(sudoku)
               t2 = time.time()
               t0 = t2-t1
               print ('\nProcess Completed within %s s' %t0)
               exit()
           else:
               pass
            
           p2 = pointlist.pop()
           tryinsert(p2,sudoku)
           sudoku[p.y*9+p.x] = 0
           sudoku[p2.y*9+p2.x] = 0
           pointlist.append (p2)

def showsudoku(sudoku):
    for y in range (9):
        for x in range (9):
            if x == 8:
                print (sudoku[y*9+x])
            else:
                print (sudoku[y*9+x], end = ' ')



if __name__=='__main__':  
    sudoku=[  
            8,0,0,0,0,0,0,0,0,  
            0,0,3,6,0,0,0,0,0,  
            0,7,0,0,9,0,2,0,0,  
            0,5,0,0,0,7,0,0,0,  
            0,0,0,0,4,5,7,0,0,  
            0,0,0,1,0,0,0,3,0,  
            0,0,1,0,0,0,0,6,8,  
            0,0,8,5,0,0,0,1,0,  
            0,9,0,0,0,0,4,0,0,  
            ]
    
    sudokubefore = sudoku
    pointlist=initpointlist(sudoku)
    print('This is the Image before Changes')  
    showsudoku(sudoku)  
    print('\n')  
    p = pointlist.pop()  
    tryinsert(p,sudoku)
    print('This is the Image After Changes')  
