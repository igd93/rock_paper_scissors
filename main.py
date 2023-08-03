import tkinter as tk

window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

myLabel = tk.Label(window, text="Enter your address: ")
myLabel.grid(column = 0, row = 0)
myText = tk.Text(window, height = 10, width = 20)
myText.grid(column = 1, row = 0)

def inputData():
    address = myText.get("1.0", "end")
    print(address)

myButton = tk.Button(window, text = "Submit", command = inputData)
myButton.grid(column= 0, row = 1)

window.mainloop()