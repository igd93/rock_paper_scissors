import tkinter as tk

window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

myCanvas = tk.Canvas(window, bg = "lightblue", height = 300, width = 300)
myCanvas.grid(row=0, column=0)

myLine = myCanvas.create_line(50, 70, 220, 40, fill="blue")

myOval = myCanvas.create_oval(40, 75, 120, 150, fill="green")

myArc = myCanvas.create_arc(175, 145, 75, 200, start=0, extent=220, fill="yellow")

window.mainloop()
