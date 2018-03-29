#!/bin/python3

import sys

TOP = 0
BOTTOM = 1
LEFT = 2
RIGHT = 3
TOP_RIGHT = 4
TOP_LEFT = 5
BOTTOM_RIGHT = 6
BOTTOM_LEFT = 7
NONE = 8

def drawBoard(board):
    print("================")
    [print(i) for i in board]

def detectDirection(queen,obstacle):
    if queen[0] > obstacle[0] and queen[1] == obstacle[1]:
        return TOP
    if queen[0] < obstacle[0] and queen[1] == obstacle[1]:
        return BOTTOM
    if queen[0] == obstacle[0] and queen[1] < obstacle[1]:
        return RIGHT
    if queen[0] == obstacle[0] and queen[1] > obstacle[1]:
        return LEFT
    if abs(queen[0]-obstacle[0]) == abs(queen[1]-obstacle[1]):
        if queen[0] < obstacle[0] and queen[1] < obstacle[1]:
            return BOTTOM_RIGHT
        if queen[0] > obstacle[0] and queen[1] < obstacle[1]:
            return TOP_RIGHT
        if queen[0] < obstacle[0] and queen[1] > obstacle[1]:
            return BOTTOM_LEFT
        if queen[0] > obstacle[0] and queen[1] > obstacle[1]:
            return TOP_LEFT
    return NONE


def placeQueenAndObstacles(board, queen,obstacles):
    board[queen[0]][queen[1]] = "q"
    for obstacle in obstacles:
        board[obstacle[0]][obstacle[1]]="0"
    return board

def queensAttack(n, k, r_q, c_q, obstacles):
    # Complete this function
    queen = (r_q-1,c_q-1)
    #board = [[" " for i in range(n)] for i in range(n)]
    #board = placeQueenAndObstacles(board,queen,obstacles)
    
    top = queen[0]
    bottom = n - queen[0] - 1
    left = queen[1]
    right = n - queen[1] - 1

    top_left = min(top,left)
    top_right = min(top,right)
    bottom_left = min(bottom,left)
    bottom_right = min(bottom,right)

    for obstacle in obstacles:
        direction = detectDirection(queen,obstacle)
        if direction == TOP:
            top = min(top, queen[0]-obstacle[0] - 1)
        if direction == BOTTOM:
            bottom = min(bottom, obstacle[0] - queen[0] - 1)
        if direction == LEFT:
            left = min(left, queen[1] - obstacle[1] - 1)
        if direction == RIGHT:
            right = min(right, obstacle[1] - queen[1] - 1)
        if direction == TOP_LEFT:
            top_left = min(top_left, min(queen[1] - obstacle[1] - 1,queen[0] - obstacle[0] - 1))
        if direction == TOP_RIGHT:
            top_right = min(top_right, min(obstacle[1] - queen[1] - 1,queen[0] - obstacle[0] - 1))
        if direction == BOTTOM_LEFT:
            bottom_left = min(bottom_left, min(obstacle[0] - queen[0] - 1, queen[1] - obstacle[1] - 1))
        if direction == BOTTOM_RIGHT:
            bottom_right = min(bottom_right, min(obstacle[0] - queen[0] - 1, obstacle[1] - queen[1] - 1))

    # print("TOP: ", top)
    # print("BOTTOM: ", bottom)
    # print("LEFT: ", left)
    # print("RIGHT: ", right)
    # print("TOP_LEFT: ", top_left)
    # print("TOP_RIGHT: ", top_right)

    # drawBoard(board)
    return top + bottom + left + right + top_left + top_right + bottom_left + bottom_right

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)]
    obstacles = []
    for obstacles_i in range(k):
       obstacles_t = [int(obstacles_temp)-1 for obstacles_temp in input().strip().split(' ')]
       obstacles.append(obstacles_t)
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
