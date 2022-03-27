#bottom up value as before hand we specified first two values
def fibboDP(n):
    fib_lis=[0,1]
    if(n==1):
        return(fib_lis[0])
    if(n==2):
        return(fib_lis[1])

    for i in range(2,n):
        fib_lis.append(fib_lis[i-1]+fib_lis[i-2])


    return(fib_lis[n-1])


n=int(input("enter n: "))
ans=fibboDP(n)
print(ans)