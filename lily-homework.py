from math import ceil
import sys

def selectionSort(alist):
    position_map = {}
    for i in range(0,len(alist)):
        position_map[alist[i]] = i

    counter = 0
    
    s_alist = sorted(alist)

    for i in range(len(alist)):
        if alist[i] != s_alist[i]:
            counter += 1

            idx = position_map[s_alist[i]]
            position_map[alist[i]] = idx
            alist[i], alist[idx] = s_alist[i],alist[i]

    return counter

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = selectionSort(arr)
    res = selectionSort(list(reversed(arr)))
    print(min(result,res))