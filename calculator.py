'''
    Author: Aleksandar Arsic
    Contact email: srpskaitucionica@gmail.com
    Github: https://github.com/SrpskaITucionica
'''


from tkinter import *


def add_number(number):
    current = calculation_entry_var.get()
    calculation_entry_var.set(str(current) + str(number))


def operation(math_var):
    first_number = calculation_entry_var.get()
    global f_num
    global math
    math = math_var
    f_num = int(first_number)
    calculation_entry_var.set('')


def calculate():
    second_number = calculation_entry_var.get()
    calculation_entry_var.set('')

    try:
        math
    except NameError:
        return None


    if math == "addition":
        calculation_entry_var.set(str(f_num + int(second_number)))

    if math == "subtraction":
        calculation_entry_var.set(str(f_num - int(second_number)))

    if math == "multiplication":
        calculation_entry_var.set(str(f_num * int(second_number)))

    if math == "division":
        calculation_entry_var.set(str(f_num / int(second_number)))


def clear():
    calculation_entry_var.set('')

def set_negative():
    current = calculation_entry_var.get()
    if '-' in current:
        calculation_entry_var.set(current)
        print('aca')
    else:
        calculation_entry_var.set(f'-{current}')

app = Tk()
app.title('Calculator')
app.resizable(False, False)


digits_frame = Frame(app)
signs_frame = Frame(app)

calculation_entry_var = StringVar()

calculation_entry = Entry(app, state='readonly', justify='right', textvariable=calculation_entry_var, font='12px')


num0_button = Button(digits_frame, text='0', padx=40, pady=15, bg='#56dba8', fg='#000', command=lambda: add_number(0))
num1_button = Button(digits_frame, text='1', padx=40, pady=15, bg='#56dba8', fg='#000', command=lambda: add_number(1))
num2_button = Button(digits_frame, text='2', padx=40, pady=15, bg='#56dba8', fg='#000', command=lambda: add_number(2))
num3_button = Button(digits_frame, text='3', padx=40, pady=15, bg='#56dba8', fg='#000', command=lambda: add_number(3))
num4_button = Button(digits_frame, text='4', padx=40, pady=15, bg='#56dba8', fg='#000', command=lambda: add_number(4))
num5_button = Button(digits_frame, text='5', padx=40, pady=15, bg='#56dba8', fg='#000', command=lambda: add_number(5))
num6_button = Button(digits_frame, text='6', padx=40, pady=15, bg='#56dba8', fg='#000', command=lambda: add_number(6))
num7_button = Button(digits_frame, text='7', padx=40, pady=15, bg='#56dba8', fg='#000', command=lambda: add_number(7))
num8_button = Button(digits_frame, text='8', padx=40, pady=15, bg='#56dba8', fg='#000', command=lambda: add_number(8))
num9_button = Button(digits_frame, text='9', padx=40, pady=15, bg='#56dba8', fg='#000', command=lambda: add_number(9))


plus_button = Button(signs_frame, text='+', padx=39, pady=15, bg='#f8ff73', command=lambda: operation('addition'))
minus_button = Button(signs_frame, text='-', padx=40, pady=15, bg='#f8ff73', command=lambda: operation('subtraction'))
divide_button = Button(signs_frame, text='/', padx=40, pady=15, bg='#f8ff73', command=lambda: operation('division'))
multiplication_button = Button(signs_frame, text='*', padx=40, pady=15, bg='#f8ff73', command=lambda: operation('multiplication'))
plus_minus_button = Button(signs_frame, text='+/-',  padx=40, pady=15, bg='#f8ff73', command=set_negative)

equal_button = Button(digits_frame, text='=', padx=40, pady=15, bg='#f2112f', fg='#fff', command=calculate)
clear_button = Button(digits_frame, text='Clear', padx=29, pady=15, bg='#f2112f', fg='#fff', command=clear)

calculation_entry.grid(row=0, column=0, columnspan=4, sticky='we', ipady=6)
digits_frame.grid(row=1, column=0, sticky='wn')
signs_frame.grid(row=1, column=1, rowspan=5, sticky='wns')

num7_button.grid(row=0, column=0)
num8_button.grid(row=0, column=1)
num9_button.grid(row=0, column=2, sticky='w')
num4_button.grid(row=1, column=0)
num5_button.grid(row=1, column=1)
num6_button.grid(row=1, column=2, sticky='w')
num1_button.grid(row=2, column=0)
num2_button.grid(row=2, column=1)
num3_button.grid(row=2, column=2, sticky='w')
num0_button.grid(row=3, column=0, sticky='w')

plus_button.grid(row=0, column=0, sticky='we')
minus_button.grid(row=1, column=0, sticky='we')
divide_button.grid(row=2, column=0, sticky='we')
multiplication_button.grid(row=3, column=0, sticky='we')
plus_minus_button.grid(row=4, column=0, sticky='we')

clear_button.grid(row=3, column=1, columnspan=2, sticky='we')
equal_button.grid(row=4, column=0, columnspan=3, sticky='we')

app.mainloop()
