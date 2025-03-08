# 🖥️ Data Structure Algorithm and Visualization  

## 📌 Project Overview  
**Data Structure Algorithm and Visualization** is an **interactive web application** designed to help users **understand and visualize** fundamental **Data Structures and Algorithms (DSA)**.  
It provides **real-time animations**, **step-by-step execution**, and **performance insights** for various DSA concepts, making learning more **engaging and intuitive**.  

---

## 🚀 Features  

✅ **Algorithm Visualizations**  
- Step-by-step execution with **interactive animations**.  
- Dynamic updates for **sorting, searching, stacks, queues, graphs, and recursion**.  
- **Color-coded** highlighting for better understanding.  

✅ **User-friendly Interface**  
- **Dashboard** with categorized algorithm tiles.  
- **Parameter sliders & dropdowns** for custom input.  
- **Visualization canvas** for real-time rendering.  

✅ **Performance Metrics**  
- **Sorting**: Number of swaps, comparisons, time complexity.  
- **Searching**: Steps taken, comparisons.  
- **Graphs**: BFS, DFS traversal order, shortest path calculations.  

✅ **Graphical Representations**  
- **Sorting**: Bar graphs representing element swaps.  
- **Searching**: Highlighted step-by-step element lookups.  
- **Graph Algorithms**: Node-edge visualizations using **NetworkX**.  

✅ **Dataset Options**  
- Custom input via text fields.  
- Predefined sample datasets for quick testing.  

---

## 📊 Supported Algorithms  

### ✅ Sorting  
- **Bubble Sort**  
- **Selection Sort**  
- **Insertion Sort**  
- **Merge Sort**  
- **Quick Sort**  

### ✅ Searching  
- **Linear Search**  
- **Binary Search**  

### ✅ Stack & Queue  
- **Stack Operations (Push, Pop, Peek, Display)**  
- **Queue Operations (Enqueue, Dequeue, Display)**  

### ✅ Graph Algorithms  
- **Breadth-First Search (BFS)**  
- **Depth-First Search (DFS)**  
- **Dijkstra's Algorithm**  

### ✅ Recursion & Backtracking  
- **Factorial, Fibonacci (Recursion)**  
- **N-Queens Problem**  
- **Knapsack Problem**  

---

## 🖥 System Requirements  

| Component      | Requirement              |  
|--------------|------------------------|  
| Python Version | 3.8+                    |  
| Libraries     | `numpy`, `pandas`, `matplotlib`, `networkx`, `streamlit` |  

---

## 📂 Project Structure  

```bash
📦 Data-Structure-Algorithm-and-Visualization
│── 📁 modules          # Contains algorithm implementations
│── 📁 assets           # Stores UI assets & images
│── 📄 app.py           # Main Streamlit application
│── 📄 requirements.txt # Dependencies list
│── 📄 README.md        # Project Documentation

🔧 Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/pavan161617/Data-Structure-Algorithm-and-Visulization.git
cd Data-Structure-Algorithm-and-Visulization
2️⃣ Create a Virtual Environment
python -m venv venv  
source venv/bin/activate   # On Windows: venv\Scripts\activate  
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
streamlit run ds_visualization.py

📜 Usage
Open the App in your browser (http://localhost:8501).
Select the Algorithm Category:
Sorting
Searching
Stack & Queue
Graphs
Recursion & Backtracking
Choose a specific algorithm from the dropdown.
Provide custom input or use predefined datasets.
Click Visualize to see:
Step-by-step execution
Algorithm logic visualization
Performance metrics (like swaps, comparisons, traversal order, etc.)
Graphical plots (bar charts, tree structures, graph edges, etc.)

📦 Example Output
Selected Algorithm:
Quick Sort

Input Array: [9, 5, 1, 4, 3]

Visualization:
✅ Pivot Selection highlighted.
✅ Partitions Swapping animated.
✅ Sorted Array: [1, 3, 4, 5, 9]

🏅 Future Enhancements
Add more algorithms (AVL Trees, Heap Sort, Graph Shortest Paths).
Optimize performance for large datasets.
Support interactive animations with better UI/UX.
Add explanations for theoretical understanding.
Allow saving visualizations as GIFs.

🤝 Contributing
🔹 Found a bug? Open an issue.
🔹 Want to add a new feature? Fork & contribute.
🔹 Star ⭐ this repo if you like the project!

📧 Contact
Developer: Pavan Kumar
GitHub: pavan161617
LinkedIn: Pavan Kumar

⭐ If you like this project, please star the repository! ⭐
This `README.md` is **structured, visually appealing, and highly professional**.

