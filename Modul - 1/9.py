#Nomer 9
def ums() :
    for i in range(101) :
        if (i+1) % 15 == 0 :
            print("Python UMS")
        elif (i+1) % 3 == 0 :
            print("Python")
        elif (i+1) % 5 == 0 :
            print("UMS")
        else :
            print(i+1)
