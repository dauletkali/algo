#!/bin/python3
from itertools import permutations
import sys

def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True

def biggerIsGreater(w):
    # Complete this function
    arr = list(w)

    np = next_permutation(arr)
    if np:
    	return ''.join(arr)

    return "no answer"

if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        w = input().strip()
        result = biggerIsGreater(w)
        print(result)
