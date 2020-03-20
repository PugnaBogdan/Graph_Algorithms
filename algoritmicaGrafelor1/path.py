from rootedTree import RootedTree
import heapq

def bfs(g, startVertex):
    '''Performs a BFS in graph g starting from startVertex.
    Returns the corresponding tree.
    '''
    tree = RootedTree(startVertex)
    queue = [startVertex]
    top_of_queue = 0
    while top_of_queue < len(queue):
        vertex = queue[top_of_queue]
        top_of_queue += 1
        for outboundNeighbour in g.parseNin(vertex):
            if not tree.nodeExits(outboundNeighbour):
                queue.append(outboundNeighbour)
                tree.addChild(vertex, outboundNeighbour)
    return tree


def getPath(tree, targetVertex):
    '''Returns the path from the root of the tree to the targetVertex,
    or None if the targetVertex is not in the tree.
    '''
    if not tree.nodeExits(targetVertex):
        return None
    path = [targetVertex]
    currentVertex = targetVertex
    while tree.getParent(currentVertex) is not None:
        currentVertex = tree.getParent(currentVertex)
        path.append(currentVertex)
    path.reverse()
    return path, len(path)-1

def dijkstra(graph, cost, startVertex):
    '''Returns the tree of minimum cost paths
	'''
    queue=list()
    distance=dict()
    distance[startVertex]=0
    heapq.heappush(queue, (0, startVertex))
    tree=RootedTree(startVertex)
    while len(queue) > 0:
        dx,x=heapq.heappop(queue)
        for y in graph.parseNout(x):
            if (y not in distance.keys() or distance[y] > distance[x] + cost[(x,y)] ):
                distance[y] = distance[x] + cost[(x,y)]
                heapq.heappush(queue, (distance[y], y))
                tree.reparent(x,y)
    return tree