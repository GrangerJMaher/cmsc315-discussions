# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Completed Implementation

I implemented the stack using a Python list. The end of the list represented the top of the stack. The `push()` method added a value using `append()`, while the `pop()` method removed and returned the most recently added value. The `peek()` method returned the top value without removing it, and `is_empty()` determined whether the stack contained any values.

I implemented the queue using `collections.deque`. The `enqueue()` method added values to the back using `append()`, while the `dequeue()` method removed values from the front using `popleft()`. The `front()` method returned the first value without removing it, and `is_empty()` determined whether the queue contained any values.

## LIFO and FIFO Demonstrations

The stack demonstration added the values `10`, `20`, `30`, and `40`. These values were removed in the order `40`, `30`, `20`, and `10`, demonstrating Last In First Out behavior.

The queue demonstration modeled customers waiting at a coffee shop. Alex, Blake, Casey, and Drew entered the queue in that order and were served in the same order  demonstrating First In First Out behavior.

## Edge Cases

I tested attempts to call `pop()` and `peek()` on an empty stack. Both operations raised an `IndexError`, which the program caught and displayed without terminating unexpectedly.

I also tested attempts to call `dequeue()` and `front()` on an empty queue. These operations similarly raised and handled an `IndexError`.

Finally I created stack and queue objects containing only one value. I removed each value and used `is_empty()` to verify that both structures were empty afterward.

## Runtime Efficiency and Data-Structure Selection

The stack used a Python list because the end of a list provided the most efficient location for stack operations. The `push()` method used `append()`, which required amortized `O(1)` time. It was described as amortized because an occasional list resizing operation required `O(n)` time, but most append operations required constant time.

The `pop()` method removed the final value in `O(1)` time, and `peek()` accessed the final value in `O(1)` time. The `is_empty()` method also required `O(1)` time because Python stored the current length of the list.

The queue used `collections.deque` because it was designed for efficient operations at both ends. The `enqueue()` method used `append()` to add a value to the back in `O(1)` time. The `dequeue()` method used `popleft()` to remove a value from the front in `O(1)` time. The `front()` and `is_empty()` methods also required `O(1)` time.

A regular Python list was not used for the queue because removing its first value with `pop(0)` would have required `O(n)` time. Every remaining value would have needed to shift one position toward the front. A deque avoided this shifting by maintaining efficient access to both ends.

These implementations had the best possible asymptotic runtime for the required operations. Adding, removing, or examining one value could not be faster than `O(1)` because each operation had to perform at least one action. Therefore, the selected list and deque implementations achieved the asymptotically optimal runtime for their respective stack and queue operations.

| Data structure | Operation | Method used | Runtime |
|---|---|---|---|
| Stack | Push | `list.append()` | Amortized `O(1)` |
| Stack | Pop | `list.pop()` | `O(1)` |
| Stack | Peek | `items[-1]` | `O(1)` |
| Stack | Check whether empty | `len(items) == 0` | `O(1)` |
| Queue | Enqueue | `deque.append()` | `O(1)` |
| Queue | Dequeue | `deque.popleft()` | `O(1)` |
| Queue | View front | `items[0]` | `O(1)` |
| Queue | Check whether empty | `len(items) == 0` | `O(1)` |

## Memory Usage

Both structures used `O(n)` memory, where `n` represented the number of stored values. As more values were added, each structure stored more object references, so its memory usage increased approximately linearly.

This `O(n)` memory requirement was asymptotically necessary because storing `n` values required retaining at least `n` object references. The underlying list and deque could reserve some additional capacity for efficient operations, but this did not change the overall `O(n)` space complexity.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Reflection Response

While completing this assignment I learned how stacks and queues organized and accessed data differently. I also learned how memory and runtime intensive each were and there respective operations. I implemented a stack with a Python list and a queue with `collections.deque`. This demonstrated how a class could provide a specialized interface while using an existing Python data structure for internal storage.

One challenge I encountered was safely handling operations on empty structures. Calling `pop()`, `peek()`, `dequeue()`, or `front()` on an empty structure could have caused an unexpected error. I addressed this by checking `is_empty()`, raising descriptive `IndexError` exceptions, and using `try` and `except` blocks during the demonstrations.

A stack followed Last In, First Out behavior making it useful for an undo feature because the most recent action was reversed first. A queue followed First In  First Out behavior  making it appropriate for a coffee shop line because customers were served in arrival order.

The selected internal structures also provided efficient runtimes. The stack performed `push()`, `pop()`, and `peek()` in amortized or worst-case `O(1)` time by operating at the end of a list. The deque performed `enqueue()`, `dequeue()`, and `front()` in `O(1)` time. This avoided the `O(n)` shifting that would have occurred if a regular list had removed queue values using `pop(0)`.