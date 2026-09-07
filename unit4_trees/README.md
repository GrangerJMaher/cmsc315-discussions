# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

# Code Documentation

## Project Overview

This project implemented a Binary Search Tree (BST) in Python. It demonstrated recursive insertion, searching, in-order traversal, and a visual tree display. It also demonstrated several edge cases, including traversing and searching an empty tree and attempting to insert a duplicate value.

## Classes

### Node

The `Node` class represented one node in the binary search tree. Each node stored:

- A value
- A reference to its left child
- A reference to its right child

Both child references were initialized to `None`, so each new node began as a leaf node.

### BST

The `BST` class represented the complete binary search tree. Its `root` variable was initialized to `None` because a new tree did not contain any nodes.

## Methods

### `insert(value)`

The `insert()` method inserted a value into the tree by calling the recursive helper method.

Smaller values were placed in the left subtree, while larger values were placed in the right subtree. This ordering allowed the tree to reduce the possible search area after each comparison.

### `_insert_recursive(node, value)`

The `_insert_recursive()` method performed the recursive insertion.

When the method reached `None`, it found an available position and created a new node. It then returned the new node so that the parent node could store the correct child reference.

If the value was smaller than the current node's value, the method continued into the left subtree. If the value was larger, it continued into the right subtree.

Duplicate values were ignored, so each value appeared only once in the tree.

### `search(value)`

The `search()` method searched for a value by calling the recursive search helper.

A BST search was often more efficient than a linear search because each comparison eliminated an entire subtree from consideration.

### `_search_recursive(node, value)`

The `_search_recursive()` method returned `True` when it found the requested value.

It returned `False` when it reached `None`, because reaching an empty position meant that the value was not stored in the tree.

When the requested value was smaller than the current value, the method searched the left subtree. When it was larger, the method searched the right subtree.

### `inorder()`

The `inorder()` method created an empty list, called the recursive traversal helper, and returned the completed list.

### `_inorder_recursive(node, values)`

The `_inorder_recursive()` method visited the tree in the following order:

1. Left subtree
2. Current node
3. Right subtree

This traversal produced sorted output because smaller values were stored on the left and larger values were stored on the right.

### `print_tree()`

The `print_tree()` method printed the formatted string returned by `tree_to_string()`.

### `tree_to_string()`

The `tree_to_string()` method returned the tree as a multi-line string.

If the tree was empty, it returned:

```text
(empty tree)
```

### `_tree_lines(node)`

The `_tree_lines()` method recursively formatted the tree using brackets, underscores, forward slashes, backslashes, and spaces.

For the values used in this project, the displayed tree represented this structure:

```text
        [50]
       /    \
    [30]    [70]
    /  \    /  \
 [20] [40] [60] [80]
```

The exact spacing depended on the formatting calculations performed by the method.

## Tree Construction

The program created a `BST` object and inserted the following values:

```python
[50, 30, 70, 20, 40, 60, 80]
```

The resulting tree contained values in both its left and right subtrees.

The value `50` became the root. Values smaller than `50` were placed in its left subtree, while values larger than `50` were placed in its right subtree.

## In-Order Traversal

The in-order traversal produced:

```python
[20, 30, 40, 50, 60, 70, 80]
```

The output was sorted because the traversal visited the left subtree, the current node, and then the right subtree.

## Search Tests

The program searched for two values that existed and two values that did not exist.

| Search value | Result | Explanation |
|---:|:---:|---|
| `20` | Found | The value had been inserted into the left subtree. |
| `60` | Found | The value had been inserted into the right subtree. |
| `25` | Not found | The value had not been inserted. |
| `90` | Not found | The value had not been inserted. |

## Edge Cases

### Empty-Tree Traversal

An empty tree was created and traversed. The traversal returned an empty list because the tree contained no nodes.

```python
[]
```

### Empty-Tree Search

The program searched an empty tree for `50`. The search returned `False` because the root was `None`.

```python
False
```

### Duplicate Insertion

The program attempted to insert `50` a second time.

The recursive insertion method ignored duplicate values, so the tree remained unchanged. The in-order traversal was the same before and after the duplicate insertion.

```python
[20, 30, 40, 50, 60, 70, 80]
```

## Time Complexity

The performance of the insertion and search operations depended on the height of the tree.

| Operation | Balanced Tree | Worst Case |
|---|---:|---:|
| Insertion | `O(log n)` | `O(n)` |
| Search | `O(log n)` | `O(n)` |
| In-order traversal | `O(n)` | `O(n)` |

A balanced tree reduced the remaining search space by approximately half after each comparison. A tree could become unbalanced if values were inserted in sorted order. In that case, the tree behaved more like a linked list, and insertion and searching could require visiting every node.

The recursive methods used `O(h)` call-stack space, where `h` represented the height of the tree.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Discussion Board Reflection

While completing this assignment, I learned how a Binary Search Tree stored and organized values using nodes and child references. I also gained a better understanding of recursion because the insertion, searching, and traversal methods repeatedly called themselves on smaller subtrees. In particular I learned why each recursive insertion call returned the current node and why the result was assigned back to `self.root`. This allowed the first inserted value to become the root while preserving the correct child references during later insertions.

The most challenging part was understanding how the recursive method updated the tree even though it only examined one node at a time. I overcame this by tracing an insertion from the root to an empty position and then following the returned node references back through each recursive call utilizing the debugging tool. Creating the visual tree display also helped me confirm that the values were placed correctly.

A BST created efficiency by keeping smaller values on the left and larger values on the right. This ordering allowed a search to eliminate an entire subtree after each comparison. A linear data structure, such as a list, might require checking every element. In a balanced BST, searching and insertion took approximately `O(log n)` time, although an unbalanced tree could degrade to `O(n)` time.