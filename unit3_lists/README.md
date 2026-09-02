# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Implementation and How the Code Works

This program demonstrates insertion, deletion, and searching using Python's built in list. Each operation has its own function while `main()` runs tests and displays the results.

### Insertion: `insert_at(lst, index, value)`

This function uses `lst.insert(index, value)` to insert a value at a specified position. Existing elements at that index and beyond shift one position to the right.

- Index `0` inserts at the beginning.
- Index `len(lst) // 2` inserts at the middle.
- Index `len(lst)` inserts at the end.

The function modifies the original list and returns that same list.

### Deletion: `delete_at(lst, index)`

This function checks whether the index is between `0` and `len(lst) - 1`. This implementation treats negative indices as invalid.

If the index is invalid, the function returns `None` without changing the list. Otherwise `lst.pop(index)` removes and returns the selected element. Later elements shift one position to the left.

Validating the index prevents an `IndexError` including when deleting from an empty list.

### Searching: `search_value(lst, value)`

This function performs a linear search by checking each element sequentially.

- If the value is found, the function returns its index.
- If the value is missing, the function returns `-1`.
- If the value appears multiple times, the function returns the first matching index.

Searching does not modify the list.

### Program Execution and Testing

The `main()` function demonstrates:

1. Inserting values at the beginning, middle, and end.
2. Deleting values from each of these positions.
3. Searching for existing and missing values.
4. Handling invalid deletion indices.
5. Deleting from an empty list.
6. Inserting into an empty list.

The middle and final indices are recalculated using the current list length because insertions and deletions change the list's size. Printed output shows the updated list, removed values, and search results.

The `if __name__ == "__main__":` check calls `main()` when the file is run directly, but not when it is imported into another Python file.

### Performance Considerations

Python lists are dynamic arrays that store references to their elements. Inserting or deleting near the beginning requires shifting many references, while operations at the end avoid these shifts.

| Operation | Time Complexity |
|---|---|
| Insert at the beginning or middle | O(n) |
| Insert at the end | O(1) amortized |
| Delete at the beginning or middle | O(n) |
| Delete at the end | O(1) amortized |
| Linear search | O(n) worst case |
| Access an element by index | O(1) |

Here `n` is the number of elements in the list. Amortized O(1) means constant time on average over many operations allowing for occasional resizing.
