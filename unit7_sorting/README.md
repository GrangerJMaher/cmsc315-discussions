# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

### Code Summary

The program implements Bubble Sort using adjacent comparisons and swaps, with an early exit when a pass makes no swaps. Merge Sort recursively divides the list into halves, sorts each half, and combines them using the `merge()` function. Both algorithms return a new sorted list without changing the original. The program displays results for two datasets and demonstrates empty, already sorted, reverse-sorted, duplicate-value, and single-element lists. It also checks whether both algorithms produce matching results for the second dataset. A real world application would be sorting rocket motor test measurements by thrust to identify the lowest and highest recorded values.

### Reflection

This assignment strengthened my understanding of iteration, recursion, and how algorithm design affects efficiency. Implementing Bubble Sort helped me understand how repeated adjacent comparisons move larger values toward the end of a list. Merge Sort demonstrated divide and conquer by breaking a problem into smaller pieces and combining their solutions. I also learned the importance of preserving the original dataset and testing edge cases rather than relying on one example.

The most challenging part was tracking the positions in the two sorted halves during merging. I addressed this by using separate indices and appending any remaining values after one half was exhausted. Handling empty and single element lists with a base case also ensured that recursion terminated correctly.

Bubble Sort is straightforward to implement, but its average and worst-case time complexity is O(n²). With early stopping, its best case is O(n), making it reasonable for small or already sorted datasets. Merge Sort consistently takes O(n log n), making it better suited to larger datasets. Its tradeoffs include additional memory and more complicated logic. Both implementations preserve equal value ordering, and both require extra memory because they return new lists.