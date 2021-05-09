#first index using start index

def firstIndexBetter(arr,x,si):
    l = len(arr)
    if si == l:
        return -1
    if arr[si] == x:
        return si
    smallerListOutput = firstIndexBetter(arr,x,si+1)
    return smallerListOutput
	
#main
#from sys import setrecursionlimit
#setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndexBetter(arr, x, 0))