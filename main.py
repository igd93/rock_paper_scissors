import tkinter as tk

window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

frame1 = tk.Frame(window)
frame1.grid(column=0, row=0, padx=10)

frame2 = tk.Frame(window)
frame2.grid(column=1, row=0)

myText = tk.Text(frame1, height=10, width=20)
myText.grid(column=0, row=0)

myLabel = tk.Label(frame2, text="Hello World")
myLabel.grid(column=0, row=0)

myButton = tk.Button(frame2, text="Click here")
myButton.grid(column=0, row=1)

window.mainloop()
