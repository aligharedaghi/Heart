import turtle

def draw_heart():
    turtle.color('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

if __name__ == "__main__":
    turtle.speed(2)
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()
    
    draw_heart()
    
    turtle.hideturtle()
    turtle.done()
