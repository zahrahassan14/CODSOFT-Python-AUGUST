from tkinter import *
from tkinter import messagebox

task_list = []

def AddTask():
    newtask = new_list.get()
    if newtask != "":
        lb.insert(END, newtask)
        task_list.append({'task': newtask, 'done': False})
        new_list.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Add a task!")

def DeleteTask():
    selected_index = lb.curselection()
    if selected_index:
        index = selected_index[0]
        del task_list[index]
        lb.delete(index)
        UpdateCompletedList()

def UpdateList():
    lb.delete(0, END)
    for task in task_list:
        task_text = f"[{'✓' if task['done'] else ' '}] {task['task']}"
        lb.insert(END, task_text)

def MarkAsDone():
    selected_index = lb.curselection()
    if selected_index:
        for index in selected_index:
            if 0 <= index < len(task_list):
                task_list[index]['done'] = True
        UpdateList()
        UpdateCompletedList()
    else:
        messagebox.showwarning("Warning", "Select a task to mark as done.")

def UpdateCompletedList():
    completed_lb.delete(0, END)
    for task in task_list:
        if task['done']:
            completed_lb.insert(END, task['task'])

td = Tk()
td.title("To Do List")
td.config(bg='#ffc3c3')
td.geometry('800x550+500+200')
td.resizable(height=True, width=True)

frame = Frame(td)
frame.pack(pady=10)

task_frame = Frame(frame)
task_frame.pack(side=LEFT, padx=10)

completed_frame = Frame(frame)
completed_frame.pack(side=LEFT, padx=10)

task_title = Label(task_frame,text="Text List", font=('Calibri',16))
task_title.pack(pady=(0,10))

lb = Listbox(
    task_frame,
    height=10,
    width=30,
    bd=0,
    fg='#222222',
    font=('Calibri', 18),
    highlightthickness=0
)
lb.pack(fill=BOTH)

completed_title = Label(completed_frame,text="Completed List", font=('Calibri',16))
completed_title.pack(pady=(0,10))

completed_lb = Listbox(
    completed_frame,
    height=10,
    width=30,
    bd=0,
    font=('Calibri', 18),
    highlightthickness=0,
    fg='#222222'
)
completed_lb.pack(fill=BOTH, side=LEFT)


new_list = Entry(td, font=('Calibri', 20))
new_list.pack(pady=20)

btn_frame = Frame(td)
btn_frame.pack(pady=20)

add_btn = Button(
    btn_frame,
    font=('Calibri', 14),
    pady=5,
    padx=10,
    text='Add to List',
    command=AddTask,
    bg='#008000'
)
add_btn.grid(row=0, column=0, padx=5, pady=5)

delete_btn = Button(
    btn_frame,
    font=('Calibri', 14),
    pady=5,
    padx=10,
    text='Delete Task',
    command=DeleteTask,
    bg='#880808'
)
delete_btn.grid(row=0, column=1, padx=5, pady=5)

markdone_btn = Button(
    btn_frame,
    font=('Calibri', 14),
    pady=5,
    padx=10,
    text='Mark as Done',
    command=MarkAsDone,
    bg='#808080'
)
markdone_btn.grid(row=0, column=2, padx=5, pady=5)

UpdateList()
UpdateCompletedList()

td.mainloop()
