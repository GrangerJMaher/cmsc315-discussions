"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    """Return a sorted copy using adjacent comparisons and swaps."""
    result = lst.copy()

    # Each pass moves the largest remaining value to the end.
    for end in range(len(result) - 1, 0, -1):
        swapped = False

        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True

        # No swaps means the entire list is already sorted.
        if not swapped:
            break

    return result


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    """Recursively divide the list, sort each half, and merge."""
    # Empty and single-element lists are already sorted.
    if len(lst) <= 1:
        return lst.copy()

    midpoint = len(lst) // 2

    # Recursively sort the two halves.
    left = merge_sort(lst[:midpoint])
    right = merge_sort(lst[midpoint:])

    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    """Combine two sorted lists into a new sorted list."""
    result = []
    i = 0
    j = 0

    # Take the smaller available value from either list.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Once one side is exhausted, append the remaining values.
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    dataset1 = [42, 17, 8, 63, 25, 4, 31, 12]

    print("\n=== DATASET #1 ===")
    print("Original list:", dataset1)
    print("Bubble Sort:  ", bubble_sort(dataset1))
    print("Merge Sort:   ", merge_sort(dataset1))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    dataset2 = [90, -10, 35, 0, 72, -3, 51, 6]

    bubble_result = bubble_sort(dataset2)
    merge_result = merge_sort(dataset2)

    print("\n=== DATASET #2 ===")
    print("Original list:", dataset2)
    print("Bubble Sort:  ", bubble_result)
    print("Merge Sort:   ", merge_result)
    print("Results match:", bubble_result == merge_result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    edge_cases = [
        (
            "Empty list",
            [],
            "Both algorithms return an empty list."
        ),
        (
            "Already sorted list",
            [1, 2, 3, 4, 5],
            "Bubble Sort stops after one pass without swaps. "
            "Merge Sort still divides and merges the list."
        ),
        (
            "Reverse-sorted list",
            [5, 4, 3, 2, 1],
            "Bubble Sort requires many swaps. "
            "Merge Sort uses the same divide-and-conquer process."
        ),
        (
            "Duplicate values",
            [4, 2, 4, 1, 2],
            "Both algorithms keep all duplicates and sort them correctly."
        ),
        (
            "Single-element list",
            [7],
            "Both algorithms return a copy containing the same value."
        ),
    ]
    for name, values, explanation in edge_cases:
        print(f"\n{name}")
        print("Original list:", values)
        print("Bubble Sort:  ", bubble_sort(values))
        print("Merge Sort:   ", merge_sort(values))
        print("Explanation:  ", explanation)

if __name__ == "__main__":
    main()