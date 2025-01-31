from heapq import heappush, heappop
from collections import defaultdict
def max_probability(n, edges, succProb, start, end):
    # initialize list to keep track of probability to travel to node
    p = [0.0] * n
    
    # transform representation of dictionary to adjacency dictionary
    # where the key = the source node and the value is a list of tuples with (destination_node, probability of edge)
    g = defaultdict(list)
    for idx, (a, b) in enumerate(edges):
        g[a].append((b, succProb[idx]))
        g[b].append((a, succProb[idx]))

    # set the probability of the start node to 1.0
    p[start] = 1.0
    # use negative weights to denote the priority for the queue, as the
    # larger the decimal value, the higher the probability. 
    # A larger decimal will indicate a higher priority for us in this implementation of Dijkstra
    queue = [(-p[start], start)]

    # while there is something in our heap
    while queue:
        # pop off the node with the highest priority (greatest probability)
        prob, cur = heappop(queue)
        # if we have reached the end node, we can immediately return the probability calculated to travel to the node
        if cur == end:
            return -prob

        # iterate through the current node's neighbors, if it has any
        for neighbor, edgeProb in g.get(cur, []):
            # if the probability to travel to this neighbor is greater than the probability previously calculated
            if -prob * edgeProb > p[neighbor]:
                # set the new probability
                p[neighbor] = -prob * edgeProb
                # push the neighbor onto the queue
                heappush(queue, (-p[neighbor], neighbor))

    # no path was found so return 0.0
    return 0.0

### Test Case #1

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

assert max_probability(n, edges, succProb, start, end) == 0.25

### Test Case #2

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.3]
start = 0
end = 2

assert max_probability(n, edges, succProb, start, end) == 0.3

### Test Case #3

n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2

assert max_probability(n, edges, succProb, start, end) == 0.0

print("All tests passed! If time remains discuss time and space complexity")
