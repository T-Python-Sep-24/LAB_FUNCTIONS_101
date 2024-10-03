def mesi(i):
    '''this fun is solstion of our task in fun101... '''
    lis=[5,4,3,2,1]
    for i in range(1,i,1):
        print(lis)
        lis.pop(0)
mesi(6)
print(mesi.__doc__)