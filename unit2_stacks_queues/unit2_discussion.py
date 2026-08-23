"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.

        # Create an empty list to store the stack's values.
        # THe end of the list will represent the top of the stack.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # Add the new value to the top of the stack.
        # Because the newest value is removed first, this supports Last-In, First-Out (LIFO) behavior.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # Raise an error if there is no values to remove.
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        # Remove and return the most recently added value.
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # Return the top value without removing it from the stack.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")

        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        # Return True when the stack contains no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        # Create an empty deque to store the queue's values.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # Add the value to the back of the queue.
        # Values added first remain at the front, values added after are appended to the back, supporting FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # Raise an error if there are no values to remove.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")

        # Remove and return the value at the front of the queue.
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # Return the front value without removing it from the queue.
        if self.is_empty():
            raise IndexError("Cannot access the front of an empty queue.")

        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.

        # Return True if the queue contains no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.")

    # Create a Stack object.
    stack = Stack()

    # Add for values to the stack.
    print("\nPushing 10, 20, 30, and 40 onto the stack.")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    # Demonstrate LIFO behavior.
    print("\nRemoving values from the stack:")
    print(f"Popped: {stack.pop()}") # 40 leaves first
    print(f"Popped: {stack.pop()}") # 30 leaves first
    print(f"Popped: {stack.pop()}") # 20 leaves first
    print(f"Popped: {stack.pop()}") # 10 leaves first
    print("The values were removed in reverse order, demonstrating LIFO behavior.")

    # Show what happens when pop() is called on an empty stack.
    print("\nAttempting to pop from an empty stack:")
    try:
        stack.pop()
    except IndexError as error:
        print(f"Error: {error}")

    # Show what happens when peek() is called on an empty stack.
    print("\nAttempting to peek at an empty stack:")
    try:
        stack.peek()
    except IndexError as error:
        print(f"Error: {error}")

    # Test a stack containing only one item. Remove it and show it is empty with is_empty().
    print("\nTesting a stack with one item:")
    single_item_stack = Stack()
    single_item_stack.push(100)

    print(f"Top value: {single_item_stack.peek()}")
    print(f"Removed value: {single_item_stack.pop()}")
    print(f"Is the stack empty? {single_item_stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    print("      test dequeuing from an empty queue,")
    print("      test viewing the front of an empty queue,")
    print("      and verify a single-item queue becomes empty after removal.")

    # Create a Queue object.
    queue = Queue()

    # Add four customers to the back of the queue.
    print("\nFour customers at the coffee shop.")
    queue.enqueue("Alex")
    queue.enqueue("Blake")
    queue.enqueue("Casey")
    queue.enqueue("Drew")

    # Display the customer at the front without removing them.
    print(f"The first customer waiting is: {queue.front()}")

    # Remove the customers to demonstrate FIFO behavior.
    print("\nServing customers in FIFO order:")
    while not queue.is_empty():
        print(f"Serving: {queue.dequeue()}")

    print("Customers were served in the order they arrived, demonstrating FIFO.")

    # Show what happens when dequeue() is used on an empty queue. Exception handling.
    print("\nAttempting to dequeue from an empty queue:")
    try:
        queue.dequeue()
    except IndexError as error:
        print(f"Error handheld: {error}")

    # Show what happens when front() is used on an empty queue. Exception handling.
    print("\nAttempting to view the front of an empty queue:")
    try:
        queue.front()
    except IndexError as error:
        print(f"Error handled: {error}")

    # Create a queue with one item and remove it. Then print whether the queue is empty with is_empty()
    print("\nTesting a queue containing one item:")
    single_item_queue = Queue()
    single_item_queue.enqueue("Only Customer")

    print(f"Removed: {single_item_queue.dequeue()}")
    print(f"Is the single item queue now empty? {single_item_queue.is_empty()}")

if __name__ == "__main__":
    main()
