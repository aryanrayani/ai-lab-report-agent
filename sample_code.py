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
