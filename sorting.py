import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Sorting delay
SORT_DELAY = 0.2

# Function to draw bars with index and values
def draw_bars(arr, highlight_index=None):
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color=['red' if i == highlight_index else 'blue' for i in range(len(arr))])
    
    # Adding index numbers below bars
    for i, v in enumerate(arr):
        ax.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=12, color='black')  # Show value
        ax.text(i, -1, str(i), ha='center', va='top', fontsize=10, color='black')  # Show index below
    
    ax.set_ylim(0, max(arr) + 5)
    st.pyplot(fig)

# Bubble Sort
def bubble_sort(arr):
    with st.spinner("Sorting..."):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_bars(arr, j)  # Highlight the swapping elements
                time.sleep(SORT_DELAY)

# Selection Sort
def selection_sort(arr):
    with st.spinner("Sorting..."):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            draw_bars(arr, i)
            time.sleep(SORT_DELAY)

# Insertion Sort
def insertion_sort(arr):
    with st.spinner("Sorting..."):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            draw_bars(arr, i)
            time.sleep(SORT_DELAY)

# Merge Sort Helper
def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)
        draw_bars(arr)
        time.sleep(SORT_DELAY)

# Merge Function
def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        draw_bars(arr, pi)
        time.sleep(SORT_DELAY)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Streamlit UI
st.title("Sorting Algorithm Visualizer")
st.sidebar.header("Choose a Sorting Algorithm")

# Dropdown for algorithm selection
algorithm = st.sidebar.selectbox("Select Sorting Algorithm", 
                                 ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"])

# Generate random array
size = st.sidebar.slider("Array Size", min_value=5, max_value=30, value=10)
arr = np.random.randint(1, 100, size).tolist()
st.write("Unsorted Array:", arr)
draw_bars(arr)

# Start sorting
if st.button("Sort"):
    if algorithm == "Bubble Sort":
        bubble_sort(arr)
    elif algorithm == "Selection Sort":
        selection_sort(arr)
    elif algorithm == "Insertion Sort":
        insertion_sort(arr)
    elif algorithm == "Merge Sort":
        merge_sort(arr, 0, len(arr) - 1)
    elif algorithm == "Quick Sort":
        quick_sort(arr, 0, len(arr) - 1)
    st.write("Sorted Array:", arr)
    draw_bars(arr)
