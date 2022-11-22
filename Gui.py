#Import the required Libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(win, text="Please provide the Document", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()


root = Tk()
root.withdraw()
# file_path = filedialog.askopenfilename()
file_path = filedialog.askdirectory()

new_file = input("Name file\n")
open_file = open(f"{file_path}\%s.py" % new_file, 'w')

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= file_path).pack(pady=20)



win.mainloop()