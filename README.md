# Max Probability Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

You are given an undirected, weighted graph of n nodes (0-indexed). The graph is represented by a list of edges where edges[i] = [a, b] is an undirected edge connecting the nodes a and b. The probability of successfully traversing that edge is represented by succProb[i].

Given two nodes, `start` and `end`, find the path with the maximum probability of success to go from `start` to `end` and return its success probablity.

If there is no path from start to end, return 0.0. 

## Examples

### Example 1

```py
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

max_probability(n, edges, succProb, start, end)
```

Produces

```py
0.25 
```

Explanation:

- To get from 0 to 2, we have two potential paths: 

  - 0 -> 1 -> 2
  - 0 -> 2
- For the first path, the probability is 0.5 * 0.5 which equals 0.25.
- The probability for the second path is 0.2.
- `0.25 > 0.2` so the first path gives us the highest probability of success.

### Example 2

```py 
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.3]
start = 0
end = 2

max_probability(n, edges, succProb, start, end)
```

Produces
```py
0.3
```

### Example 3
```py
n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2

max_probability(n, edges, succProb, start, end)
```

Produces
```py
0.0
```

## Notes for the Interviewer

### Clarifying Questions

### Q: What should I return if there is not a valid path from the start to end node?
A: You should return 0.0 if there is no valid path.

#### Q: How do the edge weights work? 
A: Edge weights are stored in an array succProb[i] where each edge weight is connected to the edge in edges[i]. So for edges[0], you will find the corresponding weight in succProb[0].

#### Q: Will the graph be connected?
A: It is not guaranteed for the graph to be connected, some nodes may be disconnected from the graph.

#### Q: How do I calculate the probability to travel to a node?
A: The probability to travel to a node is calculated by multiplying the probabilities to travel along the edges to the node. If we are traveling from A -> B -> C and the edge probability from A -> B is 0.5 and the edge probability from B -> C is 0.2, we can calculate the total probability from A -> B -> C as 0.5 * 0.2 = 0.1

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper and a very small sample graph.

- Another hint is that this problem can be solved using Dijkstra's algorithm. Remind the interviewer that the edge weights will need to be handled differently than the version of Dijkstra taught in Learn. 

- Ask the interviewer about the representation the graph is stored in. Is there a way to translate that representation to one that can be used to perform Dijkstra's algorithm?

- Remind the interviewer that the version of Dijkstra taught in Learn has us add edge weights together to determine the weight of the overall path to a node. How do probabilities differ? If they are unfamiliar, remind them that you can multiply probabilities to come up with the overall probability for an outcome. For instance, while it is a 0.5 chance to flip a coin and get Heads, you have a 0.25 chance to flip a coin and get Heads twice (0.5 * 0.5 = 0.25).

- If the interviewer has trouble coming up with a way to store the priority in the queue (heapq), remind them that the bigger a decimal for a probability is, the higher the probability. Meaning, a 0.5 probability > 0.3 probability. Thus, when storing the edge weight (probability) in the queue, they may want to consider storing the weights as negative values to ensure that the highest probability path is being considered first. 

## Optional At Home Bonus

- What are the time/space complexities of the sample solution? 

- If you performed Dijkstra's without an early termination, is there a check you can add to exit Dijkstra's early?