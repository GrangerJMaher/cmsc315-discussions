"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # Create an empty dictionary. Python dictionaries behave like hash
    # tables by storing information as key-value pairs. The key is used
    # to locate its associated value.
    inventory = {}

    # Add five key-value pairs to the dictionary.
    # Each product ID is a key and its quantity is the value.
    inventory["P100"] = 15
    inventory["P200"] = 9
    inventory["P300"] = 20
    inventory["P400"] = 12
    inventory["P500"] = 7

    print("\n=== INSERT OPERATIONS ===")
    print("Inventory after inserting five items:")
    print(inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    # A value can be looked up by providing its key.
    # The dictionary uses the key to locate the associated value.
    print("\n=== LOOKUP OPERATIONS ===")

    print("P100 quantity:", inventory["P100"])
    print("P300 quantity:", inventory["P300"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Inventory before update:")
    print(inventory)

    # Assigning a new value to an existing key updates the value
    # instead of creating another copy of the key.
    inventory["P100"] = 25

    print("Inventory after updating P100:")
    print(inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Inventory before deletion:")
    print(inventory)

    # The del statement removes the key and its associated value
    # from the dictionary.
    del inventory["P200"]

    print("Inventory after deleting P200:")
    print(inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Looking up a key that does not exist.
    # The get() method safely returns None instead of causing
    # a KeyError when the key cannot be found.
    print("Looking up missing key P600:")
    print("P600 quantity:", inventory.get("P600"))

    # Edge Case 2: Safely attempting to delete a missing key.
    # Checking whether the key exists first prevents a KeyError.
    print("Attempting to delete missing key P700:")

    if "P700" in inventory:
        del inventory["P700"]
        print("P700 was deleted.")
    else:
        print("P700 was not found, so nothing was deleted.")



if __name__ == "__main__":
    main()