"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # Return an empty traversal if the starting node does not exist.
    if start not in graph:
        return []

    visited = {start}
    order = []

    # A queue uses first-in, first-out order, so earlier discoveries
    # are processed before nodes discovered farther from the start.
    queue = deque([start])

    # BFS explores level by level. Depth first traversal follows one branch as far
    # as possible before exploring other branches.
    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                # Mark neighbors when they enter the queue to prevent
                # duplicate entries and repeated visits through cycles.
                visited.add(neighbor)

                # Neighbors enter the queue so their connections can
                # be explored after the nodes already waiting.
                queue.append(neighbor)

    return order

def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # Nodes represent campus buildings.
    # Edges represent walking paths between buildings.
    # Each path appears in both buildings' lists because paths
    # can be traveled in either direction.
    graph = {
        "Library": ["Science Hall", "Student Center"],
        "Science Hall": ["Library", "Gym"],
        "Student Center": ["Library", "Cafeteria"],
        "Gym": ["Science Hall", "Cafeteria", "Dorm"],
        "Cafeteria": ["Student Center", "Gym", "Dorm"],
        "Dorm": ["Gym", "Cafeteria"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    for building, neighbors in graph.items():
        print(f"{building}: {', '.join(neighbors)}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    start = "Library"

    # Level 0: Library
    # Level 1: Science Hall and Student Center
    # Level 2: Gym and Cafeteria
    # Level 3: Dorm
    # These levels count the fewest edges from the starting building.
    print(f"Starting building: {start}")
    print("Traversal order:", " -> ".join(bfs(graph, start)))

    # Add a new building and a walking path in both directions.
    graph["Parking Lot"] = ["Student Center"]
    graph["Student Center"].append("Parking Lot")

    print("\nAdded Parking Lot connected to Student Center.")
    print(
        "Updated Student Center neighbors:",
        ", ".join(graph["Student Center"])
    )
    print("Parking Lot neighbors:", ", ".join(graph["Parking Lot"]))

    # Parking Lot is now at level 2 because it is two edges
    # away from Library through Student Center.
    print("Updated traversal:", " -> ".join(bfs(graph, start)))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: A missing starting building.
    # BFS returns an empty list instead of raising a KeyError.
    print("\nMissing start node:", bfs(graph, "Unknown"))
    print("Unknown is not in the graph, so no nodes are visited.")

    # Edge case 2: A disconnected building.
    # BFS from Library cannot reach Observatory because it has no paths.
    graph["Observatory"] = []

    print(
        "\nTraversal with disconnected Observatory:",
        " -> ".join(bfs(graph, "Library"))
    )
    print("Observatory is not visited because it is disconnected.")

    print("Starting at Observatory:", bfs(graph, "Observatory"))
    print("Only Observatory is visited because it has no neighbors.")

    # Edge case 3: A graph containing only one building.
    # The starting building is visited even though it has no paths.
    single_node_graph = {"Library": []}

    print("\nSingle-node graph:", bfs(single_node_graph, "Library"))
    print("Library is visited once.")

    # Edge case 4: An empty graph.
    # The starting building is missing, so BFS returns an empty list.
    print("\nEmpty graph:", bfs({}, "Library"))
    print("There are no buildings to visit.")

if __name__ == "__main__":
    main()