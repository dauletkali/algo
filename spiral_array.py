
arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

def print_spiral(A,i,j):
    t = 0
    r = j-1
    l = 0
    b = i-1
    dir = 0

    while t <= b and l <= r:
        if dir == 0:
            for k in range(l,r+1):
                print(A[t][k])
            t+=1
        elif dir == 1:
            for k in range(t, b+1):
                print(A[k][r])
            r-=1
        elif dir == 2:
            for k in range(r,l-1,-1):
                print(A[b][k])
            b-=1
        elif dir == 3:
            for k in range(b,t-1,-1):
                print(A[k][l])
            l+=1
        dir = (dir+1)%4
            

print_spiral(arr,4,4)