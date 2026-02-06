#graph is non linear data structure , which is used to representation of relationship between objects.

#types of graph

#based on direction
#1.undirected graph
#2.directed graph

#based on weight
#1.unweighted graph
#2.weighted graph

#create graph using python
class Graph:
    def __init__(self):
        self.graph={}
    
    def vertex(self,vertex):
        self.graph[vertex]=[]

    def edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def display(self):
        for i in self.graph:
            print(i,'->',self.graph[i])

g = Graph()
g.vertex(0)
g.vertex(1)
g.vertex(2)
g.vertex(3)

g.edge(0, 1)
g.edge(0, 2)
g.edge(0, 3)

g.display()


#BFS
from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}
queue=deque(['A'])
visited=[]

while queue:
    node=queue.popleft()
    if node not in visited:
        print(node)
        visited.append(node)
        queue.extend(graph[node])

#DFS
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}
visit=[]
def dfs(node):
    if node not in visit:
        print(node)
        visit.append(node)
        for i in graph[node]:
            dfs(i)

dfs('A')