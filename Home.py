import streamlit as st
import functions_todo


todos = functions_todo.get_todos()
st.set_page_config(layout="wide")
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions_todo.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("Manage your Todos")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions_todo.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label = "", placeholder="Add a new Todo",
              on_change=add_todo, key = 'new_todo')

print("Hello")
st.session_state