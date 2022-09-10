import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
# arr에 담긴 숫자를 하나씩 뒤로 당기기
array = [0] *(n+1)
for i in range(1, n+1):
    array[i] = arr[i-1]
# count는 i와 j를 담은 2중리스트
count = []
for i in range(m):
    count.append(list(map(int, sys.stdin.readline().rstrip().split())))

# d는 i번째까지의 합
d = [0]*(n+1)
d[1] = array[1]

for i in range(2, n+1):
    d[i] = d[i-1] + array[i]
# sum은 count에 담긴 i부터 j까지의 합을 담은 리스트
sum = [0]*(m+1)
for i in range(1, m+1):
    sum[i] = d[count[i-1][1]]-d[count[i-1][0]-1]

for i in range(1, m+1):
    print(sum[i], end='\n')