import sys
n = int(sys.stdin.readline().rstrip())
array = [0]
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

d = [0] * 1001
dn = [0] * 1001

for i in range(1, n+1):
    dn[i] = [0, 0, 0]

dn[1][0] = array[1][0]
dn[1][1] = array[1][1]
dn[1][2] = array[1][2]
d[1] = min(dn[1][0], dn[1][1], dn[1][2])

for j in range(2, n+1):
    for i in range(3):    
        dn[j][i] = min(dn[j-1][(i+1)%3], dn[j-1][(i+2)%3])+array[j][i]
    d[j] = min(dn[j][0], dn[j][1], dn[j][2])

print(d[n])