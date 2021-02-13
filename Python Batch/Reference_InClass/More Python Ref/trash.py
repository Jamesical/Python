import turtle as t

def parallelLines(length, reps, separation):
    t.forward(length)
    t.rt(90)
    t.pu()
    t.forward(100)
    t.rt(90)
    t.forward(length)
parallelLines(100, 100, 100)
