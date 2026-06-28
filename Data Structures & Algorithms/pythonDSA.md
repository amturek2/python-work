# LeetCode Python3 Master Reference

## Table of Contents

- [Arrays](#arrays)
  - [Related Problems](#related-problems)
  - [General Ideas](#general-ideas)
  - [Common Patterns](#common-patterns)
  - [Duplicate Detection](#duplicate-detection)
  - [Frequency Counting](#frequency-counting)
  - [Complement Lookup](#complement-lookup)
  - [Encoding Strings](#encoding-strings)
  - [Useful Python Operations](#useful-python-operations)
  - [Things to Remember](#things-to-remember)
- [Two Pointers](#two-pointers)
  - [Related Problems](#related-problems-1)
  - [General Ideas](#general-ideas-1)
  - [Opposite-End Two Pointers](#opposite-end-two-pointers)
  - [Skip Invalid Characters](#skip-invalid-characters)
  - [Buy Low, Sell High Pointer Pattern](#buy-low-sell-high-pointer-pattern)
  - [Useful Python Operations](#useful-python-operations-1)
  - [Things to Remember](#things-to-remember-1)
- [Sliding Window](#sliding-window)
  - [Related Problems](#related-problems-2)
  - [General Ideas](#general-ideas-2)
  - [General Template](#general-template)
  - [Fixed-Size Window](#fixed-size-window)
  - [Variable-Size Window](#variable-size-window)
  - [Useful Python Operations](#useful-python-operations-2)
  - [Things to Remember](#things-to-remember-2)
- [Stack](#stack)
  - [Related Problems](#related-problems-3)
  - [General Ideas](#general-ideas-3)
  - [Matching Parentheses Pattern](#matching-parentheses-pattern)
  - [Core Logic](#core-logic)
  - [Useful Python Operations](#useful-python-operations-3)
  - [Things to Remember](#things-to-remember-3)
- [Binary Search](#binary-search)
  - [Related Problems](#related-problems-4)
  - [General Ideas](#general-ideas-4)
  - [Standard Iterative Pattern](#standard-iterative-pattern)
  - [Recursive Pattern](#recursive-pattern)
  - [Useful Python Operations](#useful-python-operations-4)
  - [Complexity](#complexity)
  - [Things to Remember](#things-to-remember-4)
- [Linked List](#linked-list)
  - [Related Problems](#related-problems-5)
  - [General Ideas](#general-ideas-5)
  - [Useful Operations](#useful-operations)
  - [Things to Remember](#things-to-remember-5)
- [Trees](#trees)
  - [Related Problems](#related-problems-6)
  - [General Ideas](#general-ideas-6)
  - [DFS Recursion Pattern](#dfs-recursion-pattern)
  - [BFS Level Order Pattern](#bfs-level-order-pattern)
  - [Useful Python Operations](#useful-python-operations-5)
  - [Things to Remember](#things-to-remember-6)
- [Tries](#tries)
  - [Related Problems](#related-problems-7)
  - [General Ideas](#general-ideas-7)
  - [Basic Trie Node](#basic-trie-node)
  - [Useful Python Operations](#useful-python-operations-6)
  - [Things to Remember](#things-to-remember-7)
- [Heap / Priority Queue](#heap--priority-queue)
  - [Related Problems](#related-problems-8)
  - [General Ideas](#general-ideas-8)
  - [Max Heap Trick](#max-heap-trick)
  - [Top K Pattern](#top-k-pattern)
  - [Repeatedly Remove Largest Pattern](#repeatedly-remove-largest-pattern)
  - [Scheduling with Cooldown Pattern](#scheduling-with-cooldown-pattern)
  - [Useful Python Operations](#useful-python-operations-7)
  - [Related Queue Operations for Task Scheduler](#related-queue-operations-for-task-scheduler)
  - [Related Counter Operations](#related-counter-operations)
  - [Things to Remember](#things-to-remember-8)
- [Backtracking](#backtracking)
  - [Related Problems](#related-problems-9)
  - [General Ideas](#general-ideas-9)
  - [General Template](#general-template-1)
  - [Useful Python Operations](#useful-python-operations-8)
  - [Things to Remember](#things-to-remember-9)
- [Graphs](#graphs)
  - [Related Problems](#related-problems-10)
  - [General Ideas](#general-ideas-10)
  - [BFS Pattern](#bfs-pattern)
  - [DFS Pattern](#dfs-pattern)
  - [Grid DFS Directions](#grid-dfs-directions)
  - [Useful Python Operations](#useful-python-operations-9)
  - [Things to Remember](#things-to-remember-10)
- [Advanced Graphs](#advanced-graphs)
  - [Related Problems](#related-problems-11)
  - [General Ideas](#general-ideas-11)
  - [Common Tools](#common-tools)
- [1-D Dynamic Programming](#1-d-dynamic-programming)
  - [Related Problems](#related-problems-12)
  - [General Ideas](#general-ideas-12)
  - [General Template](#general-template-2)
  - [Useful Python Operations](#useful-python-operations-10)
  - [Things to Remember](#things-to-remember-11)
- [2-D Dynamic Programming](#2-d-dynamic-programming)
  - [Related Problems](#related-problems-13)
  - [General Ideas](#general-ideas-13)
  - [General Template](#general-template-3)
  - [Useful Python Operations](#useful-python-operations-11)
  - [Watch Out](#watch-out)
- [Greedy](#greedy)
  - [Related Problems](#related-problems-14)
  - [General Ideas](#general-ideas-14)
  - [Common Greedy Patterns](#common-greedy-patterns)
  - [Useful Python Operations](#useful-python-operations-12)
- [Intervals](#intervals)
  - [Related Problems](#related-problems-15)
  - [General Ideas](#general-ideas-15)
  - [Common Interval Logic](#common-interval-logic)
  - [Useful Python Operations](#useful-python-operations-13)
  - [Things to Remember](#things-to-remember-12)
- [Math & Geometry](#math--geometry)
  - [Related Problems](#related-problems-16)
  - [General Ideas](#general-ideas-16)
  - [Useful Python Operations](#useful-python-operations-14)
- [Bit Manipulation](#bit-manipulation)
  - [Related Problems](#related-problems-17)
  - [General Ideas](#general-ideas-17)
  - [Common Bit Operations](#common-bit-operations)
  - [XOR Duplicate Cancellation Pattern](#xor-duplicate-cancellation-pattern)
  - [Things to Remember](#things-to-remember-13)
- [Master Python Library Reference](#master-python-library-reference)
  - [`heapq`](#heapq)
  - [`collections.Counter`](#collectionscounter)
  - [`collections.deque`](#collectionsdeque)
  - [Dictionary](#dictionary)
  - [Set](#set)
  - [List as Stack](#list-as-stack)
- [Pattern Recognition Cheat Sheet](#pattern-recognition-cheat-sheet)
  - [Use a Set When](#use-a-set-when)
  - [Use a Dictionary When](#use-a-dictionary-when)
  - [Use Two Pointers When](#use-two-pointers-when)
  - [Use Sliding Window When](#use-sliding-window-when)
  - [Use a Stack When](#use-a-stack-when)
  - [Use Binary Search When](#use-binary-search-when)
  - [Use a Heap When](#use-a-heap-when)
  - [Use a Queue When](#use-a-queue-when)
  - [Use Backtracking When](#use-backtracking-when)
  - [Use DP When](#use-dp-when)

This document is a reusable reference for Python3 data structures, algorithms, common patterns, useful libraries, and runtime notes from NeetCode 150.

The goal is not to store every full solution. The goal is to remember:

- What pattern each topic uses
- Which problems fit that pattern
- What Python tools are useful
- What runtime each important operation has
- How to recognize the pattern in a new problem

---

# Arrays

## Related Problems

- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Two Sum
- Encode and Decode Strings

## General Ideas

Array problems often rely on **fast lookup**, **frequency counting**, or **transforming the input into a more useful structure**.

The most common trick is to use a hash-based structure:

- Use a `set` when you only care if a value has appeared before.
- Use a `dict` when you need to map one value to another.
- Use a frequency map when you need to count occurrences.
- Use string length encoding when you need to preserve boundaries between strings.

## Common Patterns

### Duplicate Detection

Use a set to track seen values.

Core logic:

```python
seen = set()

for num in nums:
    if num in seen:
        return True
    seen.add(num)

return False
```

Use this when the question asks:

- “Does this value appear more than once?”
- “Have I seen this before?”
- “Are there duplicates?”

## Frequency Counting

Use a dictionary or `Counter` when the problem depends on counts.

Manual dictionary pattern:

```python
freq = {}

for x in items:
    freq[x] = freq.get(x, 0) + 1
```

Cleaner library pattern:

```python
from collections import Counter

freq = Counter(items)
```

Use this when the question asks:

- “Do these strings have the same characters?”
- “How many times does this appear?”
- “What is the most frequent?”
- “Are these two collections equivalent by count?”

For lowercase-letter string problems like Group Anagrams, a fixed-size count array is often better than sorting each word.

Core idea:

- Build a `26`-slot array for each word.
- Convert each character into a number index.
- Use the final count array as the dictionary key after converting it to a tuple.

Pattern:

```python
groups = {}

for word in strs:
    counts = [0] * 26

    for char in word:
        idx = ord(char) - ord("a")
        counts[idx] += 1

    key = tuple(counts)
    groups.setdefault(key, []).append(word)

return list(groups.values())
```

Character index trick:

```python
idx = ord(char) - ord("a")
```

Examples:

- `ord("a") - ord("a") = 0`
- `ord("b") - ord("a") = 1`
- `ord("z") - ord("a") = 25`

This is the cleanest way to get the number form of a lowercase character for array indexing.

## Complement Lookup

Used in Two Sum.

Instead of checking every pair, store previous numbers in a dictionary.

Core idea:

```python
need = target - num
```

If `need` was already seen, then the answer is found.

Pattern:

```python
valToIndex = {}

for i, num in enumerate(nums):
    need = target - num

    if need in valToIndex:
        return [valToIndex[need], i]

    valToIndex[num] = i
```

Use this when the problem asks for:

- Two values that add to a target
- A matching pair
- A previous value that completes the current value

## Encoding Strings

For Encode and Decode Strings, use a length prefix so the decoder knows exactly how many characters to read.

Format:

```text
length#word
```

Example:

```text
4#leet4#code
```

This is better than only using a separator because the original string may contain the separator.

## Useful Python Operations

| Operation                | Use                            | Runtime                           |
| ------------------------ | ------------------------------ | --------------------------------- |
| `set()`                  | Create empty set               | O(1)                              |
| `x in seen`              | Check membership in set        | Average O(1)                      |
| `seen.add(x)`            | Add value to set               | Average O(1)                      |
| `{}`                     | Create empty dictionary        | O(1)                              |
| `key in dict`            | Check if key exists            | Average O(1)                      |
| `dict[key] = value`      | Insert or update value         | Average O(1)                      |
| `dict.get(key, default)` | Safely get value               | Average O(1)                      |
| `Counter(items)`         | Count frequencies              | O(n)                              |
| `enumerate(nums)`        | Loop with index and value      | O(n) total                        |
| `len(s)`                 | Get length                     | O(1)                              |
| `ord(char)`              | Convert char to Unicode number | O(1)                              |
| `ord(char) - ord("a")`   | Map lowercase char to `0..25`  | O(1)                              |
| `s[i:j]`                 | Slice string                   | O(k), where k is slice length     |
| `int(s)`                 | Convert string to integer      | O(d), where d is number of digits |
| `str(num)`               | Convert number to string       | O(d), where d is number of digits |

## Things to Remember

- A set answers: “Have I seen this?”
- A dictionary answers: “What value is associated with this key?”
- A frequency map answers: “How many times did this appear?”
- For lowercase English letters, a `26`-length array is a compact frequency map.
- Convert a character to an array index with `ord(char) - ord("a")`.
- A list cannot be a dictionary key, but `tuple(counts)` can.
- For strings, slicing creates a new string, so it costs O(k).
- `Counter` is cleaner than manually writing count logic, but manual dictionaries are good practice.

---

# Two Pointers

## Related Problems

- Valid Palindrome
- Best Time to Buy and Sell Stock

## General Ideas

Two pointer problems use two indexes to scan the input more intelligently than a nested loop.

Common forms:

- One pointer at the beginning and one at the end
- One slow pointer and one fast pointer
- One pointer tracking the best position so far, while the other explores

## Opposite-End Two Pointers

Used in Valid Palindrome.

Core idea:

```python
l, r = 0, len(s) - 1
```

Compare both ends. If they match, move inward.

```python
l += 1
r -= 1
```

Use this when the problem involves:

- Palindromes
- Symmetry
- Comparing front and back
- Sorted arrays where pairs may exist

## Skip Invalid Characters

For Valid Palindrome, skip characters that are not letters or numbers.

Useful operation:

```python
c.isalnum()
```

Cleaner than writing:

```python
c.isalpha() or c.isnumeric()
```

## Buy Low, Sell High Pointer Pattern

Used in Best Time to Buy and Sell Stock.

The left pointer represents the best buying day so far.

The right pointer represents the current selling day.

Core idea:

```python
if prices[r] < prices[l]:
    l = r
else:
    maxProfit = max(maxProfit, prices[r] - prices[l])
```

Use this when:

- You need a best earlier value
- The order matters
- You need to compare current value to the best previous value

## Useful Python Operations

| Operation       | Use                         | Runtime |
| --------------- | --------------------------- | ------- |
| `s.lower()`     | Convert string to lowercase | O(n)    |
| `c.isalnum()`   | Check if letter or number   | O(1)    |
| `c.isalpha()`   | Check if letter             | O(1)    |
| `c.isnumeric()` | Check if number             | O(1)    |
| `s[i]`          | Index string                | O(1)    |
| `nums[i]`       | Index list                  | O(1)    |
| `max(a, b)`     | Get larger value            | O(1)    |
| `min(a, b)`     | Get smaller value           | O(1)    |

## Things to Remember

- Two pointers are often O(n) because each pointer moves through the input at most once.
- If the input is sorted, two pointers often replace a nested loop.
- For palindrome problems, try to avoid creating a cleaned copy if O(1) space is required.
- For stock problems, the buy pointer must always come before the sell pointer.

---

# Sliding Window

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Best Time to Buy and Sell Stock
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Permutation in String
- Minimum Window Substring
- Sliding Window Maximum

## General Ideas

Sliding window is used for **contiguous subarrays** or **contiguous substrings**.

The window usually has:

```python
l = 0
```

and a right pointer that expands:

```python
for r in range(len(nums)):
```

The pattern is:

1. Add the right value to the window.
2. Check if the window is invalid.
3. Shrink from the left until valid.
4. Update the answer.

## General Template

```python
l = 0

for r in range(len(nums)):
    # add nums[r] to window

    while window_is_invalid:
        # remove nums[l] from window
        l += 1

    # update result
```

## Fixed-Size Window

Use when the problem says size `k`.

Example logic:

```python
window_sum += nums[r]

if r >= k:
    window_sum -= nums[r - k]
```

## Variable-Size Window

Use when the problem asks for longest, shortest, or most optimal valid window.

Examples:

- Longest substring without duplicates
- Minimum substring containing all required characters
- Longest valid replacement window

## Useful Python Operations

| Operation          | Use                        | Runtime      |
| ------------------ | -------------------------- | ------------ |
| `dict.get(key, 0)` | Track counts in window     | Average O(1) |
| `set.add(x)`       | Track unique values        | Average O(1) |
| `set.remove(x)`    | Remove from window         | Average O(1) |
| `max(a, b)`        | Update longest/best result | O(1)         |

## Things to Remember

- Sliding window only works when the problem is about contiguous elements.
- The right pointer usually expands every loop.
- The left pointer only moves when the window becomes invalid.
- Most sliding window problems are O(n), not O(n²), because each pointer moves forward at most n times.

---

# Stack

## Related Problems

- Valid Parentheses

## General Ideas

A stack is useful when the most recent thing must be handled first.

This is called LIFO:

```text
Last In, First Out
```

## Matching Parentheses Pattern

Use a dictionary to map closing brackets to opening brackets.

```python
pairs = {
    ")": "(",
    "}": "{",
    "]": "["
}
```

Use a stack to store opening brackets.

When a closing bracket appears, it must match the top of the stack.

## Core Logic

```python
if c in pairs:
    if stack and stack[-1] == pairs[c]:
        stack.pop()
    else:
        return False
else:
    stack.append(c)
```

## Useful Python Operations

| Operation         | Use               | Runtime        |
| ----------------- | ----------------- | -------------- |
| `stack = []`      | Use list as stack | O(1)           |
| `stack.append(x)` | Push onto stack   | Amortized O(1) |
| `stack.pop()`     | Pop from stack    | O(1)           |
| `stack[-1]`       | Peek top value    | O(1)           |
| `if stack:`       | Check if nonempty | O(1)           |
| `len(stack)`      | Get stack size    | O(1)           |

## Things to Remember

Use a stack when problems involve:

- Parentheses
- Matching pairs
- Nested expressions
- Reversing order
- Undo behavior
- Monotonic increasing/decreasing logic

---

# Binary Search

## Related Problems

- Binary Search

## General Ideas

Binary search is used when the input is sorted or when the answer space is monotonic.

At each step, binary search eliminates half of the possibilities.

## Standard Iterative Pattern

```python
l, r = 0, len(nums) - 1

while l <= r:
    mid = (l + r) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1

return -1
```

## Recursive Pattern

```python
def binsearch(nums, l, r, target):
    if l > r:
        return -1

    mid = (l + r) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binsearch(nums, mid + 1, r, target)
    else:
        return binsearch(nums, l, mid - 1, target)
```

## Useful Python Operations

| Operation          | Use                 | Runtime              |
| ------------------ | ------------------- | -------------------- |
| `(l + r) // 2`     | Integer midpoint    | O(1)                 |
| `nums[mid]`        | Access middle value | O(1)                 |
| Function recursion | Recursive calls     | O(log n) calls total |

## Complexity

Iterative:

- Time: O(log n)
- Space: O(1)

Recursive:

- Time: O(log n)
- Space: O(log n)

## Things to Remember

Binary search works when:

- The array is sorted.
- You can discard half the search space.
- The condition changes from false to true at some point.
- The answer space is monotonic.

Watch out for infinite loops. Usually, after checking `mid`, move past it:

```python
l = mid + 1
r = mid - 1
```

---

# Linked List

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Reorder List
- Remove Nth Node From End of List

## General Ideas

Linked list problems are about changing pointers, not shifting values.

Common pointer names:

```python
prev
curr
next_node
slow
fast
dummy
```

## Useful Operations

| Operation             | Use               | Runtime |
| --------------------- | ----------------- | ------- |
| `curr.next`           | Access next node  | O(1)    |
| `curr.next = node`    | Rewire pointer    | O(1)    |
| `dummy = ListNode(0)` | Fake starter node | O(1)    |

## Things to Remember

- Use a dummy node when the head might change.
- Use slow and fast pointers for cycle detection or finding the middle.
- Always save `next_node` before changing `curr.next`.

---

# Trees

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Invert Binary Tree
- Maximum Depth of Binary Tree
- Diameter of Binary Tree
- Balanced Binary Tree
- Same Tree
- Subtree of Another Tree
- Binary Tree Level Order Traversal
- Validate Binary Search Tree

## General Ideas

Trees usually use DFS or BFS.

DFS is often recursive.

BFS usually uses a queue.

## DFS Recursion Pattern

```python
def dfs(root):
    if not root:
        return

    dfs(root.left)
    dfs(root.right)
```

## BFS Level Order Pattern

```python
from collections import deque

q = deque([root])

while q:
    node = q.popleft()

    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)
```

## Useful Python Operations

| Operation       | Use                      | Runtime |
| --------------- | ------------------------ | ------- |
| `if not root`   | Base case for empty node | O(1)    |
| `root.left`     | Access left child        | O(1)    |
| `root.right`    | Access right child       | O(1)    |
| `deque([root])` | Create queue with root   | O(1)    |
| `q.popleft()`   | Pop from front           | O(1)    |

## Things to Remember

DFS is useful for:

- Depth
- Height
- Path problems
- Recursive comparisons

BFS is useful for:

- Level order
- Shortest path in unweighted tree/graph
- Processing nodes by distance from root

---

# Tries

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Implement Trie
- Design Add and Search Words Data Structure
- Word Search II

## General Ideas

A trie is a tree for characters.

It is useful when problems involve:

- Prefixes
- Word search
- Autocomplete
- Dictionary matching

## Basic Trie Node

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
```

## Useful Python Operations

| Operation                          | Use                  | Runtime      |
| ---------------------------------- | -------------------- | ------------ |
| `char in node.children`            | Check if path exists | Average O(1) |
| `node.children[char] = TrieNode()` | Create new child     | Average O(1) |
| `node = node.children[char]`       | Move to child node   | Average O(1) |

## Things to Remember

- A trie trades memory for fast prefix lookup.
- Search runtime is O(length of word), not O(number of words).
- Use `endOfWord` to distinguish full words from prefixes.

---

# Heap / Priority Queue

## Related Problems

- Kth Largest Element in a Stream
- Last Stone Weight
- Task Scheduler

## General Ideas

A heap is used when you repeatedly need the smallest or largest available item.

Python’s heap library is:

```python
import heapq
```

Python heaps are min-heaps by default.

That means:

```python
heap[0]
```

is always the smallest value.

## Max Heap Trick

To simulate a max heap, store negative values.

```python
heapq.heappush(heap, -num)
largest = -heapq.heappop(heap)
```

This works because the largest positive number becomes the smallest negative number.

## Top K Pattern

For Kth Largest Element in a Stream, the best pattern is usually a min-heap of size `k`.

The heap stores the k largest values seen so far.

The smallest value inside that heap is the kth largest overall.

```python
heap[0]
```

is the kth largest.

## Repeatedly Remove Largest Pattern

For Last Stone Weight, use a max heap because each step needs the two largest stones.

Since Python has a min-heap, use negative values.

## Scheduling with Cooldown Pattern

For Task Scheduler, use:

- A heap for the task with highest remaining count
- A queue for tasks waiting on cooldown

This combines priority selection with time-based waiting.

## Useful Python Operations

| Operation                  | Use                              | Runtime    |
| -------------------------- | -------------------------------- | ---------- |
| `heapq.heappush(heap, x)`  | Push value into heap             | O(log n)   |
| `heapq.heappop(heap)`      | Remove and return smallest value | O(log n)   |
| `heap[0]`                  | Peek smallest value              | O(1)       |
| `heapq.heapify(nums)`      | Convert list into heap           | O(n)       |
| `heapq.nsmallest(k, nums)` | Return k smallest values         | O(n log k) |
| `heapq.nlargest(k, nums)`  | Return k largest values          | O(n log k) |

## Related Queue Operations for Task Scheduler

```python
from collections import deque
```

| Operation     | Use               | Runtime |
| ------------- | ----------------- | ------- |
| `deque()`     | Create queue      | O(1)    |
| `q.append(x)` | Add to back       | O(1)    |
| `q.popleft()` | Remove from front | O(1)    |
| `q[0]`        | Peek front        | O(1)    |

## Related Counter Operations

```python
from collections import Counter
```

| Operation          | Use                          | Runtime |
| ------------------ | ---------------------------- | ------- |
| `Counter(tasks)`   | Count frequencies            | O(n)    |
| `counter.items()`  | Loop through key-value pairs | O(k)    |
| `counter.values()` | Get counts                   | O(k)    |

## Things to Remember

Use a heap when the problem says or implies:

- kth largest
- kth smallest
- top k
- repeatedly take min/max
- priority queue
- schedule highest priority task
- merge sorted lists

For kth largest, do not always use a max heap. A min-heap of size `k` is often better.

---

# Backtracking

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Subsets
- Combination Sum
- Permutations
- Subsets II
- Word Search
- Palindrome Partitioning
- N-Queens

## General Ideas

Backtracking is used when you need to explore all possible choices.

The basic structure is:

1. Choose
2. Explore
3. Undo the choice

## General Template

```python
res = []

def backtrack(path):
    if done:
        res.append(path.copy())
        return

    for choice in choices:
        path.append(choice)
        backtrack(path)
        path.pop()
```

## Useful Python Operations

| Operation                 | Use                | Runtime |
| ------------------------- | ------------------ | ------- |
| `path.append(x)`          | Choose             | O(1)    |
| `path.pop()`              | Undo choice        | O(1)    |
| `path.copy()`             | Save current path  | O(k)    |
| `res.append(path.copy())` | Store one solution | O(k)    |

## Things to Remember

Use backtracking when:

- You need all combinations
- You need all permutations
- You need all subsets
- You need to try paths and undo choices
- The problem asks for “all possible” results

---

# Graphs

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Number of Islands
- Clone Graph
- Max Area of Island
- Pacific Atlantic Water Flow
- Course Schedule
- Rotting Oranges
- Walls and Gates

## General Ideas

Graphs are made of nodes and edges.

Common graph representations:

```python
adj = {}
```

or for grids:

```python
grid[r][c]
```

## BFS Pattern

Use BFS when exploring by distance or level.

```python
from collections import deque

q = deque()
visited = set()

q.append(start)
visited.add(start)

while q:
    node = q.popleft()

    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            q.append(nei)
```

## DFS Pattern

Use DFS when exploring as far as possible before backtracking.

```python
visited = set()

def dfs(node):
    if node in visited:
        return

    visited.add(node)

    for nei in graph[node]:
        dfs(nei)
```

## Grid DFS Directions

```python
directions = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]
```

## Useful Python Operations

| Operation           | Use                 | Runtime      |
| ------------------- | ------------------- | ------------ |
| `set()`             | Track visited nodes | O(1)         |
| `visited.add(node)` | Mark visited        | Average O(1) |
| `node in visited`   | Check if visited    | Average O(1) |
| `deque()`           | BFS queue           | O(1)         |
| `q.append(x)`       | Enqueue             | O(1)         |
| `q.popleft()`       | Dequeue             | O(1)         |

## Things to Remember

Use BFS for:

- Shortest path in unweighted graphs
- Level-by-level spread
- Rotting oranges style problems

Use DFS for:

- Connected components
- Island problems
- Cycle detection
- Recursive exploration

---

# Advanced Graphs

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Reconstruct Itinerary
- Min Cost to Connect All Points
- Network Delay Time
- Swim in Rising Water
- Alien Dictionary
- Cheapest Flights Within K Stops

## General Ideas

Advanced graph problems usually involve specialized algorithms.

Important patterns:

- Dijkstra’s algorithm
- Union Find
- Topological Sort
- Minimum Spanning Tree
- Backtracking with graph edges

## Common Tools

| Tool          | Use                                    |
| ------------- | -------------------------------------- |
| Heap          | Dijkstra / shortest path               |
| Union Find    | Connected components / cycle detection |
| DFS           | Topological sort / cycle detection     |
| BFS           | Shortest path with equal weights       |
| Sorting edges | Kruskal’s MST                          |

---

# 1-D Dynamic Programming

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Climbing Stairs
- Min Cost Climbing Stairs
- House Robber
- House Robber II
- Longest Palindromic Substring
- Palindromic Substrings
- Decode Ways
- Coin Change
- Maximum Product Subarray
- Word Break
- Longest Increasing Subsequence

## General Ideas

Dynamic programming is used when a problem can be broken into smaller overlapping subproblems.

1-D DP usually means:

```python
dp[i]
```

represents the answer up to index `i`.

## General Template

```python
dp = [0] * (n + 1)

dp[0] = base_case

for i in range(1, n + 1):
    dp[i] = recurrence

return dp[n]
```

## Useful Python Operations

| Operation   | Use                 | Runtime |
| ----------- | ------------------- | ------- |
| `[0] * n`   | Create DP array     | O(n)    |
| `dp[i]`     | Access state        | O(1)    |
| `max(a, b)` | Choose best option  | O(1)    |
| `min(a, b)` | Choose minimum cost | O(1)    |

## Things to Remember

Use DP when:

- Choices repeat
- Brute force recomputes the same states
- The answer depends on previous answers
- The problem asks for count, min, max, or possibility

---

# 2-D Dynamic Programming

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Unique Paths
- Longest Common Subsequence
- Best Time to Buy and Sell Stock with Cooldown
- Coin Change II
- Target Sum
- Interleaving String
- Longest Increasing Path in a Matrix
- Distinct Subsequences
- Edit Distance

## General Ideas

2-D DP is used when the state depends on two variables.

Examples:

- Two indexes
- Row and column
- Two strings
- Current index and remaining amount

## General Template

```python
dp = [[0] * cols for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        dp[r][c] = recurrence
```

## Useful Python Operations

| Operation                           | Use                 | Runtime         |
| ----------------------------------- | ------------------- | --------------- |
| `[[0] * cols for _ in range(rows)]` | Create 2-D DP table | O(rows \* cols) |
| `dp[r][c]`                          | Access cell         | O(1)            |

## Watch Out

Do not create a 2-D list like this:

```python
dp = [[0] * cols] * rows
```

This creates repeated references to the same row.

Use this instead:

```python
dp = [[0] * cols for _ in range(rows)]
```

---

# Greedy

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Maximum Subarray
- Jump Game
- Jump Game II
- Gas Station
- Hand of Straights
- Merge Triplets to Form Target Triplet
- Partition Labels
- Valid Parenthesis String

## General Ideas

Greedy means making the best local choice at each step.

A greedy solution works when the local best choice leads to the global best answer.

## Common Greedy Patterns

- Track max reachable index
- Track current best answer
- Sort first, then choose locally
- Use min or max as you scan
- Use intervals to make earliest/latest decisions

## Useful Python Operations

| Operation      | Use                  | Runtime    |
| -------------- | -------------------- | ---------- |
| `max(a, b)`    | Track best value     | O(1)       |
| `min(a, b)`    | Track smallest value | O(1)       |
| `nums.sort()`  | Sort in place        | O(n log n) |
| `sorted(nums)` | Return sorted copy   | O(n log n) |

---

# Intervals

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Insert Interval
- Merge Intervals
- Non-overlapping Intervals
- Meeting Rooms
- Meeting Rooms II
- Minimum Interval to Include Each Query

## General Ideas

Interval problems usually start by sorting by start time.

```python
intervals.sort(key=lambda x: x[0])
```

After sorting, compare the current interval with the previous interval.

## Common Interval Logic

Two intervals overlap if:

```python
current_start <= previous_end
```

They do not overlap if:

```python
current_start > previous_end
```

## Useful Python Operations

| Operation              | Use                 | Runtime        |
| ---------------------- | ------------------- | -------------- |
| `intervals.sort()`     | Sort in place       | O(n log n)     |
| `sorted(intervals)`    | Return sorted copy  | O(n log n)     |
| `key=lambda x: x[0]`   | Sort by start time  | O(1) per item  |
| `res.append(interval)` | Add merged interval | Amortized O(1) |

## Things to Remember

Sort first.

Then ask:

- Do these intervals overlap?
- Should I merge them?
- Should I count a conflict?
- Should I keep the one that ends earlier?

---

# Math & Geometry

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Happy Number
- Plus One
- Rotate Image
- Spiral Matrix
- Set Matrix Zeroes
- Pow(x, n)
- Multiply Strings
- Detect Squares

## General Ideas

Math and geometry problems usually require careful implementation.

Common themes:

- Modulo
- Division
- Coordinates
- Matrix traversal
- Rotations
- Hash maps for counting points

## Useful Python Operations

| Operation      | Use                            | Runtime  |
| -------------- | ------------------------------ | -------- |
| `abs(x)`       | Absolute value                 | O(1)     |
| `sum(nums)`    | Sum values                     | O(n)     |
| `pow(a, b)`    | Exponentiation                 | O(log b) |
| `a % b`        | Remainder                      | O(1)     |
| `a // b`       | Integer division               | O(1)     |
| `divmod(a, b)` | Returns quotient and remainder | O(1)     |

---

# Bit Manipulation

## Related Problems

None completed yet.

Common NeetCode problems in this section:

- Single Number
- Number of 1 Bits
- Counting Bits
- Reverse Bits
- Missing Number
- Sum of Two Integers
- Reverse Integer

## General Ideas

Bit manipulation works directly with binary representation.

The most important idea is that XOR cancels equal values.

## Common Bit Operations

| Operation | Meaning      |            |
| --------- | ------------ | ---------- |
| `x & y`   | Bitwise AND  |            |
| `x        | y`           | Bitwise OR |
| `x ^ y`   | Bitwise XOR  |            |
| `~x`      | Bitwise NOT  |            |
| `x << 1`  | Shift left   |            |
| `x >> 1`  | Shift right  |            |
| `x & 1`   | Check if odd |            |
| `x ^ x`   | Equals 0     |            |
| `x ^ 0`   | Equals x     |            |

## XOR Duplicate Cancellation Pattern

Useful when every number appears twice except one.

```python
res = 0

for num in nums:
    res ^= num

return res
```

## Things to Remember

- XOR cancels duplicates.
- AND can check whether a bit is turned on.
- Shifting left multiplies by 2.
- Shifting right divides by 2 using integer division behavior.

---

# Master Python Library Reference

## `heapq`

```python
import heapq
```

| Function                   | Use                    | Runtime    |
| -------------------------- | ---------------------- | ---------- |
| `heapq.heappush(heap, x)`  | Push item into heap    | O(log n)   |
| `heapq.heappop(heap)`      | Pop smallest item      | O(log n)   |
| `heapq.heapify(nums)`      | Convert list into heap | O(n)       |
| `heapq.nsmallest(k, nums)` | Return k smallest      | O(n log k) |
| `heapq.nlargest(k, nums)`  | Return k largest       | O(n log k) |

## `collections.Counter`

```python
from collections import Counter
```

| Function           | Use               | Runtime |
| ------------------ | ----------------- | ------- |
| `Counter(items)`   | Count frequencies | O(n)    |
| `counter.items()`  | Key-value pairs   | O(k)    |
| `counter.keys()`   | Unique keys       | O(k)    |
| `counter.values()` | Counts            | O(k)    |

## `collections.deque`

```python
from collections import deque
```

| Function          | Use               | Runtime |
| ----------------- | ----------------- | ------- |
| `deque()`         | Create deque      | O(1)    |
| `q.append(x)`     | Add to right      | O(1)    |
| `q.appendleft(x)` | Add to left       | O(1)    |
| `q.pop()`         | Remove from right | O(1)    |
| `q.popleft()`     | Remove from left  | O(1)    |
| `q[0]`            | Peek front        | O(1)    |

## Dictionary

| Operation                | Use              | Runtime      |
| ------------------------ | ---------------- | ------------ |
| `{}`                     | Empty dictionary | O(1)         |
| `key in dict`            | Check key        | Average O(1) |
| `dict[key]`              | Get value        | Average O(1) |
| `dict[key] = value`      | Insert/update    | Average O(1) |
| `dict.get(key, default)` | Safe get         | Average O(1) |
| `dict.items()`           | Key-value pairs  | O(n)         |

## Set

| Operation         | Use                               | Runtime      |
| ----------------- | --------------------------------- | ------------ |
| `set()`           | Empty set                         | O(1)         |
| `x in seen`       | Membership check                  | Average O(1) |
| `seen.add(x)`     | Add value                         | Average O(1) |
| `seen.remove(x)`  | Remove value, errors if missing   | Average O(1) |
| `seen.discard(x)` | Remove value, no error if missing | Average O(1) |

## List as Stack

| Operation         | Use          | Runtime        |
| ----------------- | ------------ | -------------- |
| `stack.append(x)` | Push         | Amortized O(1) |
| `stack.pop()`     | Pop from end | O(1)           |
| `stack[-1]`       | Peek top     | O(1)           |
| `len(stack)`      | Stack size   | O(1)           |

---

# Pattern Recognition Cheat Sheet

## Use a Set When

- You need fast membership lookup.
- You need to detect duplicates.
- You only care whether something exists.

## Use a Dictionary When

- You need to map values to indices.
- You need frequency counts.
- You need to look up complements.
- You need key-value relationships.

## Use Two Pointers When

- You compare values from both ends.
- You need a pair in a sorted array.
- You need to track a buy/sell position.
- You can move pointers inward or forward instead of using nested loops.

## Use Sliding Window When

- The problem is about contiguous subarrays or substrings.
- You need the longest or shortest valid window.
- You can update the window as it expands and shrinks.

## Use a Stack When

- The most recent item matters first.
- The problem has nested structure.
- You need to match opening and closing symbols.
- You need monotonic increasing/decreasing behavior.

## Use Binary Search When

- The input is sorted.
- You can eliminate half the options.
- The answer space is monotonic.

## Use a Heap When

- You need top k.
- You repeatedly need the smallest or largest value.
- You need priority-based processing.
- You need efficient scheduling by priority.

## Use a Queue When

- You need first-in, first-out behavior.
- You are doing BFS.
- Items become available in time order.

## Use Backtracking When

- You need all combinations, subsets, permutations, or paths.
- You make a choice, explore it, then undo it.

## Use DP When

- The problem has overlapping subproblems.
- The answer depends on previous answers.
- The problem asks for a max, min, count, or boolean possibility.

---
