from tkinter import *


def button_clicked():

    miles = round(int(input1.get())*1.6,2)
    km_text.config(text=miles)


window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# Label
input1 = Entry(width=10)
input1.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(column=2, row=0)
equal_label = Label(text="is equal to", font=("Arial", 14, "bold"))
equal_label.grid(column=0, row=1)
km_text = Label(text="0", font=("Arial", 14, "bold"))
km_text.grid(column=1, row=1)
km_label = Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=3)

# Entry

input1 = Entry(width=10)
input1.grid(column=1, row=0)

window.wait_window()
