# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Program Description

For this assignment, I created an inventory system that uses a Python dictionary as a hash table. Each product SKU, such as `P100`, is used as a key, while the quantity of that product is stored as its associated value. The program begins by creating an empty dictionary and inserting five products into the inventory.

The program demonstrates lookup operations by using product SKUs to retrieve their quantities. It then updates the quantity associated with `P100`, showing that assigning a new value to an existing key replaces its previous value rather than creating a duplicate key. The program also removes `P200` using the `del` statement and displays the inventory before and after the operation.

Finally, the program tests two edge cases involving keys that do not exist. The `get()` method is used to safely search for `P600`, returning `None` instead of causing a `KeyError`. Before attempting to delete `P700`, the program uses the `in` operator to determine whether the key exists. This prevents the program from attempting to delete a nonexistent key and causing an error.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

### Reflection

This assignment helped me better understand how Python dictionaries use the principles of hash tables to organize information into key-value pairs. I learned how to insert, retrieve, update, and delete dictionary entries and how to safely handle keys that may not exist. One challenge was understanding what happens when a nonexistent key is accessed or deleted. I learned that directly accessing or deleting a missing key can cause a `KeyError`, while methods such as `get()` and checking for a key with the `in` operator can prevent these errors.

Hash tables work by applying a hash function to a key to determine where its associated value should be stored. Ideally, this allows a program to locate a value without searching through every element. A collision occurs when two different keys map to the same location in the hash table. The underlying implementation must resolve these collisions while still allowing the correct values to be retrieved. Because hashing provides direct access based on a key, hash tables can make insertion, lookup, and deletion much more efficient than sequentially searching through a collection.