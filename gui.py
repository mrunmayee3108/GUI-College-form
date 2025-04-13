from tkinter import *

def onsubmit():
   name = entry1.get()
   branch = branch_var.get()
   games = cricket_var.get(), football_var.get(), badminton_var.get()
   
   game_names = []
   if games[0]: game_names.append("Cricket")
   if games[1]: game_names.append("Football")
   if games[2]: game_names.append("Badminton")
   
   labelonsubmit.config(text = f"OUTPUT: \n Your name is {name}. \n {name} is from {branch} Department.\n {name} is from {branch} Department and enjoys playing {', '.join(game_names) if game_names else 'nothing'}.")
   labelonsubmit.grid(row=5, column = 1,columnspan = 4, padx = 10, pady = 10, sticky = 'w')
   
root = Tk()
root.title("College admission registration form")
root.geometry('600x600')

label1 = Label(root, text="Enter Student Name:")
label1.grid(row=1, column=1, padx=10, pady=10, sticky='e')

entry1 = Entry(root, width=40)
entry1.grid(row=1, column=2, padx=10, pady=10)

branch_var = StringVar()

label2 = Label(root, text="Select your branch:")
label2.grid(row=2, column=1, padx=10, pady=10, sticky='e')

Radiobutton(root, text="Computer Engineering",variable = branch_var, value="Computer Engineering").grid(row=2, column=2, padx=10, pady=10, sticky='w')
Radiobutton(root, text="Information Technology",variable = branch_var, value="Information Technology").grid(row=2, column=3, padx=10, pady=10, sticky='w')
Radiobutton(root, text="Artificial Intelligence and Data Science",variable = branch_var, value="Artificial Intelligence and Data Science").grid(row=2, column=4, padx=10, pady=10, sticky='w')

label3 = Label(root, text="Select favourite games:")
label3.grid(row=3, column=1, padx=10, pady=10, sticky='e')

cricket_var = IntVar()
football_var = IntVar()
badminton_var = IntVar()

Checkbutton(root, text="Cricket", variable = cricket_var).grid(row=3, column=2, padx=10, pady=10, sticky='w')
Checkbutton(root, text="Football", variable = football_var).grid(row=3, column=3, padx=10, pady=10, sticky='w')
Checkbutton(root, text="Badminton", variable = badminton_var).grid(row=3, column=4, padx=10, pady=10, sticky='w')

button = Button(root, text = "Submit", command=onsubmit).grid(row=4, column=1, columnspan=4, padx=10, pady=20)
labelonsubmit = Label(root, text = "", justify=LEFT)

root.mainloop()
