"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""

class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Each node stores a value and references to its two children.
        # A new node begins as a leaf, so both references are None.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # An empty tree does not have a root node.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Smaller values belong on the left, while larger values
        # belong on the right. This ordering gives the BST its
        # efficient search behavior.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # Reaching None means that an available position was found.
        if node is None:
            return Node(value)

        if value < node.value:
            # A smaller value must be inserted somewhere in the
            # current node's left subtree.
            node.left = self._insert_recursive(node.left, value)

        elif value > node.value:
            # A larger value must be inserted somewhere in the
            # current node's right subtree.
            node.right = self._insert_recursive(node.right, value)

        else:
            # This implementation ignores duplicates because each
            # value is stored only once in the tree.
            return node

        # Return the node so its parent keeps the correct child reference.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # A BST can eliminate an entire subtree after each comparison.
        # A linear search may have to check every element individually.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # If None is reached, the value is not in the tree.
        if node is None:
            return False

        if value == node.value:
            return True

        if value < node.value:
            # A smaller value can only be in the left subtree.
            return self._search_recursive(node.left, value)

        # A larger value can only be in the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        if node is None:
            return

        # In-order traversal visits the left subtree, the current node,
        # and then the right subtree. Since smaller BST values are on
        # the left and larger values are on the right, the result is sorted.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)

    def print_tree(self):
        print(self.tree_to_string())

    def tree_to_string(self):
        if self.root is None:
            return "(empty tree)"

        return "\n".join(self._tree_lines(self.root))

    def _tree_lines(self, node):
        if node is None:
            return []

        label = f"[{node.value}]"
        left = self._tree_lines(node.left)
        right = self._tree_lines(node.right)

        if not left and not right:
            return [label]

        if not left:
            offset = right[0].index("[") - len(label)
            top = [
                " " * max(0, offset) + label,
                " " * max(len(label), right[0].index("[")) + "\\"
            ]
            return top + [" " * max(0, -offset) + row for row in right]

        if not right:
            offset = left[0].index("]")
            return [
                " " * (offset + 1) + label,
                " " * offset + "/"
            ] + left

        offset = max(
            0, len(left[0]) + len(label) - right[0].index("[")
        )

        for i in range(0, min(len(left), len(right)), 2):
            offset = max(
                offset, len(left[i]) + 3 - right[i].index("[")
            )

        merged = []
        for i in range(max(len(left), len(right))):
            a = left[i] if i < len(left) else ""
            if i < len(right):
                b = " " * offset + right[i]
                a += b[len(a):]
            merged.append(a)

        x = merged[0].index("]")
        y = merged[0].rindex("[")
        padding = max(0, y - x - 1 - len(label))

        top = (
                " " * (x + 1)
                + "_" * (padding // 2)
                + label
                + "_" * ((padding + 1) // 2)
        )
        branches = " " * x + "/" + " " * (y - x - 1) + "\\"

        return [top, branches] + merged

def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    tree = BST()
    inserted_values = [50, 30, 70, 20, 40, 60, 80]

    for value in inserted_values:
        tree.insert(value)

    print("Values inserted:", inserted_values)
    tree.print_tree()

    # At each node, the BST compares the new value with the current
    # value. It then moves left or right, eliminating the opposite
    # subtree from consideration and reducing the remaining search space.
    print("Smaller values were placed left; larger values were placed right.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    traversal = tree.inorder()
    print("In-order traversal:", traversal)

    # The traversal is sorted because it visits all smaller values
    # before the current node and all larger values afterward.
    print("The values are sorted because traversal follows left, node, right.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # The searches for 20 and 60 return True because those values were
    # inserted. The searches for 25 and 90 return False because they
    # do not appear anywhere in the tree.

    search_values = [20, 60, 25, 90]

    for value in search_values:
        result = tree.search(value)

        if result:
            print(f"Search for {value}: Found")
        else:
            print(f"Search for {value}: Not found")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    empty_tree = BST()

    # Traversing an empty tree returns an empty list because there are
    # no nodes to visit.
    print("Empty-tree traversal:", empty_tree.inorder())

    # Searching an empty tree returns False because its root is None.
    print("Search empty tree for 50:", empty_tree.search(50))

    # The insert method ignores duplicate values in this implementation.
    print("Tree before duplicate insertion:", tree.inorder())
    tree.insert(50)
    print("Tree after inserting duplicate 50:", tree.inorder())


if __name__ == "__main__":
    main()