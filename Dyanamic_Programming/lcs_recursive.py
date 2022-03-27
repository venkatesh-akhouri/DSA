def recursiveLCSLength(x,y,m,n):
    #base condition
    if(m==0 or n==0):
        return(0)
    elif(x[m-1]==y[n-1]):
        return 1+(recursiveLCSLength(x,y,m-1,n-1))
    else:
        return max(recursiveLCSLength(x,y,m-1,n),recursiveLCSLength(x,y,m,n-1))






x=input("str 1")
y=input("str 2")
m=len(x)
n=len(y)
l=recursiveLCSLength(x,y,m,n)
print("length of max subsequence is "+str(l))