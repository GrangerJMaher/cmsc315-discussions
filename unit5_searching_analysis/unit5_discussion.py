"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # In the worst case, every element must be checked.
    # For n elements, this gives O(n) time complexity.
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    left = 0
    right = len(lst) - 1

    # Halving the search space each iteration gives O(log n) time complexity.
    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            # Discard the middle element and everything to its left.
            left = middle + 1
        else:
            # Discard the middle element and everything to its right.
            right = middle - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")
    small_dataset = [2, 4, 6, 8, 10]

    # Both searches return 3 for 8 because indexes start at 0.
    # Both return -1 for 7 because it is not in the list.
    for target in [8, 7]:
        print(f"Target: {target}")
        print(f"Linear search index: {linear_search(small_dataset, target)}")
        print(f"Binary search index: {binary_search(small_dataset, target)}")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")
    large_dataset = list(range(100000))

    # Both searches return 99999 for the last value and -1 for 100000.
    # Linear search checks all 100000 elements in either case.
    # Binary search needs at most 17 iterations for this list.
    # As n grows, O(log n) grows much more slowly than O(n).
    for target in [99999, 100000]:
        print(f"Target: {target}")
        print(f"Linear search index: {linear_search(large_dataset, target)}")
        print(f"Binary search index: {binary_search(large_dataset, target)}")

    print("Linear search checks 100000 elements for each target.")
    print("Binary search uses at most 17 iterations for each target.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")
    print("\n=== EDGE CASE TESTS ===")

    # An empty list has no elements, so both searches return -1.
    print("Empty list: expected -1")
    print(f"Linear search index: {linear_search([], 5)}")
    print(f"Binary search index: {binary_search([], 5)}")

    # The only element is the target, so both searches return 0.
    print("\nSingle-element list, target present: expected 0")
    print(f"Linear search index: {linear_search([5], 5)}")
    print(f"Binary search index: {binary_search([5], 5)}")

    # The only element is not the target, so both searches return -1.
    print("\nSingle-element list, target absent: expected -1")
    print(f"Linear search index: {linear_search([5], 3)}")
    print(f"Binary search index: {binary_search([5], 3)}")


if __name__ == "__main__":
    main()