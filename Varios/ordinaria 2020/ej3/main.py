def getIndices(A:list,x:int):
    if len(A)==1 and A[0]==x:
        return 1
    else:
        return [1+getIndices(A[:len(A)//2],x)]+[[(len(A)//2)+getIndices(A[len(A)//2:],x)]]
