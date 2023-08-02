import tkinter as tk

window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

myLabel = tk.Label(text = "Select your hobbies: ")
myLabel.grid(column = 0, row = 0)

CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
C1 = tk.Checkbutton(window, text = "Singing", 
                    variable = CheckVar1, onvalue=1, offvalue=0,
                    height=2, width=10)
C1.grid(column= 0 ,row = 1)

C2 = tk.Checkbutton(window, text = "Reading", 
                    variable = CheckVar2, onvalue=1, offvalue=0,
                    height=2, width=10)
C2.grid(column= 0 ,row = 2)

def printCheck():
    value1 = CheckVar1.get()
    value2 = CheckVar2.get()
    print(value1)
    print(value2)

button = tk.Button(window, text = "Submit", command = printCheck)
button.grid(column = 0, row = 3)

window.mainloop()