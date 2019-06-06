import math

def prims(adjMatrix):
    vertices = len(adjMatrix)
    tree = [0]
    weights = []
    edges = [[0 for x in range(vertices)] for x in range(vertices)]
    while len(tree) < vertices:
        minIndex = 0
        minEdge = math.inf
        minRow = 0
        # for every node in the tree
        for i in range(len(tree)):
            row = adjMatrix[tree[i]]
            # for every edge with this node
            for j in range(len(row)):
                edge = row[j]
                if edge < minEdge and j not in tree:
                    minEdge = edge
                    minRow = i
                    minIndex = j
        tree.append(minIndex)
        weights.append(minEdge)
        edges[minRow][minIndex] = minEdge

    return(sum(weights))

def readGraph():
    file = open("p107_network.txt")
    lines = file.readlines()
    numVertices = len(lines)
    edges = [[math.inf for x in range(numVertices)] for x in range(numVertices)]
    for i in range(len(lines)):
        parts = lines[i].split(",")
        for j in range(len(parts)):
            if not parts[j].strip() == '-':
                edges[i][j] = int(parts[j].strip())
                edges[j][i] = int(parts[j].strip())
    file.close()
    return edges

def sumGraph(graph):
    total = 0
    for i in range(len(graph)):
        row = graph[i]
        for j in row:
            if not j == math.inf:
                total += j
    return total/2
# graph edges with weights
# diagram of graph is shown above
graph = readGraph()

oldWeight = sumGraph(graph)
# pass the # of vertices and the graph to run prims algorithm 
newWeight = prims(graph)

print(oldWeight)
print(newWeight)
print(oldWeight-newWeight)
