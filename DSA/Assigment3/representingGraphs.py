from dataclasses import dataclass

class vertex:
    def __init__(self):
        self.neighbors = [] # neighbor, weight
        self.value = None

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def addVertex(self, vertexName):
        self.vertices[vertexName] = vertex()
    
    def getVertices(self):
        return self.vertices.keys()
    
    def addEdge(self, origin, dest, cost):
        self.vertices[origin].neighbors.append([dest, cost])
    
    def getEdges(self, origin):
        return self.vertices[origin].neighbors

    def clear(self):
        self.vertices = {}

class MinPriorityQueue:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return not len(self.data)

    def addWithPriority(self, elem, priority):
        self.data.append([elem, priority])

    def next(self):
        if self.isEmpty():
            return None
        min_item = min(self.data, key=lambda x: x[1])
        self.data.remove(min_item)
        return min_item[0]

    def adjustPriority(self, target, newPriority):
        for item in self.data:
            if item[0] == target:
                self.data.remove(item)
                break
        self.data.append([target, newPriority])

class maze:
    def __init__(self, size=9):
        self.size = size
        self.data = Graph()
        # Exactly 81 characters matching your visual map
        self.mazeString = '##########      S## # ######   #   ## ##### ##       ## ##### ## #T    ##########'
        
        # 1. Add all vertices with coordinates (row, col)
        for i in range(size):
            for j in range(size):
                idx = i * size + j
                self.data.addVertex((self.mazeString[idx], (i, j)))
                
        # 2. Add edges between walkable nodes
        for node in list(self.data.vertices.keys()):
            char, (r, c) = node
            if char != '#':
                directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < size and 0 <= nc < size:
                        target_idx = nr * size + nc
                        target_char = self.mazeString[target_idx]
                        if target_char != '#':
                            target_node = (target_char, (nr, nc))
                            self.data.addEdge(node, target_node, 1)

    def solve(self):
        start_node = None
        target_node = None
        for node in self.data.getVertices():
            if node[0] == 'S':
                start_node = node
            elif node[0] == 'T':
                target_node = node

        if not start_node or not target_node:
            print("Start or Target not found!")
            return

        # Dijkstra's Algorithm
        distances = {node: float('inf') for node in self.data.getVertices()}
        previous = {node: None for node in self.data.getVertices()}
        distances[start_node] = 0

        pq = MinPriorityQueue()
        pq.addWithPriority(start_node, 0)

        while not pq.isEmpty():
            current = pq.next()

            if current == target_node:
                break

            for neighbor, weight in self.data.getEdges(current):
                alt = distances[current] + weight
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    previous[neighbor] = current
                    pq.addWithPriority(neighbor, alt)

        # Reconstruct path
        path = []
        curr = target_node
        while curr and curr != start_node:
            path.append(curr)
            curr = previous[curr]
        
        # Mark path with '.' on the maze display string
        maze_chars = list(self.mazeString)
        for node in path:
            if node[0] not in ('S', 'T'):
                r, c = node[1]
                maze_chars[r * self.size + c] = '.'
        
        self.solvedString = "".join(maze_chars)

    def printMaze(self):
        display_str = self.solvedString if hasattr(self, 'solvedString') else self.mazeString
        for i in range(self.size):
            print(display_str[i * self.size : (i + 1) * self.size])

# Test the maze solver
test = maze()
test.solve()
test.printMaze()