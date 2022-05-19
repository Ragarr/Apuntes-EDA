from graph import Graph
from sys import maxsize
class MyGraph(Graph):
    def __init__(self, vertices, directed=True):
        super().__init__(vertices, directed)
    
    def closer_vertex(self,visited,distances):
        min=maxsize
        for vertex in self._vertices.keys():
            if distances[vertex] <= min and visited[vertex] == False:
                min = distances[vertex]  # update the new smallest
                min_vertex = vertex  # update the index of the smallest

        return min_vertex
                
    def dijkstra(self,origin):
        distances={}
        visited={}
        previus={}
        for v in self._vertices.keys():
            distances[v]=maxsize
            visited[v]=False
            previus[v]=None
        distances[origin]=0

        for _ in self._vertices.keys():
            current=self.closer_vertex(visited,distances)
            visited[current]=True
            for e in self._vertices[current]:
                if distances[e._vertex]>distances[current]+1:
                    distances[e._vertex]=distances[current]+1
                    previus[e._vertex]=current
        
        return previus

        

    
    def minimumPath(self,start,end):
        paths=self.dijkstra(start)
        output=[]
        current=end
        while current:
            output.insert(0,current)
            current=paths[current]
        
        return output
            


labels=['A', 'B', 'C', 'D', 'E','F','G']    
# Create a given graph  
g = MyGraph(labels)  
g.addEdge('A', 'B')
g.addEdge('B', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'E')
g.addEdge('D', 'E')
g.addEdge('E', 'F')
g.addEdge('G', 'D')

print(g)

print(g.minimumPath('A','F'))
