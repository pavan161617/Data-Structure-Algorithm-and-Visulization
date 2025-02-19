import streamlit as st
import webbrowser
import pandas as pd
import plotly.express as px

# Define the mapping of categories to their respective local URLs and descriptions
categories = {
    "Array": ("http://localhost:8501", "Visualize array operations like insertion, deletion, and sorting."),
    "Greedy": ("http://localhost:8502", "See how greedy algorithms optimize solutions efficiently."),
    "Queue": ("http://localhost:8503", "Understand queue operations like enqueue and dequeue."),
    "Backtracking": ("http://localhost:8504", "Explore backtracking algorithms with visualization."),
    "Sorting": ("http://localhost:8505", "Compare different sorting algorithms in action."),
    "Stack": ("http://localhost:8506", "Learn how stacks handle operations like push and pop."),
    "Searching": ("http://localhost:8507", "Experience searching techniques like binary and linear search."),
}

# Set page config
st.set_page_config(page_title="Data Structure Visualization", layout="wide")

# Title
st.title("Data Structure Algorithm Visualization")

# Search bar
search_query = st.text_input("Search for a category", "")

# Initialize session state for click tracking if not already done
if 'click_counts' not in st.session_state:
    st.session_state.click_counts = {name: 0 for name in categories.keys()}

# Reorder categories so that searched items appear at the top
if search_query:
    categories = dict(sorted(categories.items(), key=lambda x: (search_query.lower() not in x[0].lower(), x[0])))

# Create a grid layout for the blocks
cols = st.columns(4)

# Dark Mode Toggle
dark_mode = st.toggle("Dark Mode")

# Apply dark mode styling
if dark_mode:
    st.markdown(
        """
        <style>
            body { background-color: #222; color: white; }
            .stButton>button { background-color: #444; color: white; }
        </style>
        """, unsafe_allow_html=True
    )

# Display blocks with hover descriptions
for i, (name, (url, description)) in enumerate(categories.items()):
    with cols[i % 4]:
        if st.button(name, key=name):
            webbrowser.open(url)
            st.session_state.click_counts[name] += 1  # Increment click count
        st.caption(description)

# Analytics Dashboard
st.subheader("Analytics Dashboard")

# Display recorded click counts
st.write("### Recorded Click Counts")
st.write(st.session_state.click_counts)

click_data = pd.DataFrame({"Category": list(st.session_state.click_counts.keys()), "Clicks": list(st.session_state.click_counts.values())})
fig = px.bar(click_data, x="Category", y="Clicks", title="Category Click Counts", labels={"Clicks": "Number of Clicks"}, color="Category")
st.plotly_chart(fig)
