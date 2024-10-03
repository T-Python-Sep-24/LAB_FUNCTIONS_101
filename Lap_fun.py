def mesi():
    '''this fun is solstion of our task in fun101... '''
    lis=[5,4,3,2,1]
    for i in range(1,6,1):
        print(lis)
        lis.pop(0)

messi=mesi()
print(mesi.__doc__, messi)


