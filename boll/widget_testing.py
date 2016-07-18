import tkinter

def button1_command():
    print('button1 def')

def print_hello(event):

    print(event.num)
    print(event.x, event.y)

    me = event.widget
    if me == button1:
        print('Hello')
    elif me == button2:
        print('but2')
    else:
        raise  ValueError()

def init_main_windowq():
    global root, button1, button2, label, text, scale

    root = tkinter.Tk()

    button1 = tkinter.Button(root, text="Button", command=button1_command)
    button1.bind("<Button>", print_hello)
    button1.pack()

    button2 = tkinter.Button(root, text="Button")
    button2.bind("<Button-1>", print_hello)
    button2.pack()

    variable = tkinter.IntVar(0)
    label = tkinter.Label(root, text=variable)
    scale = tkinter.Scale(root, orient=tkinter.HORIZONTAL, lenght=300,
                          from_=0, to=100, tickinterval=10, resolution=5, variable=variable)
    text = tkinter.Entry(root, textvariable=variable)

    for obj in button1, button2, label, scale, text:
        obj.pack()

if __name__ == '__main__':
    init_main_windowq()
    root.mainloop()