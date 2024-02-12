# from tkinter import *
#
# # root = Tk()
# #
# # my_label1 = Label(root, text="Hello world:")
# # my_label2 = Label(root, text="hello motherfucker")
# #
# # my_label1.grid(row=0, column=0)
# # my_label2.grid(row=1, column=0)
# #
# # root.mainloop()

#Create a button!!!

# from tkinter import *
#
# root = Tk()
#
# my_button = Button(root, text="Click me!")
# my_button.pack()
#
# root.mainloop()


#Create a button and fix its size
#padx = wide, pady = height
#fg = "blue" (make text calor on the button)
#bg = "yellow" (make background color on the button)
# from tkinter import *
#
# root = Tk()
#
# def my_button_does():
#     my_text = Label(root, text="Congratulation you have created a button for the first time")
#     my_text.pack()
#
# my_button = Button(root, text="Click me!", command=my_button_does, fg="Green", bg="yellow")
# my_button.pack()
#
# root.mainloop()


# button and field for filling

# from tkinter import *
#
# root = Tk()
#
# e = Entry(root, width=50, bg="blue", fg="yellow")
# e.pack()
# e.get() # this mean take from field.
# e.insert(0, "enter your name")
# def my_button_does():
#     my_text = Label(root, text="This is not your true name")
#     my_text.pack()
#
# my_button = Button(root, text="Click me!", command=my_button_does, fg="Green", bg="yellow")
# my_button.pack()
#
# root.mainloop()


#Calculator

from tkinter import *

root = Tk()
root.title("Simple calculator")

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, pady=10)

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

    return

def add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def subtraction():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def multiplication():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def dividion():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def clear():
    e.delete(0, END)

def equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))





button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click("1"))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click("2"))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click("3"))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click("4"))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click("5"))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click("6"))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click("7"))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click("8"))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click("9"))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click("0"))
button_add = Button(root, text="+", padx=40, pady=20, command=add)
button_equal = Button(root, text="=", padx=40, pady=20, command=equal)
button_subtraction = Button(root, text="-", padx=40, pady=20, command=subtraction)
button_multiplication = Button(root, text="x", padx=40, pady=20, command=multiplication)
button_divide = Button(root, text="/", padx=40, pady=20, command=dividion)
button_clear = Button(root, text="CLEAR", padx=25, pady=20, command=clear)


button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)
button_3.grid(row=1, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)
button_9.grid(row=3, column=3)

button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=3)

button_add.grid(row=1, column=4)
button_divide.grid(row=4, column=4)
button_multiplication.grid(row=3, column=4)
button_subtraction.grid(row=2, column=4)

button_clear.grid(row=4, column=2)


root.mainloop()