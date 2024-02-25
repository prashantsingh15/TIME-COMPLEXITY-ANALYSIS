from sys import stdin


def arrayEquilibriumIndex(arr, n) :
    n = 0
    
    i=0
    leftsum = 0
    rightsum = 0
    index=0
    while i<len(arr):
        n +=arr[i]
        i=i + 1
    # print(n)
    while index <len(arr):
        rightsum=n-leftsum-arr[index]
        if (rightsum==leftsum):
            return index

        leftsum=leftsum + arr[index]
        index=index +1
    return -1




    
 

     
   


def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1