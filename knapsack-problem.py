#!/bin/python3

import sys
def draw(board):
	for i in board:
		print(i)
def unboundedKnapsack(k, arr):
    board = []
    board.append([0 for i in range(k+1)])
    for j in arr:
    	board.append([0 for i in range(k+1)])

    for i in range(1,len(arr)+1):
        el = arr[i-1]
        for j in range(1,k+1):
            if j%el == 0:
                board[i][j] = j
            elif j - el >= 0:
                if board[i][j-el] == (j - el):
                    board[i][j] = j
                else:
                    a = board[i-1][j]
                    b = el + board[i-1][j-el]
                    c = board[i][j-1]
                    board[i][j] = max(a,b,c)
            else:
                board[i][j] = board[i-1][j]
    return board[-1][-1]

if __name__ == "__main__":
    t = int(input().strip())
    res = []
    for i in range(t):
    	n, k = input().strip().split(' ')
    	n, k = [int(n), int(k)]
    	arr = list(map(int, input().strip().split(' ')))    	
    	res.append(unboundedKnapsack(k, arr))
    for i in res:
    	print(i)