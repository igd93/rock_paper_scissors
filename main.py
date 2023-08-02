import tkinter as tk

def hello(event):
    print("Hello world")

window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

label_name = tk.Label(text = "Hello world")
label_name.grid(column= 0, row = 0)

my_button = tk.Button(window, text= "some text")
my_button.grid(column = 1, row = 0)
my_button.bind("<Button-1>", hello)


window.mainloop()