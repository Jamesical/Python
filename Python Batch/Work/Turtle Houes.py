import turtle

t = turtle.Turtle() 

def r():
    t.lt(90)
    t.forward(250)

    t.rt(90)

    for i in range (19):
        t.forward(10)
        t.rt(10)

    t.lt(125)
    t.forward(150)

    

def stolen():
    a = input("Enter Name: ")
    turtle.color('deep pink')
    style = ('Courier', 30, 'italic')
    turtle.write(a, font=style, align='center')

    
        
    

r()
#stolen()




turtle.mainloop()
