#last index - traversing from end
def lastIndex(arr,x):
    l = len(arr)
    if l == 0:
        return -1
    if arr[-1] == x:
        return l-1
    smallerList = arr[:l-1]
    smallerListOutput = lastIndex(smallerList,x)
    if smallerListOutput == -1:
        return -1
    else:
        return smallerListOutput
# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex(arr, x))