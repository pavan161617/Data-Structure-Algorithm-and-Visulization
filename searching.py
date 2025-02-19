import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt

# Function to perform binary search
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    steps = []
    while low <= high:
        mid = (low + high) // 2
        steps.append((low, mid, high))
        if arr[mid] == key:
            return mid, steps
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

# Function to perform linear search
def linear_search(arr, key):
    steps = []
    for i, num in enumerate(arr):
        steps.append(i)
        if num == key:
            return i, steps
    return -1, steps

# Function to find peak element
def find_peak(arr):
    low, high = 0, len(arr) - 1
    steps = []
    while low <= high:
        mid = (low + high) // 2
        steps.append(mid)
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return mid, steps
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, steps

# Streamlit UI
st.title("Search Algorithm Visualizer")

algo = st.selectbox("Choose an Algorithm", ["Binary Search", "Linear Search", "Find Peak Element"])
size = st.slider("Array Size", min_value=5, max_value=20, value=10)
arr = np.sort(np.random.randint(1, 100, size))
st.write("Array:", arr)

key = st.number_input("Enter key to search", min_value=1, max_value=100, step=1)
if st.button("Run Algorithm"):
    if algo == "Binary Search":
        index, steps = binary_search(arr, key)
        for step in steps:
            st.write(f"Low: {step[0]}, Mid: {step[1]}, High: {step[2]}")
            time.sleep(0.5)
        st.success(f"Key found at index {index}" if index != -1 else "Key not found")
    elif algo == "Linear Search":
        index, steps = linear_search(arr, key)
        for step in steps:
            st.write(f"Checking index: {step}")
            time.sleep(0.5)
        st.success(f"Key found at index {index}" if index != -1 else "Key not found")
    elif algo == "Find Peak Element":
        index, steps = find_peak(arr)
        for step in steps:
            st.write(f"Checking index: {step}")
            time.sleep(0.5)
        st.success(f"Peak element found at index {index}" if index != -1 else "No peak element found")