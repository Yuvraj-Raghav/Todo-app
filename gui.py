
import functions

import FreeSimpleGUI as sg
import  time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt",'w') as file:
        pass
sg.theme("Black")

clock = sg.Text('',key = 'clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo",key = "todo")
add_button =sg.Button("Add",size=10,)

list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica',20))

while True:
    event ,values= window.read(timeout=200)

    if event in (sg.WIN_CLOSED,'Exit'):
        break
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
                new_todo = values['todo'].strip()
                if new_todo=="":
                    sg.popup("Please enter a to-do item")
                else:
                    todos = functions.get_todos()
                    todos.append(new_todo +"\n")
                    functions.write_todos(todos)
                    window['todos'].update(values = todos)
        case "Edit":
            try:
              todo_to_edit = values['todos'][0]
              new_todo = values['todo']
              if new_todo=="":
                  sg.popup("Please Enter a new value to Edit.")
              else:
                  todos = functions.get_todos()
                  index = todos.index(todo_to_edit)
                  todos[index] = new_todo
                  functions.write_todos(todos)
                  window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",font=("Helvetica",20))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = "")
            except IndexError:
                sg.popup("Please select an item first",font=("Helvetica",20))




window.close()
