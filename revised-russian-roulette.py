#!/bin/python3

import sys
from collections import Counter
from math import ceil
def revisedRussianRoulette(doors):
    # Complete this function
    s = 0
    c = 0
    for (v,i) in enumerate(doors):
	    if i == 1 and v == len(doors)-1:
	    	c+=1
	    	s += ceil(c/2)
	    else:
	    	if i == 1:
	    		c+=1
	    	else:
	    		s += ceil(c/2)
	    		c=0

    co = Counter(doors)
    return [ceil(s),co[1]]



if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (" ".join(map(str, result)))