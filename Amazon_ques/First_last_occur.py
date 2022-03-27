#given a sorted array find the first and last occurence of a number
'''Input : arr[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}
        x = 5
Output : First Occurrence = 2
         Last Occurrence = 5'''


def first_last(arr,x):
    f=-1
    last=-1
    for i in range(len(arr)):
        if(x==arr[i]):
            if (f==-1):
                f=i
            last=i

    print("first: "+str(f))
    print("last "+str(last))




arr=[1, 3, 5, 5, 5, 5, 67, 123, 125]
first_last(arr,5)


