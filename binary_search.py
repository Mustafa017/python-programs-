def binarysearch(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if item == midpoint:
            return True
        else:
            if item < midpoint:
                return binarysearch(alist[:midpoint],item)
            else:
                return binarysearch(alist[midpoint:],item)
alist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarysearch(alist,3))
print(binarysearch(alist,13))
