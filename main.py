import tkinter as tk

window = tk.Tk()
window.title("My first GUI App")
window.geometry("1000x600")

# first name
fNameLabel = tk.Label(text="First Name: ")
fNameLabel.grid(column=0, row=0)
fNameEntry = tk.Entry(window)
fNameEntry.grid(column=1, row=0)
# last name
lNameLabel = tk.Label(text="Last Name: ")
lNameLabel.grid(column=0, row=1)
lNameEntry = tk.Entry(window)
lNameEntry.grid(column=1, row=1)
# address
addressLabel = tk.Label(text="Address: ")
addressLabel.grid(column=0, row=2)
addressText = tk.Text(window, height=4, width=15)
addressText.grid(column=1, row=2)
# nationality Options Menu
nationLabel = tk.Label(text="Nationality: ")
nationLabel.grid(column=0, row=3)
nationaVar = tk.StringVar(window)
nationaVar.set("Select")
opMenu = tk.OptionMenu(window, nationaVar, "North America",
                       "South America", "Europe", "Asia", "Pacific")
opMenu.grid(column=1, row=3)

genderLabel = tk.Label(text="Gender: ")
genderLabel.grid(column=0, row=4)
genderVar = tk.StringVar()
R1 = tk.Radiobutton(window, text="Male", variable=genderVar, value="Male")
R1.grid(column=1, row=4)
R2 = tk.Radiobutton(window, text="Female", variable=genderVar, value="Female")
R2.grid(column=2, row=4)
# T&C check button
termsVar = tk.IntVar()
C1 = tk.Checkbutton(window, text="I agree to T&C",
                    variable=termsVar, onvalue=1, offvalue=0, height=2, width=17)
C1.grid(column=1, row=5)

# method to print data to the cli


def printData():
    print(fNameEntry.get())
    print(lNameEntry.get())
    print(addressText.get("1.0", "end"))
    print(nationaVar.get())
    print(genderVar.get())
    print(termsVar.get())


button = tk.Button(window, text="Submit", command=printData)
button.grid(column=0, row=6)


window.mainloop()
