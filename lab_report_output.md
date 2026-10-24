# Implementation of Dijkstra's Single-Source Shortest Path Algorithm

> **Hacktoberfest Hack Day Ahmedabad 2026**  
> **Track**: Best Use of Gemma (Focused AI Tools for Student Productivity)  
> **AI Model Family**: Google Gemma 2 Academic Synthesis Engine (Automated Local Fallback)  
> **Generated On**: October 24, 2026 - 13:02:57  

---

## 📋 Student & Experiment Metadata

| Attribute | Record Details |
| :--- | :--- |
| **Student Name** | `Aryan Rayani` |
| **Enrollment Number** | `2026-ENG-CS-042` |
| **Academic Course** | `CS302 - Design and Analysis of Algorithms Lab` |
| **Target Code File** | `sample_code.py` |
| **Sandbox Safeguard** | `5.0-Second Subprocess Sandbox Timeout` |
| **Verification Result** | **✅ PASSED** (Exit Code: `0`) |
| **Execution Duration** | `1243.06 ms` |

---

## 1. 🎯 Experiment Objective

To formulate, implement, and verify Dijkstra's greedy algorithm using a binary min-heap priority queue for computing single-source shortest path trees on weighted directed/undirected graphs. The experiment validates algorithmic correctness, edge relaxation invariants, and optimal substructure properties.

### Problem Statement & Scope
Given a directed graph G = (V, E) with non-negative edge weights w: E -> R+ and a source vertex s in V, determine the shortest path distance delta(s, v) and reconstruct the shortest path trajectory from s to every reachable vertex v in V.

---

## 2. 🧠 Algorithm Theory & Mathematical Principle

Dijkstra's algorithm is grounded in the Greedy Choice Property and Optimal Substructure theorem. It maintains two disjoint sets of vertices: S (vertices whose shortest distance from source is finalized) and V \ S (vertices in the candidate priority queue). At each step, the algorithm greedily extracts the vertex u in V \ S with minimum tentative distance d[u]. For every adjacent edge (u, v) with weight w(u, v), the relaxation step tests whether d[u] + w(u, v) < d[v]. If true, d[v] is updated to d[u] + w(u, v) and its predecessor pi[v] is recorded as u. Because edge weights are strictly non-negative, the greedy choice is globally optimal (No subsequent relaxation can reduce d[u]).

### Algorithmic Code Walkthrough
1. Distance Initialization: All vertices are assigned tentative distance infinity, with the designated source vertex initialized to 0.0.
2. Min-Heap Maintenance: Python's standard `heapq` module stores pairs of `(cumulative_distance, vertex_id)`, providing O(log V) extract-min operations.
3. Vertex Finalization Loop: Vertices are popped from the min-heap. A `visited` hash-set safeguards against re-processing stale entries.
4. Edge Relaxation & Predecessor Tracking: For each outbound edge from the current vertex, edge costs are evaluated; shorter paths trigger updates and push new candidate pairs onto the priority queue.
5. Backtracking Path Reconstruction: The `reconstruct_path` function starts from target destination vertex 'Z' and backtracks through the predecessor dictionary to produce the exact sequence of router hops.

---

## 3. 💻 Verified Student Source Code

```python
"""
Experiment 04: Implementation of Dijkstra's Single-Source Shortest Path Algorithm
Student Name: Aryan Rayani
Course: CS302 - Design and Analysis of Algorithms (DAA) Lab
Enrollment No: 2026-ENG-CS-042
"""

import heapq
import time
from typing import Dict, List, Tuple, Optional

def dijkstra(graph: Dict[str, List[Tuple[str, int]]], start_node: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    """
    Computes shortest paths from start_node to all reachable nodes using a min-heap priority queue.
    
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V + E)
    """
    # Initialize distances with infinity
    distances: Dict[str, float] = {node: float('inf') for node in graph}
    distances[start_node] = 0.0
    
    # Predecessor map for path reconstruction
    predecessors: Dict[str, Optional[str]] = {node: None for node in graph}
    
    # Priority queue stores tuples of (distance, node)
    pq: List[Tuple[float, str]] = [(0.0, start_node)]
    
    visited = set()
    step_counter = 0

    print(f"[DAA LAB] Initializing Dijkstra's search from source node: '{start_node}'")
    print("-" * 65)

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If node has already been finalized, skip
        if current_node in visited:
            continue
            
        visited.add(current_node)
        step_counter += 1
        print(f"Step {step_counter:02d}: Finalized Node '{current_node}' with cumulative cost = {current_distance:.1f}")

        # Relax neighboring edges
        for neighbor, weight in graph.get(current_node, []):
            if neighbor in visited:
                continue
                
            distance = current_distance + weight
            
            # If a shorter path is found, relax the edge
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
                print(f"         Relaxed edge ({current_node} -> {neighbor}): New tentative cost = {distance:.1f}")

    print("-" * 65)
    return distances, predecessors

def reconstruct_path(predecessors: Dict[str, Optional[str]], target_node: str) -> List[str]:
    """Reconstructs the shortest path from start node to target node."""
    path = []
    curr = target_node
    while curr is not None:
        path.append(curr)
        curr = predecessors.get(curr)
    path.reverse()
    return path

def main():
    print("=" * 65)
    print("EXPERIMENT 04: DIJKSTRA'S ALGORITHM VERIFICATION")
    print("=" * 65)
    
    # Campus Network Topology (Nodes represent building routers; edges represent latency in ms)
    network_graph: Dict[str, List[Tuple[str, int]]] = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2), ('Z', 6)],
        'E': [('C', 10), ('D', 2), ('Z', 3)],
        'Z': [('D', 6), ('E', 3)]
    }

    start_node = 'A'
    destination_node = 'Z'
    
    t_start = time.perf_counter()
    distances, predecessors = dijkstra(network_graph, start_node)
    t_elapsed_ms = (time.perf_counter() - t_start) * 1000.0

    print("\n[RESULT 1: ALL-PAIRS DISTANCES FROM NODE 'A']")
    for node, dist in sorted(distances.items()):
        print(f"  Target: {node} | Shortest Latency: {dist:.1f} ms")

    optimal_path = reconstruct_path(predecessors, destination_node)
    print(f"\n[RESULT 2: OPTIMAL ROUTE TO DESTINATION '{destination_node}']")
    print(f"  Path: {' -> '.join(optimal_path)}")
    print(f"  Total Path Cost: {distances[destination_node]:.1f} ms")
    print(f"  Execution Time: {t_elapsed_ms:.4f} ms")

    # Assertions for programmatic grading verification
    assert distances['Z'] == 13.0, f"Expected 13.0 ms, got {distances['Z']}"
    assert optimal_path == ['A', 'C', 'B', 'D', 'E', 'Z'], f"Optimal path mismatch: {optimal_path}"
    print("\n[VERIFICATION STATUS] All unit assertions passed successfully! Exit Code: 0")
    print("=" * 65)

if __name__ == '__main__':
    main()
```

---

## 4. 🖥️ Live Subprocess Sandbox Execution Output

### Standard Output (stdout)
```text
=================================================================
EXPERIMENT 04: DIJKSTRA'S ALGORITHM VERIFICATION
=================================================================
[DAA LAB] Initializing Dijkstra's search from source node: 'A'
-----------------------------------------------------------------
Step 01: Finalized Node 'A' with cumulative cost = 0.0
         Relaxed edge (A -> B): New tentative cost = 4.0
         Relaxed edge (A -> C): New tentative cost = 2.0
Step 02: Finalized Node 'C' with cumulative cost = 2.0
         Relaxed edge (C -> B): New tentative cost = 3.0
         Relaxed edge (C -> D): New tentative cost = 10.0
         Relaxed edge (C -> E): New tentative cost = 12.0
Step 03: Finalized Node 'B' with cumulative cost = 3.0
         Relaxed edge (B -> D): New tentative cost = 8.0
Step 04: Finalized Node 'D' with cumulative cost = 8.0
         Relaxed edge (D -> E): New tentative cost = 10.0
         Relaxed edge (D -> Z): New tentative cost = 14.0
Step 05: Finalized Node 'E' with cumulative cost = 10.0
         Relaxed edge (E -> Z): New tentative cost = 13.0
Step 06: Finalized Node 'Z' with cumulative cost = 13.0
-----------------------------------------------------------------

[RESULT 1: ALL-PAIRS DISTANCES FROM NODE 'A']
  Target: A | Shortest Latency: 0.0 ms
  Target: B | Shortest Latency: 3.0 ms
  Target: C | Shortest Latency: 2.0 ms
  Target: D | Shortest Latency: 8.0 ms
  Target: E | Shortest Latency: 10.0 ms
  Target: Z | Shortest Latency: 13.0 ms

[RESULT 2: OPTIMAL ROUTE TO DESTINATION 'Z']
  Path: A -> C -> B -> D -> E -> Z
  Total Path Cost: 13.0 ms
  Execution Time: 0.0462 ms

[VERIFICATION STATUS] All unit assertions passed successfully! Exit Code: 0
=================================================================
```

---

## 5. ⚡ Asymptotic Big-O Complexity Analysis

| Complexity Dimension | Asymptotic Bound | Engineering Explanation |
| :--- | :--- | :--- |
| **Best-Case Time** | `O((V + E) log V)` | O((V + E) log V) - With binary min-heap, each vertex is extracted once and each edge relaxed at most once. |
| **Average-Case Time** | `O((V + E) log V)` | O((V + E) log V) - Dominant cost stems from E heap push operations and V extract-min operations. |
| **Worst-Case Time** | `O((V + E) log V)` | O((V + E) log V) - For dense graphs where E ≈ V^2, time complexity upper-bounds at O(V^2 log V). |
| **Auxiliary Memory Space** | `O(V)` | O(V) - Storage required for distances dictionary, predecessor map, and visited set. |
| **Total Footprint Space** | `O(V + E)` | O(V + E) - Total memory required to store the adjacency list representation of the network topology. |

---

## 6. 🔍 Verification & Correctness Assessment

> **Automated Verification Grade**: ✅ PASSED  
> **Analysis**: VERIFICATION CONFIRMED: All execution checkpoints and programmatic unit assertions passed successfully. Output latency metrics and shortest path sequence match theoretical analytical ground-truth.

---

## 7. 🎓 Viva-Voce Examination Preparation (Gemma AI Generated)

### Q1: Why does Dijkstra's algorithm fail or produce incorrect results on graphs with negative edge weights?
**Model Answer:** Dijkstra's algorithm assumes the greedy property: once a vertex is finalized and added to the settled set S, its shortest path is permanent and cannot decrease. Negative edge weights violate this invariant, because a path passing through a negative edge later could yield a lower total cost for an already finalized vertex. Bellman-Ford or Johnson's algorithm must be used for graphs with negative weights.

### Q2: What is the theoretical time complexity difference between using an Adjacency Matrix vs. Adjacency List with a Min-Heap?
**Model Answer:** With an Adjacency Matrix and linear search for min-distance, the time complexity is O(V^2), which is optimal for very dense graphs (E ≈ V^2). With an Adjacency List and Min-Heap (or Fibonacci Heap), complexity is O((V + E) log V) (or O(E + V log V) with Fibonacci Heap), which is significantly faster for sparse graphs where E << V^2.

### Q3: Explain the Edge Relaxation condition and how path reconstruction is mathematically achieved.
**Model Answer:** Edge relaxation evaluates the triangle inequality: if d[u] + w(u, v) < d[v], then a shorter route to v through u exists. If satisfied, d[v] is relaxed to d[u] + w(u, v) and predecessor pi[v] = u. Path reconstruction performs reverse traversal from target destination t using pi[t], pi[pi[t]], until the source s is reached, yielding the optimal sequence.

---

## ✍️ Faculty Evaluation & Grade Assessment

| Evaluation Criteria | Maximum Marks | Marks Awarded | Faculty Remarks |
| :--- | :---: | :---: | :--- |
| Algorithm Implementation & Logic | 10 | [ ___ / 10 ] | |
| Sandbox Execution & Test Cases | 10 | [ ___ / 10 ] | |
| Big-O Complexity Rigor | 05 | [ ___ / 05 ] | |
| Viva-Voce Defense | 05 | [ ___ / 05 ] | |
| **TOTAL SCORE** | **30** | **[ ___ / 30 ]** | **Status: PENDING SIGNATURE** |

**Faculty Evaluator Signature**: ________________________   **Date**: ______________
