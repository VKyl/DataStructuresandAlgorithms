n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    edges_with = map(int, input().split())
    for vertex in edges_with:
        graph[vertex - 1].append(i+1)

print(n)
for node in graph:
    if not node:
        print(" ")
    else:
        print(" ".join(map(str, node)))