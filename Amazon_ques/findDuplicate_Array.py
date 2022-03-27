'''Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.
Sample Input:

[3 1 1 4 1]

Sample Output:

1

If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1'''

def findDuplicates(arr):
    arr.sort()
    for i in range(1,len(arr)):
        if(arr[i]==arr[i-1]):
            return(arr[i])


    return(-1)


arr=[3,4,2,6,1]
ans=findDuplicates(arr)
print(ans)