#!/bin/bash

TODO_FILE="$HOME/.todo_list"  # File to store tasks

# Check if the TODO file exists, if not, create it
if [ ! -f "$TODO_FILE" ]; then
    touch "$TODO_FILE"
fi

# Function to show the menu
show_menu() {
    clear
    echo "----------------------------"
    echo "     To-Do List Manager"
    echo "----------------------------"
    echo "1. View To-Do List"
    echo "2. Add a Task"
    echo "3. Remove a Task"
    echo "4. Mark Task as Complete"
    echo "5. Exit"
    echo "----------------------------"
    echo -n "Choose an option: "
}

# Function to view the to-do list
view_tasks() {
    echo "----------------------------"
    echo "Your To-Do List"
    echo "----------------------------"
    if [ ! -s "$TODO_FILE" ]; then
        echo "No tasks in your to-do list."
    else
        cat -n "$TODO_FILE"
    fi
    echo "----------------------------"
    read -n 1 -s -r -p "Press any key to return to the menu..."
}

# Function to add a task
add_task() {
    echo -n "Enter the task description: "
    read task
    if [ -n "$task" ]; then
        echo "$task" >> "$TODO_FILE"
        echo "Task added!"
    else
        echo "Task description cannot be empty."
    fi
    read -n 1 -s -r -p "Press any key to return to the menu..."
}

# Function to remove a task
remove_task() {
    view_tasks
    echo -n "Enter the task number to remove: "
    read task_number
    if [ -n "$task_number" ] && [ "$task_number" -gt 0 ]; then
        sed -i "${task_number}d" "$TODO_FILE"
        echo "Task removed!"
    else
        echo "Invalid task number."
    fi
    read -n 1 -s -r -p "Press any key to return to the menu..."
}

# Function to mark a task as complete
mark_complete() {
    view_tasks
    echo -n "Enter the task number to mark as complete: "
    read task_number
    if [ -n "$task_number" ] && [ "$task_number" -gt 0 ]; then
        sed -i "${task_number}s/$/ [Completed]/" "$TODO_FILE"
        echo "Task marked as complete!"
    else
        echo "Invalid task number."
    fi
    read -n 1 -s -r -p "Press any key to return to the menu..."
}

# Main loop to display the menu and handle user input
while true; do
    show_menu
    read choice
    case $choice in
        1) view_tasks ;;
        2) add_task ;;
        3) remove_task ;;
        4) mark_complete ;;
        5) echo "Goodbye!"; exit 0 ;;
        *) echo "Invalid option. Please try again."; read -n 1 -s -r -p "Press any key to continue..." ;;
    esac
done
