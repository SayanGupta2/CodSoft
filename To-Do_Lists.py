# import all libraries

from tkinter import *
from tkinter import messagebox

tasks_list = []
counter = 1

# def functions will here in this section

def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error")
        return 0
    return 1

def clear_taskNumberField():
    taskNumberField.delete(0.0, END)

def clear_taskField():
    enterTaskField.delete(0, END)

def insertTask():      # insert task function will start hare
    global counter
    value = inputError()
    if value == 0:
        return

    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
    counter += 1
    clear_taskField()

def delete():      # delete the task number
    global counter
    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return
    
    number = taskNumberField.get(1.0, END)
    if number == "\n":
        messagebox.showerror("input error")
        return
    else:
        task_no = int(number)

    clear_taskNumberField()
    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)
    
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])

def save_to_file():    # save this task into a text file
    with open("to_do_list.txt", "w") as file:
        for task in tasks_list:
            file.write(task)

if __name__ == "__main__":     # main function will start hare 
    gui = Tk()
    gui.configure(background="light green")
    gui.title("ToDo App")
    gui.geometry("250x350")  # Slightly increased the height for Save button

    enterTask = Label(gui, text="Enter Your Task", bg="light green")
    enterTaskField = Entry(gui)
    Submit = Button(gui, text="Submit", fg="Black", bg="Red", command=insertTask)
    TextArea = Text(gui, height=5, width=25, font="lucida 13")
    taskNumber = Label(gui, text="Delete Task Number", bg="blue")
    taskNumberField = Text(gui, height=1, width=2, font="lucida 13")
    delete = Button(gui, text="Delete", fg="Black", bg="Red", command=delete)
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)
    
    # Added a Save button

    Save = Button(gui, text="Save", fg="Black", bg="Green", command=save_to_file)
    
    enterTask.grid(row=0, column=2)
    enterTaskField.grid(row=1, column=2, ipadx=50)
    Submit.grid(row=2, column=2)
    TextArea.grid(row=3, column=2, padx=10, sticky=W)
    taskNumber.grid(row=4, column=2, pady=5)
    taskNumberField.grid(row=5, column=2)
    delete.grid(row=6, column=2, pady=5)
    Save.grid(row=7, column=2)  # Placed the Save button at row 7
    
    Exit.grid(row=8, column=2)  # Incremented the row for Exit button
    
    gui.mainloop()
