import sys
n = int(sys.stdin.readline().rstrip())
d = [0] * (n+1)
d[1] = 0
pre = [0]*(n+1)
pre[1] = 0
for i in range(2, n+1):
    d[i] = d[i-1]+1
    pre[i] = i-1
    if i%3 == 0 and d[i] > d[i//3]+1:
        pre[i] = i//3
        d[i] = d[i//3]+1
    if i%2 == 0 and d[i] > d[i//2]+1:
        pre[i] = i//2
        d[i] = d[i//2]+1
print(d[n])
count = n
count_array = [n]
while count > 1:
    count = pre[count]
    count_array.append(count)

for i in count_array:
    print(i, end=' ')