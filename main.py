import tkinter as tk

window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

label_name = tk.Label(text = "Hello world")
label_name.grid(column= 0, row = 0)

window.mainloop()