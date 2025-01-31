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

