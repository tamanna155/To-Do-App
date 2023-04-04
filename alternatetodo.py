import functions
import time
name = time.strftime("%B %d, %Y %H:%M:%S")
print("(The time is printed using time.strftime() function)")
print("It is", name)
while True:
    user_action = input("Type \n 1.Add 2.Show 3.Edit 4.Complete 5.Exit \n")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        item = user_action.strip("add")
        todo = functions.get_todos()
        todo.append(item + "\n")
        functions.write_todos("todos.txt", todo)
    elif user_action.startswith("show"):
        todo = functions.get_todos()
        new_todos = []
        for items in todo:
            new_item = items.strip("\n")
            new_todos.append(new_item)
        for index, items in enumerate(new_todos):
            index = index + 1
            print(index, items)
    elif user_action.startswith("edit"):
        try:
            edit = int(user_action.strip("edit"))
            new = input("Enter the updated todo: ")
            todo = functions.get_todos()
            print("the old list is: ", todo)
            num = edit - 1
            todo[num] = new + "\n"
            functions.write_todos("todos.txt", todo)
            print("the new list is: ", todo)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("complete"):
        complete = int(user_action.strip("complete"))
        try:
            todo = functions.get_todos()
            num = complete - 1
            element = todo[num].strip("\n")
            todo.pop(num)
            functions.write_todos("todos.txt", todo)
        except IndexError:
            print("There is no value existing with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
