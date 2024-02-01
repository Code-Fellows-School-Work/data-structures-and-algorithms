# Tree Fizz Buzz
Write a function called fizz buzz tree that takes in a k-ary tree as an argument and returns a new k-ary tree.
Determine if the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure but modify the values as the following:
If the value is divisible by 3, then replace the value with "Fizz"
If the value is divisible by 5, then replace the value with "Buzz"
If the value is divisible by 3 and 5, then replace the value with "FizzBuzz"
If the value is not divisible by 3 or 5, convert the number to a string

## Whiteboard Process
[Tree Fizz Buzz](/python/docs/tree_fizz_buzz/White%20Board.png)

## Approach & Efficiency
O(n) for space and time because the algorithm has the traverse every node in the tree, determine each node value, then make a copy of the tree structure using the new node values

## Solution
Available at: [Tree Fizz Buzz](/python/code_challenges/tree_fizz_buzz.py)