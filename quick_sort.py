def partition(A, start, end):
    pivot = A[end]
    partitionIndex = start-1
    for i in range(start, end):
        if A[i] <= pivot:
            partitionIndex += 1
            A[partitionIndex], A[i] = A[i], A[partitionIndex]

    A[partitionIndex+1], A[end] = A[end], A[partitionIndex+1] 
    return partitionIndex+1

def quick_sort(A, start, end):
    if start < end:
        partitionIndex = partition(A, start,end)
        quick_sort(A, start, partitionIndex-1)
        quick_sort(A, partitionIndex+1, end)


a = [9,8,7,6,5,4,3,2,1]
quick_sort(a, 0,8)
print(a)