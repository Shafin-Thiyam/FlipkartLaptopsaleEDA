def summing(N):
    sumNum=0
    lst=list()
    for i in range(N):
        if(i+1==N):
            lst.append(-sumNum)
        else:
            sumNum+=i
            lst.append(i)
    return lst