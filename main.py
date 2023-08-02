import tkinter as tk

window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

var = tk.IntVar()
R1 = tk.Radiobutton(window, text = "Option 1", variable = var, value = 1)
R1.grid(column = 0, row = 0)

R2 = tk.Radiobutton(window, text = "Option 2", variable=var, value = 2)
R2.grid(column = 1, row = 0)

def printOption():
    value = var.get()
    print(value)

button = tk.Button(window, text = "Click Here", command = printOption)
button.grid(column = 0, row = 1)

window.mainloop()