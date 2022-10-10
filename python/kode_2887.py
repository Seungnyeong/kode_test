# https://www.acmicpc.net/problem/2887


# 메모리 초과
# 크루스칼 알고리즘 최소 신장 트리
n = int(input())
li = []
for i in range(n):
    problem = list(map(int, input().split(' ')))
    li.append(problem)


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


dist_li = {}
root = list(range(n))
edge, cost = 0, 0


for i in range(n):
    for j in range(i + 1, n):
        dist_li[i, j] = min(abs(li[i][0] - li[j][0]),
                            abs(li[i][1] - li[j][1]),
                            abs(li[i][2] - li[j][2]))
                            
dist_li = sorted(dist_li.items(), key=lambda item: item[1])

for point, weight in dist_li:
    a, b = find(point[0]), find(point[1])
    if a != b:
        root[b] = a
        edge += 1
        cost += weight
    if edge == n-1:
        break

print(cost)