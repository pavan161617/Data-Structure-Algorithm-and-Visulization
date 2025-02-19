import streamlit as st
import matplotlib.pyplot as plt
from collections import deque
import re

def is_valid_expression(expression):
    """Validates if the expression contains only allowed characters."""
    return bool(re.match(r'^[A-Za-z0-9+\-*/^()]+$', expression))

def infix_to_postfix(expression):
    if not is_valid_expression(expression):
        return "Invalid expression!"
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = ''
    for char in expression:
        if char.isalnum():
            output += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                output += stack.pop()
            stack.append(char)
    while stack:
        output += stack.pop()
    return output

def infix_to_prefix(expression):
    expression = expression[::-1]
    expression = ['(' if char == ')' else ')' if char == '(' else char for char in expression]
    postfix = infix_to_postfix(expression)
    return postfix[::-1]

def postfix_to_infix(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            if len(stack) < 2:
                return "Invalid Postfix Expression!"
            b = stack.pop()
            a = stack.pop()
            stack.append(f'({a}{char}{b})')
    return stack[0]

def prefix_to_infix(expression):
    stack = []
    for char in reversed(expression):
        if char.isalnum():
            stack.append(char)
        else:
            if len(stack) < 2:
                return "Invalid Prefix Expression!"
            a = stack.pop()
            b = stack.pop()
            stack.append(f'({a}{char}{b})')
    return stack[0]

class Stack:
    def __init__(self):
        self.stack = deque()
        self.index = 0  # Ensuring sequential insertion
    
    def push(self, value):
        self.stack.append((self.index, value))
        self.index += 1  # Increment index for the next value
    
    def pop(self):
        if self.stack:
            self.index -= 1
            return self.stack.pop()[1]
        return 'Stack is empty'
    
    def peek(self):
        return self.stack[-1][1] if self.stack else 'Stack is empty'
    
    def display(self):
        return [item[1] for item in self.stack]
    
    def clear(self):
        self.stack.clear()
        self.index = 0
    
    def visualize(self):
        fig, ax = plt.subplots()
        values = [item[1] for item in self.stack]
        indices = [item[0] for item in self.stack]
        ax.bar(indices, values, color='lightblue')
        ax.set_xticks(indices)
        ax.set_xticklabels(indices)
        ax.set_xlabel("Stack Index")
        ax.set_ylabel("Values")
        ax.set_title("Stack Visualization")
        if self.stack:
            ax.text(indices[-1], values[-1] + 0.5, 'Top', ha='center', color='red', fontsize=12)
        return fig

# Initialize stack in session state
if 'stack' not in st.session_state:
    st.session_state.stack = Stack()

stack = st.session_state.stack

st.title("Expression Conversion & Stack Visualization")
option = st.sidebar.selectbox("Choose Operation", [
    "Infix to Postfix", "Infix to Prefix", "Postfix to Infix", "Prefix to Infix", "Stack Operations"])

if option in ["Infix to Postfix", "Infix to Prefix", "Postfix to Infix", "Prefix to Infix"]:
    expr = st.text_area("Enter Expression:")
    if st.button("Convert"):
        if option == "Infix to Postfix":
            result = infix_to_postfix(expr)
        elif option == "Infix to Prefix":
            result = infix_to_prefix(expr)
        elif option == "Postfix to Infix":
            result = postfix_to_infix(expr)
        elif option == "Prefix to Infix":
            result = prefix_to_infix(expr)
        st.write("Converted Expression:", result)

elif option == "Stack Operations":
    operation = st.radio("Choose Stack Operation", ["Push", "Pop", "Peek", "Display", "Clear Stack"])
    if operation == "Push":
        value = st.number_input("Enter Value to Push", step=1, value=0)
        if st.button("Push"):
            stack.push(value)
            st.write("Stack after Push:", stack.display())
            st.pyplot(stack.visualize())
    elif operation == "Pop":
        if st.button("Pop"):
            popped_value = stack.pop()
            st.write("Popped Value:", popped_value)
            st.write("Stack after Pop:", stack.display())
            st.pyplot(stack.visualize())
    elif operation == "Peek":
        if st.button("Peek"):
            st.write("Top of Stack:", stack.peek())
    elif operation == "Display":
        st.write("Current Stack:", stack.display())
        st.pyplot(stack.visualize())
    elif operation == "Clear Stack":
        if st.button("Clear"):
            stack.clear()
            st.write("Stack Cleared!")
            st.pyplot(stack.visualize())