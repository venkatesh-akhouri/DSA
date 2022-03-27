'''
essentialy we have to find the max sum of elements in an array  BUT WE CANNOT ADD ADJACENT ELEMENTS'
'''


#DP approach
def house_robberDP(arr):
    rob1=rob2=0
    for a in arr:
        temp=max()