'''
Given an array of integers,  sort the array into a wave like array and return it,

In other words, arrange the elements into a sequence such that  a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
'''

#sort the array and swap the adjacent elements
def wave_array(arr):
    arr.sort()

    for i in range(0,len(arr),2):
        arr[i],arr[i+1]=arr[i+1],arr[i]

    print(arr)


arr=[1,2,3,4]
arr2=[10, 5, 6, 3, 2, 20, 100, 80]
wave_array(arr2)


#the catch here is the odd idx element should be small than its adjacent even idx element(both)
#traverse only odd indoces

def wave_arr2(arr):
    for i in range(1,len(arr),2):
        if(arr[i]>arr[i+1]):

