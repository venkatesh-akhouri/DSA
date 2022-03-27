'''You are climbing a stair case and it takes A steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

#dynamic programming approach without array
def no_ways(n):
    res=-1
    last,slast=1,1
    for i in range(n-1):
        res=last+slast
        last=slast
        slast=res

    return(res)

def no_ways_arr(n):
     arr=[-1]*(n+1)
     arr[-1],arr[-2]=1,1
     i=n-2
     while(i>=0):
         arr[i]=arr[i+1]+arr[i+2]
         i=i-1
     return(arr[0])




ans=no_ways(5)
print(ans)
ans2=no_ways_arr(5)
print("array method se "+str(ans2))
