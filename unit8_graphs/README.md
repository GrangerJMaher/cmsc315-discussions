# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

This program models a campus navigation system. Buildings represent nodes, and walking paths represent edges. It displays the graph, performs BFS, adds a new building and path, and demonstrates edge cases.

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

## How the Code Works

The graph is represented by a Python dictionary using adjacency lists. Each key is a building name, and its value is a list of neighboring buildings. The initial graph includes Library, Science Hall, Student Center, Gym, Cafeteria, and Dorm. Each walking path appears in both buildings’ lists because the graph is undirected.

The bfs(graph, start) function first checks whether the starting building exists. If it does not, the function returns an empty list. Otherwise, it creates a visited set, a queue using deque, and a list to record the traversal order.

The starting building is marked as visited and added to the queue. The function repeatedly removes the building at the front of the queue, records it, and adds its unvisited neighbors. Neighbors are marked as visited when they enter the queue to prevent duplicate entries and repeated visits through cycles.

The queue processes buildings in first-in, first-out order, allowing BFS to explore level by level. Starting from Library produces this traversal:

Library -> Science Hall -> Student Center -> Gym -> Cafeteria -> Dorm

The program then adds Parking Lot and connects it to Student Center in both directions. The updated traversal is:

Library -> Science Hall -> Student Center -> Gym -> Cafeteria -> Parking Lot -> Dorm

The order within each level depends on the order of neighbors in the adjacency lists. This function returns the order of visited buildings rather than a specific route or walking distance.

## Edge Cases

- Missing starting node: Starting from Unknown returns an empty list.
- Disconnected graph: Observatory has no paths, so BFS from Library does not reach it. Starting from Observatory visits only Observatory.
- Single-node graph: A graph containing only Library visits Library once.
- Empty graph: BFS returns an empty list because the starting node does not exist.

## Reflection Response

While completing this assignment, I learned how to represent a graph using an adjacency list and traverse it using breadth-first search. My example modeled campus buildings as nodes and walking paths as edges. Using Python’s deque helped me understand how a first-in, first-out queue allows BFS to explore buildings level by level.

One challenge was preventing the search from repeatedly visiting buildings connected by cycles. I addressed this by using a visited set and marking each building as visited when adding it to the queue. I also explored missing starting nodes, disconnected buildings, single-node graphs, and empty graphs. These cases helped me understand that BFS only visits nodes reachable from the starting location.

BFS and DFS differ in how they explore connections. BFS searches neighboring nodes before moving farther away, while DFS follows one branch deeply before backtracking. BFS is useful for finding routes with the fewest connections in an unweighted graph, such as campus paths or degrees of separation in social networks. DFS is useful for exploring mazes, detecting cycles, and analyzing dependencies. This assignment helped me connect graph traversal algorithms to practical navigation problems.