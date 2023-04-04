import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="items", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button], [list_box, edit_button]], font=('Kanit, sans-serif', 16))
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
            window['items'].update(values=todos)

        case "Edit":
            item = value['items'][0]
            new_item = value['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(item)
            todos[index] = new_item
            functions.write_todos("todos.txt", todos)
            window['items'].update(values=todos)

        case "items":
            window['todo'].update(value=value['items'][0])
        case sg.WINDOW_CLOSED:
            break

window.close()
