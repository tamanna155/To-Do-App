import functions
import PySimpleGUI as sg
import time
sg.theme("Black")
clock = sg.Text(" ", key="watch")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="items", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
window = sg.Window('My To-Do App', layout=[[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button]], font=('Kanit, sans-serif', 16))
while True:
    event, value = window.read(timeout=200)
    window['watch'].update(value=time.strftime("%B %d, %Y %H:%M:%S"))
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
            try:
                item = value['items'][0]
                new_item = value['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(item)
                todos[index] = new_item
                functions.write_todos("todos.txt", todos)
                window['items'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Kanit', 16), button_color='red')

        case "Complete":
            comp = value['items'][0]
            todos = functions.get_todos()
            todos.remove(comp)
            functions.write_todos("todos.txt", todos)
            window['items'].update(values=todos)
            window['todo'].update(values="")

        case "items":
            window['todo'].update(value=value['items'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()