'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''
 #solution 1, brute force approach
 #generate sub arrays, check if sum >= target. kepp a track of length to return minimum length
import sys
def brute_force(arr,tgt):
    min_len=sys.maxsize
    for i in range(len(arr)):
        curr_sum=0
        for j in range(i,len(arr)):
            curr_sum+=arr[j]
            if(curr_sum>=tgt):
                curr_len=j-i+1
                if(curr_len<min_len):
                    min_len=curr_len
                break
    print("ans "+str(min_len))


def sliding_window(arr,tgt):
    print('starting func')
    left=right=0
    curr_sum=0
    min_len=sys.maxsize
    for right in range(len(arr)):
        curr_sum+=arr[right]
       #print("curr sum is "+str(curr_sum))
        while(curr_sum>=tgt):
            curr_len=right-left+1
            min_len=min(curr_len,min_len)
            curr_sum-=arr[left]
            left+=1

    print("sliding window: "+str(min_len))




arr=[2,3,1,2,8,3]
tgt=8
brute_force(arr,tgt)
sliding_window(arr,tgt)


