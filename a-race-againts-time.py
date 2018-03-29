#!/bin/python3

import sys

def draw(board):
	for i in board:
		print(i)

def raceAgainstTime(n, mason_height, heights, prices):
    # Complete this function
    board = []
    for i in range(n):
    	b = []
    	for j in range(n):
    		b.append(0)
    	board.append(b)
    draw(board)
    
if __name__ == "__main__":
    n = int(input().strip())
    mason_height = int(input().strip())
    heights = list(map(int, input().strip().split(' ')))
    prices = list(map(int, input().strip().split(' ')))
    result = raceAgainstTime(n, mason_height, heights, prices)
    print(result)