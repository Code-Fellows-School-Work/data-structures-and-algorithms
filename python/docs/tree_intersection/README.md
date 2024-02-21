# Tree Intersection
Write a function called tree intersection that takes two binary trees as parameters. Using hashmap implementation as part of the algorithm, return a set of values found in both trees

## Whiteboard Process
[Tree Intersection](/python/docs/tree_intersection/tree_intersection.PNG)

## Approach & Efficiency
O(n) for space and time because the algorithm traveres through the first binary tree and stores values in the set. Then the algorithm traverses through the second binary tree and compares the values to the first set and stores common values in the second set.

## Solution
Available at: [Tree Intersection](/python/code_challenges/tree_intersection.py)