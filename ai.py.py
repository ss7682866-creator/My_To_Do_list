import streamlit as st

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="To-Do List",
    page_icon="✅",
    layout="centered"
)

# -----------------------------
# Initialize session state
# -----------------------------
# Tasks are stored as a list of dictionaries.
# Session state keeps the tasks available during the current session.
if "tasks" not in st.session_state:
    st.session_state.tasks = []


# -----------------------------
# Function to add a new task
# -----------------------------
def add_task(task_name):
    if task_name.strip():
        st.session_state.tasks.append({
            "task": task_name.strip(),
            "completed": False
        })


# -----------------------------
# Function to delete a task
# -----------------------------
def delete_task(task_index):
    st.session_state.tasks.pop(task_index)


# -----------------------------
# Function to clear completed tasks
# -----------------------------
def clear_completed_tasks():
    st.session_state.tasks = [
        task for task in st.session_state.tasks
        if not task["completed"]
    ]


# -----------------------------
# Application title
# -----------------------------
st.title("✅ To-Do List")
st.write("A simple task manager built with Python and Streamlit.")

# -----------------------------
# Add a new task
# -----------------------------
st.subheader("Add a New Task")

task_input = st.text_input(
    "Enter your task:",
    placeholder="Example: Complete Python assignment"
)

if st.button("➕ Add Task"):
    if task_input.strip():
        add_task(task_input)
        st.success("Task added successfully!")
        st.rerun()
    else:
        st.warning("Please enter a task.")


# -----------------------------
# Task statistics
# -----------------------------
total_tasks = len(st.session_state.tasks)

completed_tasks = sum(
    1 for task in st.session_state.tasks
    if task["completed"]
)

st.subheader("Task Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Tasks", total_tasks)

with col2:
    st.metric("Completed Tasks", completed_tasks)


# -----------------------------
# Display tasks
# -----------------------------
st.subheader("My Tasks")

if not st.session_state.tasks:
    st.info("No tasks available. Add a new task above!")

else:
    for index, task in enumerate(st.session_state.tasks):

        col1, col2 = st.columns([4, 1])

        # Checkbox for completing the task
        with col1:
            completed = st.checkbox(
                task["task"],
                value=task["completed"],
                key=f"task_{index}"
            )

            # Update task completion status
            st.session_state.tasks[index]["completed"] = completed

        # Delete button
        with col2:
            if st.button("🗑️", key=f"delete_{index}"):
                delete_task(index)
                st.rerun()


# -----------------------------
# Clear completed tasks
# -----------------------------
if completed_tasks > 0:
    st.divider()

    if st.button("🧹 Clear Completed Tasks"):
        clear_completed_tasks()
        st.success("Completed tasks cleared!")
        st.rerun()