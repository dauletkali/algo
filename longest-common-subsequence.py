#!/bin/python3

import sys

def draw(board):
	for i in board:
		print(i)

def longestCommonSubsequence(s1, s2):
    # Complete this function
    board = []
    board.append([0 for j in range(len(s2)+1)])
    for i in range(len(s1)):
    	board.append([0 for j in range(len(s2)+1)])

    for i in range(1, len(s1)+1):
    	for j in range(1,len(s2)+1):
    		if s1[i-1] == s2[j-1]:
    			board[i][j] = board[i-1][j-1] + 1
    		else:
    			board[i][j] = max(board[i][j-1],board[i-1][j])
    
    res = []
    longest_subsequence = board[-1][-1]
    row = -1
    column = -1
    
    while longest_subsequence > 0:
    	if a[row] == b[column]:
    		res.append(a[row])
    		row -= 1
    		column -= 1
    		longest_subsequence -= 1
    	else:
    		if board[row-1][column] > board[row][column-1]:
    			row -= 1
    		else:
    			column -= 1
    	
    return reversed(res)

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    result = longestCommonSubsequence(a, b)
    print(" ".join([str(i) for i in result]))