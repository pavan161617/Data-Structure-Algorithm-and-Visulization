import streamlit as st
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="Greedy Algorithms", layout="centered")

# Title
st.markdown("## Greedy Algorithm")

# Kruskal's Algorithm with Visualization
st.markdown("### Kruskal's Minimum Spanning Tree (MST)")
def kruskal_mst():
    st.write("Enter graph edges (u, v, weight):")
    edges_input = st.text_area("Example: 0 1 10\n0 2 6\n0 3 5\n1 3 15\n2 3 4", height=150)
    if st.button("Run Kruskal's Algorithm"):
        class Edge:
            def __init__(self, u, v, weight):
                self.u = u
                self.v = v
                self.weight = weight

        def find(parent, i):
            if parent[i] == i:
                return i
            parent[i] = find(parent, parent[i])  # Path compression
            return parent[i]

        def union(parent, rank, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                if rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                elif rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        def kruskal(edges, V):
            result = []
            edges.sort(key=lambda x: x.weight)
            parent = list(range(V))
            rank = [0] * V
            e, i = 0, 0
            while e < V - 1 and i < len(edges):
                edge = edges[i]
                i += 1
                x, y = find(parent, edge.u), find(parent, edge.v)
                if x != y:
                    e += 1
                    result.append(edge)
                    union(parent, rank, x, y)
            return result
        
        edges = []
        lines = edges_input.split('\n')
        for line in lines:
            parts = line.split()
            if len(parts) == 3:
                edges.append(Edge(int(parts[0]), int(parts[1]), int(parts[2])))
        
        V = max((max(edge.u, edge.v) for edge in edges), default=0) + 1 if edges else 0
        if V > 0:
            mst_edges = kruskal(edges, V)
            for edge in mst_edges:
                st.write(f"Edge: {edge.u} - {edge.v} | Weight: {edge.weight}")
            
            # Visualization
            G = nx.Graph()
            for edge in edges:
                G.add_edge(edge.u, edge.v, weight=edge.weight)
            pos = nx.spring_layout(G)
            plt.figure(figsize=(6, 4))
            nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
            nx.draw_networkx_edge_labels(G, pos, edge_labels={(edge.u, edge.v): edge.weight for edge in edges})
            st.pyplot(plt)
        else:
            st.error("Invalid or empty input. Please enter valid graph edges.")
kruskal_mst()

# Fractional Knapsack
st.markdown("### Fractional Knapsack")
def fractional_knapsack():
    weights_input = st.text_input("Enter weights (comma separated):", "10,20,30")
    values_input = st.text_input("Enter values (comma separated):", "60,100,120")
    capacity = st.number_input("Enter knapsack capacity:", min_value=1, value=50)
    if st.button("Run Knapsack Algorithm"):
        weights = list(map(int, weights_input.split(',')))
        values = list(map(int, values_input.split(',')))
        ratio = sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True)
        total_value = 0
        for w, v in ratio:
            if capacity >= w:
                capacity -= w
                total_value += v
            else:
                total_value += (capacity / w) * v
                break
        st.write(f"Maximum Value: {total_value}")
fractional_knapsack()

# Merge Intervals
st.markdown("### Merge Intervals")
def merge_intervals():
    intervals_input = st.text_area("Enter intervals (each line start,end):", "1,3\n2,6\n8,10\n15,18")
    if st.button("Run Merge Intervals"):
        intervals = [list(map(int, line.split(','))) for line in intervals_input.split('\n') if line]
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        st.write(f"Merged Intervals: {merged}")
merge_intervals()

# Counting Money
st.markdown("### Counting Money")
def counting_money():
    amount = st.number_input("Enter amount:", min_value=1, value=289)
    if st.button("Run Money Counting"):
        denominations = [100, 50, 20, 10, 5, 1]
        result = {}
        for denom in denominations:
            count, amount = divmod(amount, denom)
            if count:
                result[denom] = count
        st.write(f"Money Breakdown: {result}")
counting_money()

# Huffman Coding
st.markdown("### Huffman Coding")
def huffman_coding():
    freq_input = st.text_area("Enter character frequencies (char:freq per line):", "a:5\nb:9\nc:12\nd:13\ne:16\nf:45")
    if st.button("Run Huffman Coding"):
        class Node:
            def __init__(self, char, freq):
                self.char = char
                self.freq = freq
                self.left = None
                self.right = None
            def __lt__(self, other):
                return self.freq < other.freq
        
        def huffman_tree(freq_dict):
            heap = [Node(char, freq) for char, freq in freq_dict.items()]
            heapq.heapify(heap)
            while len(heap) > 1:
                left, right = heapq.heappop(heap), heapq.heappop(heap)
                merged = Node(None, left.freq + right.freq)
                merged.left, merged.right = left, right
                heapq.heappush(heap, merged)
            return heap[0]
        
        def generate_codes(node, prefix="", code_dict={}):
            if node:
                if node.char is not None:
                    code_dict[node.char] = prefix
                generate_codes(node.left, prefix + "0", code_dict)
                generate_codes(node.right, prefix + "1", code_dict)
            return code_dict
        
        freq_dict = {line.split(':')[0]: int(line.split(':')[1]) for line in freq_input.split('\n') if ':' in line}
        root = huffman_tree(freq_dict)
        codes = generate_codes(root)
        st.write(f"Huffman Codes: {codes}")
huffman_coding()
