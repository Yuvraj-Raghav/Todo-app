#from functions import get_todos ,write_todos
#imports the get_todos and write_todo function from the function.py file
#import functions
import  time
#Use for importing date and time functions so that we can use in our code
now = time.strftime("%B %d, %Y %H:%M:%S")
print('It is', now)
while True:
    #This section is for user Input
    user_action = input("Type add , show , edit , complete or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()
    if user_action.startswith("add") :
            todo = user_action[4:]

            todos = functions.get_todos('todos.txt')
            todos.append(todo + '\n')

            functions.write_todos(todos)

    elif user_action.startswith("show"):

            todos = functions.get_todos()

            #new_todos=[item.strip('\n') for item in todos] ----> This is inline for loop that strips '\n' from string
            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                row = f"{index+1}-{item}"
                print(row)
    elif user_action.startswith("edit"):
            #Exception Handling
            try:
                number = int(user_action[5:])

                number = number - 1

                todos = functions.get_todos()


                new_todo = input("Enter New Todo: ")

                todos[number] = new_todo + '\n'

                functions.write_todos(todos)

            except ValueError:
                print("Your command is not valid.""\n"
                      "you have to Enter a Number to edit")
                continue

    elif user_action.startswith("complete"):
        try:
                number = int(user_action[9:])

                todos = functions.get_todos()

                removed_todo = todos[number - 1].strip('\n')
                todos.pop(number - 1)

                functions.write_todos(todos)

                message = f"Todo {removed_todo} was removed from the ToDo list"
                print(message)
        except IndexError:
            print("The Number doesnt exits in the Todo List")
            continue
        except ValueError:
            print("You have to enter a number of the completed item")
            continue
    elif user_action.startswith("exit"):
            break
    else:
        print("Hey you Entered a Wrong command")
print("Bye!")


