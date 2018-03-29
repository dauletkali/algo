#!/bin/python3

import sys

def digitSum(n):
	# Complete this function
	if len(n) == 1:
		return n
	p = str(sum([int(k) for k in n]))
	return digitSum(p)

if __name__ == "__main__":
	n, k = input().strip().split(' ')
	n, k = [str(n), int(k)]
	s = 0
	for i in n:
		s += int(i)*k

	result = digitSum(str(s))
	print(result)