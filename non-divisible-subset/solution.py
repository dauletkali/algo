import sys

def nonDivisibleSubset(k, arr):
    # Complete this function
    map = [0,0,0,0,0,0,0,0,0,0,
    		0,0,0,0,0,0,0,0,0,0,
    		0,0,0,0,0,0,0,0,0,0,
    		0,0,0,0,0,0,0,0,0,0,
    		0,0,0,0,0,0,0,0,0,0,
    		0,0,0,0,0,0,0,0,0,0,
    		0,0,0,0,0,0,0,0,0,0,
    		0,0,0,0,0,0,0,0,0,0,
    		0,0,0,0,0,0,0,0,0,0,
    		0,0,0,0,0,0,0,0,0,0,0]
    for element in arr:
    	map[element%k] += 1
        
    res = min(map[0],1)
    for i in range(1,int(k/2)+1):
    	res += max(map[i],map[k-i])
    return res

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)
