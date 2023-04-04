import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]], font=('Kanit, sans-serif', 16))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos("todos.txt", todos)
window.close()
