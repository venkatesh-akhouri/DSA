'''
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
A = [3, 5, 4, 2]
'''

#brute force method
import sys


def brute_force(arr):
    max_dist=-sys.maxsize
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[i]<arr[j]):
                max_dist=max(max_dist,j-i)

    print("using brute force "+str(max_dist))



arr=[3, 5, 4, 2]
arr2=[1,2,3,4,5]
brute_force(arr2)
