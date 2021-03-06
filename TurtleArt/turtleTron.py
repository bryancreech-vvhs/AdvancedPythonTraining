from turtle import Turtle, Screen

def main():
    t = Turtle()
    s = Screen()
    s.colormode(255)
    s.bgcolor((76, 237, 87))
    t.color((122, 59, 71))

    s.listen()
    s.onkey(lambda : left(t), 'Left')
    s.onkey(lambda : right(t), 'Right')
    s.onkeypress(lambda : up(t), 'Up')

    s.mainloop()

def left(t):
    t.left(90)

def right(t):
    t.right(90)

def up(t):
    t.forward(10)

if __name__ == '__main__':
    main()