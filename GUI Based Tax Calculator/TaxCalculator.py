from tkinter import *


def tax_amount(price, tax):
    cost = price * (tax / 100)
    total_cost = price + cost
    return total_cost


def field1():
    entryField.delete(0, 'end')
    price = price_field.get()
    tax = tax_field.get()
    amount = tax_amount(int(price), int(tax))
    entry.set("The total cost after tax is: ₹" + str(amount))


root = Tk()
root.configure(background="blue4")
root.title("@TK")
root.resizable(1, 0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

entry = StringVar()
entryField = Entry(root, textvariable=entry, background="LightYellow2", foreground="blue4", justify=CENTER)
entryField.grid(row=0, column=0, columnspan=2, sticky=W + E)
entryField.columnconfigure(0, weight=1)

label = Label(root, text="Price", background="blue4", foreground="PaleTurquoise1")
label.grid(row=1, column=0, sticky=E)
tax_price = Label(root, text="Tax amount (%)", background="blue4", foreground="PaleTurquoise1")
tax_price.grid(row=2, column=0, sticky=E)

price_field = Entry(root, background="SkyBlue2", foreground="blue4")
price_field.grid(row=1, column=1, sticky=W)
tax_field = Entry(root, background="SkyBlue2", foreground="blue4")
tax_field.grid(row=2, column=1, sticky=W)

button = Button(root, text="Find total cost", command=field1)
button.grid(row=3, columnspan=2)

root.mainloop()
