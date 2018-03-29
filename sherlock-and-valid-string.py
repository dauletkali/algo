from collections import Counter   
import sys

def isValid(s):
    char_map = Counter(s)
    occurence_map = Counter(char_map.values())
    if len(occurence_map) == 1:
        return "YES"
    if len(occurence_map) == 2:
    	d = list(occurence_map.items())
    	if d[0][1] == 1 or d[1][1] == 1 and abs(d[0][0]-d[1][0]) == 1:
    		return "YES"
    return "NO"

s = input().strip()
result = isValid(s)
print(result)