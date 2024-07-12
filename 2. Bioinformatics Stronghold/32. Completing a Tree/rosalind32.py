from collections import deque

def BFS(tree, visited, start, need_edge_count):
    need_v = deque()
    need_v.append(start)
    
    while (need_v):
        current_node = need_v.popleft()
        visited.append(current_node)
        next_nodes = tree[current_node]
        for i in range(len(next_nodes)):
            current_next_node = next_nodes[i]
            
            if current_next_node not in visited:
                need_v.append(current_next_node)
    
    if len(visited) != len(tree):
        need_edge_count += 1
        return False, need_edge_count
    else:
        return True, need_edge_count
                
name = input()
f = open(name, 'r')

n = int(f.readline()[:-1])
adjList = [[] for i in range(n + 1)]

for line in f.readlines():
    oneNode, otherNode = list(map(int, line.split()))
    adjList[oneNode].append(otherNode)
    adjList[otherNode].append(oneNode)

visited = [0]
res_edge_count = 0


for i in range(1, n + 1):
    if i not in visited:
        flag, res_edge_count = BFS(adjList, visited, i, res_edge_count)
        if flag:
            break

print(res_edge_count)
