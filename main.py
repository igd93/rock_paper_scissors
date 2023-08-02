import tkinter as tk

def hello(event):
    print("Hello world")

window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

mylabel = tk.Label(text = "Hello World")
mylabel.pack(side = tk.TOP)


window.mainloop()