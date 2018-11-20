def insertion_sort(arr):
    for i in range(1,len(arr)):
        pick = arr[i]
        hole = i
        while hole > 0 and arr[hole - 1] > pick:
            arr[hole]=arr[hole-1]
            arr[hole-1]=pick
            hole-=1
        arr[hole]=pick
    return arr

# O(n*n), O(n)
print(insertion_sort([0,9,8,7,6,5,4,3,2,1]))