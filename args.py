def myfunc(*args):
    mylist = []

    for item in args:
        if item % 2 == 0:
            mylist.append(item)
        else:
            pass

    print(mylist)
    #return mylist


myfunc(5,6,7,8)
