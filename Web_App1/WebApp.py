import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos("todos.txt", todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")
for index, data in enumerate(todos):
    checkbox = st.checkbox(data, key=f'checkbox_{index}')
    if checkbox:
        todos.pop(index)
        functions.write_todos("todos.txt", todos)
        del st.session_state[f'checkbox_{index}']
        st.experimental_rerun()

st.text_input(label='Enter a Todo', placeholder='Add a new todooooo', on_change=add_todo, key='new_todo')
st.session_state
