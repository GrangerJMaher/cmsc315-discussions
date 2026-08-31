"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""
import math


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # insert() places value at the specified index.
    # The element currently at index, along with every element after it,
    # shifts one position to the right.
    lst.insert(index, value)

    # Inserting near the beginning is generally slower because many elements
    # must be shifted. Inserting near the end is faster because few or no
    # existing elements need to move.

    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validate the index before deleting. This prevents an IndexError and
    # ensures the program handles invalid input safely.
    if index < 0 or index >= len(lst):
        return None

    # pop(index) removes the element, shifts later elements one position
    # to the left, and returns the removed value.
    removed_value = lst.pop(index)
    return removed_value


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search because it examines elements sequentially,
    # starting at the beginning and continuing one element at a time.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # If the entire list is scanned without finding the value, return -1.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # Create and display the original list.
    values = [10, 20, 30, 40]
    print("Original list:", values)

    # Insert 5 at index 0, which is the beginning of the list.
    insert_at(values, 0, 5)
    print("After inserting 5 at the beginning:", values)

    # Insert 25 at the middle index. Existing elements at and after this
    # index are shifted one position to the right.
    middle_index = math.ceil(len(values) / 2)
    insert_at(values, middle_index, 25)
    print("After inserting 25 in the middle:", values)

    # Using len(values) as the index inserts 50 at the end of the list.
    insert_at(values, len(values), 50)
    print("After inserting 50 at the end:", values)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Delete the first element, located at index 0.
    removed_value = delete_at(values, 0)
    print("Removed from the beginning:", removed_value)
    print("Updated list:", values)

    # Delete the element at the current middle index.
    middle_index = math.ceil(len(values) / 2)
    removed_value = delete_at(values, middle_index)
    print("Removed from the middle:", removed_value)
    print("Updated list:", values)

    # The final element is located at index len(values) - 1.
    removed_value = delete_at(values, len(values) - 1)
    print("Removed from the end:", removed_value)
    print("Updated list:", values)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Search for a value that exists and display its index.
    search_result = search_value(values, 25)
    print("Searching for 30: found at index", search_result)

    # Search for a value that is absent. The function returns -1.
    search_result = search_value(values, 100)
    print("Searching for 100: not found; result =", search_result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")


    # Edge case 1: An invalid index cannot be deleted, so None is returned.
    removed_value = delete_at(values, 100)
    print("Deleting at invalid index 100:", removed_value)
    print("List remains unchanged:", values)

    # Edge case 2: Deleting from an empty list safely returns None.
    empty_list = []
    removed_value = delete_at(empty_list, 0)
    print("Deleting from an empty list:", removed_value)

    # Edge case 3: A value can still be inserted into an empty list.
    insert_at(empty_list, 0, 99)
    print("After inserting 99 into the empty list:", empty_list)

if __name__ == "__main__":
    main()