def sort_selection(arr):
    for i in range(len(arr)-1):
        imin = i
        for j in range(i+1, len(arr)):
            if arr[j] <= arr[imin]:
                imin = j
        temp = arr[i]
        arr[i] = arr[imin]
        arr[imin] = temp

    return arr
# O(n*n)
print(sort_selection([9,8,7,6,5,4,3,2,1]))