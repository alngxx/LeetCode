# An Loc LeetCode's journey
My DSA practice log, organized by topic. I work through problems ahead of software engineering internship OA.

## How I work each problem

1. **Brute force first**
2. **Push for something better** 
3. **Check the hints if stuck for 10-15 minutes** 
4. **Write the intuition in docstrings to better identify problem patterns**
```python
""" Approach: O(time), O(space)
1. Step in plain words
2. Step in plain words
3. Step in plain words
"""
... solution code
```


```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ Hashmap: O(n), O(n)
        1. Walk through nums once
        2. For each number, check if target - num was seen before
        3. If yes, return both indices; otherwise store num and its index
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
```

## Topics

| Folder | Focus |
|---|---|
| `Array & Hashing` | Hash maps, frequency counting, grouping |
| `Two Pointers` | Opposite-direction and same-direction pointer techniques |
| `Sliding Window` | Fixed-size and variable-size windows |
| `Stack & Queue` | Monotonic stacks, queue-based simulation |
| `Binary Search` | Search on sorted arrays and search spaces |
| `Linked List` | Traversal, reversal, cycle detection |
| `Tree` | DFS/BFS traversal, recursion on tree structure |
| `Graph` | BFS/DFS on grids and graphs, Dijkstra's |
| `Recursion` | Backtracking and recursive enumeration |
| `1D Dynamic Programming` | Single-sequence DP |
| `2D Dynamic Programming` | Grid and two-sequence DP |
| `Greedy` | Local-choice algorithms with proof of correctness |
| `Intervals` | Merging, scheduling, overlap problems |
| `Heap` | Priority queue-based selection problems |
| `Maths & Geometry` | Number theory, simulation, geometric reasoning |
| `Collection` | Problems that don't fit a single category above |

## Solving priorities

When more than one approach passes, I prefer, in this order:
1. The best time complexity that still fits the constraints
2. Among equal time complexity, the one using less extra space
3. Among equal complexity, the one easiest to explain out loud
