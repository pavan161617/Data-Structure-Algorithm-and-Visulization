import streamlit as st
import matplotlib.pyplot as plt
import time
from collections import deque

# Streamlit page config
st.set_page_config(page_title="Queue Visualization", layout="wide")

# Queue data structure
class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def clear(self):
        self.queue.clear()
    
    def get_items(self):
        return list(self.queue)

# Initialize session state for the queue if not already done
if "queue" not in st.session_state:
    st.session_state.queue = Queue()

# Function to visualize the queue
def plot_queue(queue_items):
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.clear()
    ax.set_xlim(0, len(queue_items) + 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    for i, item in enumerate(queue_items):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, fill=True, color='skyblue', edgecolor='black'))
        ax.text(i + 0.5, 0.5, str(item), fontsize=12, ha='center', va='center')
    
    st.pyplot(fig)

# Streamlit UI
st.title("Queue Data Structure Visualization")

col1, col2 = st.columns(2)

with col1:
    new_element = st.text_input("Enter an element to enqueue:")
    if st.button("Enqueue"):
        if new_element:
            st.session_state.queue.enqueue(new_element)
            time.sleep(0.5)  # Animation effect
            st.rerun()
    
    if st.button("Dequeue"):
        dequeued_item = st.session_state.queue.dequeue()
        if dequeued_item is not None:
            st.success(f"Dequeued: {dequeued_item}")
            time.sleep(0.5)  # Animation effect
            st.rerun()
        else:
            st.warning("Queue is empty!")
    
    if st.button("Peek"):
        front_item = st.session_state.queue.peek()
        if front_item is not None:
            st.info(f"Front Element: {front_item}")
        else:
            st.warning("Queue is empty!")
    
    if st.button("Clear Queue"):
        st.session_state.queue.clear()
        time.sleep(0.5)  # Animation effect
        st.rerun()

with col2:
    st.subheader("Queue Visualization")
    plot_queue(st.session_state.queue.get_items())

# Run Streamlit on a different port
if __name__ == "__main__":
    import os
    os.system("streamlit run queue_visual.py --server.port=8502")
