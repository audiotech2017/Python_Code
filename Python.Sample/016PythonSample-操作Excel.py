
import xlrd #pip install Xlrd
df=xlrd.open_workbook('data.xlsx')  
table=df.sheet_by_name('早起Python')
data_list=[] 
for i in range(table.nrows):
    data_list.append(table.row_values(i))
data_list1 = []
data_list1 = data_list[::-1]
item = data_list1.pop(-1)
data_list1.insert(0,item)
import xlwt
df2 = xlwt.Workbook()
table2=df2.add_sheet('早起Python')
for i in range(2):
    for j in range(9):
        table2.write(i,j,data_list1[j][i])
df2.save('data2.xls')