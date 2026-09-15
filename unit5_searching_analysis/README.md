# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## How the Code Works

### Linear Search

The `linear_search(lst, target)` function checks each element from the beginning of the list. If an element matches the target the function returns its index. If the loop finishes without finding the target it returns `-1`.

Linear search works on both sorted and unsorted lists. Its worst case time complexity is O(n) because it may need to check every element.

### Binary Search

The `binary_search(lst, target)` function requires a sorted list. It uses `left` and `right` to track the boundaries of the remaining search area. During each iteration, it calculates the middle index using `(left + right) // 2`.

If the middle element matches the target, the function returns its index. If the target is larger, `left` moves past the middle element. If the target is smaller, `right` moves before it. Each step eliminates approximately half of the remaining elements.

If the boundaries cross, the target is absent, and the function returns `-1`. Binary search has O(log n) worst-case time complexity.

### Dataset Tests and Results

The `main()` function runs both algorithms and prints their results.

- **Small dataset:** The list `[2, 4, 6, 8, 10]` is searched for `8` and `7`. Both algorithms return index `3` for `8` and `-1` for `7`.
- **Large dataset:** A list containing integers from `0` through `99999` is searched for `99999` and `100000`. Both algorithms return `99999` for the existing value and `-1` for the missing value.
- **Empty list:** Both algorithms return `-1`.
- **Single element list:** Both return `0` when the target is present and `-1` when it is absent.

For each large dataset target, linear search checks all 100,000 elements. Binary search requires only 17 iterations. These counts follow from how the algorithms work; the program does not measure execution time.

The `if __name__ == "__main__":` statement calls `main()` when the file is run directly.

## Real-World Use Case

A student directory could use either algorithm to find a student ID. Linear search is useful when the IDs are unsorted or the directory is small. Binary search is useful when the IDs are already sorted, especially if the directory is large and searched frequently.

Sorting an unsorted directory takes additional work. For a single search linear search may be more practical than sorting first. For many searches, maintaining a sorted list can make binary search worthwhile.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

### My Reflection

In this assignment I learned how to implement linear and binary search and compare their efficiency. Linear search checks elements one at a time while binary search repeatedly divides the search area in half. Testing both algorithms helped me understand why O(log n) becomes more efficient than O(n) as the dataset grows.

The most challenging part was understanding how to update the boundaries in binary search. I worked through which half could contain the target and moved the appropriate boundary past the middle element. This ensures that the search keeps progressing. Testing empty and single element lists also helped me check the stopping conditions and return values.

Linear search is useful for small or unsorted datasets because it does not require preparation. Binary search is useful for large, sorted datasets that need frequent searches. For example a student directory sorted by ID could use binary search to find records quickly. However, sorting an unsorted directory takes extra work, and keeping it sorted requires effort when records change. For a single lookup in an unsorted list, linear search may be the more practical choice.