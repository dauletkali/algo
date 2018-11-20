arr = [9,8,7,6,5,4,3,2,1,0]

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) / 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    sorted=[] #array to store the sorted list
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1

    sorted+=left[i:]
    sorted+=right[j:]
    return sorted

print(merge_sort(arr))