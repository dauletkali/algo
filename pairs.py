#!/bin/python3

import sys

def pairs(k, arr):
    # Complete this function
    counter = 0
    for i in arr:
    	for j in arr:
    		if abs(i-j == k):
    			counter += 1
    return counter

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(k, arr)
    print(result)