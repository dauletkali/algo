#!/bin/python3

import sys

def draw(board):
	for i in board:
		print(i)

def commonChild(s1, s2):
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

    draw(board)
    return board[-1][-1]

s1 = input().strip()
s2 = input().strip()
result = commonChild(s1, s2)
print(result)





