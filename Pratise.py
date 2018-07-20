

dictx = {'red':'1','blue':'2'}
dict1 = {'Name' : 'John1', 'Age' : '22', 'Sex' : 'Male'}
#dict = {'Name' : 'John2', 'Age' : '23', 'Sex' : 'Feale'}
#dict = {'Name' : 'John3', 'Age' : '24', 'Sex' : 'Feale'}
#TinyDict = {'Name' : 'John5', 'Age' : '24', 'Sex' : 'Feale'}


while True:
      try: print (dict1.popitem())
      except KeyError:
            print ('End of the Dictionary')
            break
            

print ('print of dictx')
for x in dictx:
      print(x, dictx[x])
      
print ('Add dict1')      
for x in dictx:
      try: dict1[x] = dictx[x]
      except KeyError:
            print ('key error')
            break

print ('print of dict1')
for x in dict1:
      print (x, dict1[x])
