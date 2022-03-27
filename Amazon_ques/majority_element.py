#A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).

def majority_naive(arr):
    required_count=len(arr)//2
    for i in range(len(arr)):
        count=0
        for j in range(i,len(arr)):
            if(arr[i]==arr[j]):
                count+=1
                if(count>required_count):
                    return("majority: "+str(arr[i]))

    return("no majority element")

#hash table approach
def majority_hash(arr):
    hash_table={}
    for num in arr:
        if num not in hash_table:
            hash_table[num]=1
        else:
            hash_table[num]+=1

    for val in hash_table:
        if(hash_table[val]>calendar(arr)//2):
            return ("majority: " + str(arr[i]))

    return ("no majority element")

#moore's voting algoritm
def canBeMajority(arr):
    idx=0
    count=1
    for i in range(1,len(arr)):
        if(arr[idx]==arr[i])
            count+=1
        else:
            count-=1
        if(count==0):
            idx=i
            count=1
    return(arr[idx])

def ismajority(len):
    num=canBeMajority(arr)
    if(num>len):
        print("majority is "+)



arr=[7, 7, 7, 2, 3, 5, 7]
ans=majority_naive(arr)
print(ans)
ans2=majority_naive(arr)
print(ans2)




