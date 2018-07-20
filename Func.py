

def Print_Dict():
        dict = {'Name':'Eric', 'Age':23}
        dlist = [key for key in dict.keys()]
        print (dlist)
        for x in dict.values():
                print (x)


def Print_Dictx():
        d = {'One':1,'Two':2,'Three':3,'Four':4}
        di = {v:k for k, v in d.items()}
        print (di.items)
        print (d.items)
        for v in di.items():
            print (v)
        for key,value in d.items():
                if value == 1:
                        print (key)


Print_Dict()
