# -*- coding: utf-8 -*-
import os,sys
import xlrd
 
 
default_encoding = 'gbk'
'''
    ?????????????
'''
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
     
def search(base):
    pattern = '.xls'
    fileresult = []
    cur_list = os.listdir(base)
    for item in cur_list:
        full_path = os.path.join(base, item)
        if os.path.isdir(full_path):            
            fileresult += search(full_path)
        if os.path:
            if full_path.endswith(pattern):
                fileresult.append(full_path)
    return fileresult                
     
def run(dir1,dir2):
    root = dir1
    dirout = dir2 + '\\csv'
    if os.path.exists(dirout) == False:
        os.makedirs(dirout)
    else:
        pass
    base = root
    for result in search(base):
        print ('Input from:%s' %result)
        filename = os.path.basename(result) 
        dirname = os.path.dirname(result)
        dir1_1 = os.path.split(dir1)    
        dirname1 = os.path.split(dirname) 
        outputdir = dirname1[0].split(dir1_1[0])
        newdir = dirout + os.sep + outputdir[1] + os.sep + dirname1[1] + os.sep 
        print ('Output to:%s' %newdir)
        if os.path.exists(newdir) == False:
            os.makedirs(newdir)
        else:
            pass
        a = xlrd.open_workbook(result)
        for i in a.sheets():
            output = open(newdir + filename.decode('gbk')+"_"+ i.name + ".csv",'a')
            for r in range(i.nrows):
                linevalue = []
                for l in range(i.ncols):
                    if i.cell(r,l).ctype == 0:
                        linevalue.append(('%*s'%(4,' ')))   
                    else:
                        b = i.cell(r,l).value
                        if type(b) == type(4.0):
                            b= str(b)
                        linevalue.append(b)
                d = ','.join(linevalue).encode('gbk')
                output.write(d+'\n') 
            output.write(os.linesep)
        output.close()
 
if __name__ == '__main__':
    dirs = sys.argv
    if len(dirs)!=3:
        print ('???????'.decode('utf-8') )
        sys.exit()
    run(dirs[1],dirs[2])
