import streamlit as st
import itertools
import time
import math

# Set page title
st.set_page_config(page_title="String Permutation Generator", layout="wide")

# Page heading
st.title("🔀 String Permutation Generator")

# Sidebar settings
st.sidebar.header("⚙️ Settings")

# Step visualization settings
visualize_steps = st.sidebar.checkbox("Show Step-by-Step Animation", value=True)
animation_speed = st.sidebar.slider("Animation Speed (seconds per step)", 0.1, 1.0, 0.3)

# User enters a string (no length limit)
user_input = st.text_input("Enter a string (No Length Limit):")

# Function to generate permutations using backtracking
def permute_backtracking(s, step=0, results=[]):
    if step == len(s):
        results.append("".join(s))
        return
    for i in range(step, len(s)):
        s[step], s[i] = s[i], s[step]  # Swap
        permute_backtracking(s, step + 1, results)
        s[step], s[i] = s[i], s[step]  # Swap back (backtracking)
    return results

# Solve permutations when button is clicked
if st.button("Generate Permutations"):
    if len(user_input) == 0:
        st.warning("⚠️ Please enter a string.")
    else:
        st.write("### 🔹 All Permutations (Grid View):")

        # Generate permutations
        results = permute_backtracking(list(user_input), results=[])
        
        # Grid visualization settings
        cols_per_row = min(6, len(results))  # Max 6 columns
        rows = math.ceil(len(results) / cols_per_row)

        placeholders = [st.empty() for _ in range(len(results))]  # Placeholders for animation

        # Styling for permutation boxes
        box_style = """
        <div style='
            background-color: black;
            color: white;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            padding: 10px;
            border-radius: 10px;
            margin: 5px;
        '>{}</div>
        """

        if visualize_steps:
            for i, p in enumerate(results):
                placeholders[i].markdown(box_style.format(p), unsafe_allow_html=True)
                time.sleep(animation_speed)  # Slow down for visualization
        else:
            # Display in grid layout
            cols = st.columns(cols_per_row)
            for i, p in enumerate(results):
                with cols[i % cols_per_row]:  
                    st.markdown(box_style.format(p), unsafe_allow_html=True)
