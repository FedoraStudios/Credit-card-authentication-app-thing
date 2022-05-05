from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()
root.title("Credit Card Authentication")
root.geometry("600x400")

root.configure(background="light gray")

input_box = Entry()
input_box.place(relx=0.5, rely=0.3, anchor = CENTER)

BankName = Label(root, text="Bank of America", bg="red", fg = "blue", font="bold")
BankName.place(relx = 0.5 , rely = 0.05 , anchor = CENTER)

img=ImageTk.PhotoImage(Image.open ("credit.jpg"))
label = Label(root, image=img)
 

def authentication():
        try:
            input_value = int(input_box.get())
            messagebox.showinfo("Welcome","Your credit card has been accepted.")
        except(ValueError):
            messagebox.showinfo("Error", "Please enter a valide pin number")
            


btn = Button(root, text = "validate credit card", command = authentication)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)
label.place(relx=0.5, rely=0.7, anchor = CENTER)

root.mainloop()