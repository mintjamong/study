import sys
n = int(sys.stdin.readline().rstrip())
d = [0] * 1001

d[1] = 1
d[2] = 2
# overflow 날 수 있어서 미리 나누기
for i in range(3, n+1):
    d[i] = (d[i-1]+d[i-2])%10007

print(d[n])
