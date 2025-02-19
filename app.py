import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Initialize state variables
if "arr" not in st.session_state:
    st.session_state.arr = [random.randint(1, 100) for _ in range(10)]
    st.session_state.size = 10
    st.session_state.max_value = 100
    st.session_state.time_delay = 0.5
    st.session_state.step = 0

# Function to visualize the array
def draw_array(arr, highlight=[]):
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ["yellow" if i in highlight else "skyblue" for i in range(len(arr))]
    ax.bar(range(len(arr)), arr, color=colors)
    ax.set_xticks(range(len(arr)))
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title("Array Visualization")
    st.pyplot(fig)

# Function for Kadane's Algorithm (Maximum Subarray Sum)
def kadane_algorithm(arr):
    max_sum = -float("inf")
    current_sum = 0
    start = end = s = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i
        if current_sum < 0:
            current_sum = 0
            s = i + 1
    return max_sum, arr[start : end + 1]

# Function for Linear Search
def linear_search(arr, key):
    for i, value in enumerate(arr):
        if value == key:
            return i
    return -1

# Rainwater Trapping Algorithm with Visualization
def rain_water_trapping(arr):
    n = len(arr)
    if n == 0:
        return 0, []

    left_max = [0] * n
    right_max = [0] * n
    trapped_water = [0] * n

    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])

    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])

    total_water = 0
    for i in range(n):
        trapped_water[i] = max(0, min(left_max[i], right_max[i]) - arr[i])
        total_water += trapped_water[i]

    return total_water, trapped_water

# Function to visualize Rainwater Trapping
def visualize_rainwater(arr, trapped_water):
    fig, ax = plt.subplots(figsize=(10, 5))

    bar_width = 0.8
    for i in range(len(arr)):
        ax.bar(i, arr[i], width=bar_width, color="blue")  # Original bars
        if trapped_water[i] > 0:
            ax.bar(i, trapped_water[i], bottom=arr[i], width=bar_width, color="cyan", alpha=0.7)  # Trapped water

    ax.set_xlabel("Index")
    ax.set_ylabel("Height")
    ax.set_xticks(range(len(arr)))
    ax.set_title("Rain Water Trapping Visualization")
    st.pyplot(fig)

# Prefix Sum Algorithm
def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

# Partition Algorithm (Lomuto Partition)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Streamlit UI
st.title("Array Operations with Streamlit")
st.write("Visualize algorithms like Kadane's, Linear Search, Partition, Prefix Sum, and Rainwater Trapping.")

# Display the array
st.subheader("Current Array:")
draw_array(st.session_state.arr)

# Insert Element
with st.expander("Insert Element"):
    insert_index = st.number_input(
        "Index to Insert", min_value=0, max_value=st.session_state.size - 1, value=0
    )
    insert_value = st.number_input(
        "Value to Insert", min_value=1, max_value=st.session_state.max_value, value=1
    )

    if st.button("Insert Element"):
        st.session_state.arr.insert(insert_index, insert_value)
        st.session_state.size += 1
        st.write(f"Inserted {insert_value} at index {insert_index}")
        draw_array(st.session_state.arr)

# Delete Element
with st.expander("Delete Element"):
    delete_index = st.number_input(
        "Index to Delete", min_value=0, max_value=st.session_state.size - 1, value=0
    )

    if st.button("Delete Element"):
        deleted_value = st.session_state.arr.pop(delete_index)
        st.session_state.size -= 1
        st.write(f"Deleted {deleted_value} at index {delete_index}")
        draw_array(st.session_state.arr)

# Run Kadane's Algorithm
if st.button("Run Kadane's Algorithm"):
    max_sum, sub_array = kadane_algorithm(st.session_state.arr)
    st.write(f"Maximum Subarray Sum: {max_sum}")
    st.write(f"Subarray: {sub_array}")

# Linear Search
search_key = st.number_input(
    "Enter element to search", min_value=0, max_value=st.session_state.max_value, value=0
)
if st.button("Search Element"):
    index = linear_search(st.session_state.arr, search_key)
    if index != -1:
        st.write(f"Element {search_key} found at index {index}")
    else:
        st.write(f"Element {search_key} not found.")

# Partition Algorithm Execution
if st.button("Partition Array"):
    partition_index = partition(st.session_state.arr, 0, len(st.session_state.arr) - 1)
    st.write(f"Partition Done! Pivot Index: {partition_index}")
    draw_array(st.session_state.arr)

# Prefix Sum Execution
if st.button("Compute Prefix Sum"):
    prefix = prefix_sum(st.session_state.arr)
    st.write("Prefix Sum Array:", prefix)
    draw_array(prefix)

# Rainwater Trapping Execution
if st.button("Calculate Trapped Rainwater"):
    trapped_water, water_levels = rain_water_trapping(st.session_state.arr)
    st.write(f"Total Water Trapped: {trapped_water}")
    visualize_rainwater(st.session_state.arr, water_levels)

# Reset the array
if st.button("Reset Array"):
    st.session_state.arr = [random.randint(1, 100) for _ in range(10)]
    st.session_state.size = 10
    draw_array(st.session_state.arr)
