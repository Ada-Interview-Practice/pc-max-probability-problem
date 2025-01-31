def max_probability(n, edges, succProb, start, end):
    pass
    
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
