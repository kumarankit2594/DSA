#check if number present in list
def checkNumber(arr, x):
    if arr[0] == x:
        return True
    smallerList = arr[1:]
    try: 
        if checkNumber(smallerList,x):
            return True
        else:
            return False
    except:
        return False
        
    

# Main
from sys import setrecursionlimit
#setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')