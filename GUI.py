import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo")
window = sg.Window('My To-Do App', layout=[""])
window.read()
window.close()
