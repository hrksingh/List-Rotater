def list_rotater(alist, k):

    for i in range(k):
        alist.append(alist[0])
        del alist[0]

    print(alist)
        
        
        


k = 2;
alist = [1,2,3,4,5,6]

list_rotater(alist,k)
