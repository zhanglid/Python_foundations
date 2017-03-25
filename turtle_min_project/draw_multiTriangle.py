import turtle


def draw_green_triangle(brad, length):
    brad.fillcolor('green')
    brad.begin_fill()
    brad.fd(length)
    brad.left(120)
    brad.fd(length)
    brad.left(120)
    brad.fd(length)
    brad.left(120)
    brad.end_fill()


def draw_inside_triangle(brad, length):
    # draw two triangles, one is green, one is white inside
    brad.penup()
    brad.fd(length/2)
    brad.pendown()
    brad.fillcolor('white')
    brad.begin_fill()
    brad.left(60)
    brad.fd(length/2)
    brad.left(120)
    brad.fd(length/2)
    brad.left(120)
    brad.fd(length/2)
    brad.end_fill()
    brad.penup()
    brad.left(60)
    brad.bk(length/2)
    brad.pendown()


def draw_three_triangle(brad, length):
    # draw small triangles at each three sub triangles
    draw_inside_triangle(brad, length/2)
    brad.fd(length/2)
    draw_inside_triangle(brad, length/2)
    brad.left(120)
    brad.penup()
    brad.fd(length/2)
    brad.right(120)
    brad.pendown()
    draw_inside_triangle(brad, length/2)
    brad.right(120)
    brad.penup()
    brad.fd(length/2)
    brad.left(120)
    brad.pendown()


window = turtle.Screen()
brad = turtle.Turtle()
brad.color('green')
brad.shape('turtle')
brad.speed(100)
brad.pencolor('blue')
length = 300
draw_green_triangle(brad, length)
draw_inside_triangle(brad, length)
draw_three_triangle(brad, length)
draw_three_triangle(brad, length / 2)
brad.fd(length / 2)
draw_three_triangle(brad, length / 2)
brad.left(120)
brad.fd(length / 2)
brad.right(120)
draw_three_triangle(brad, length / 2)
brad.right(120)
brad.fd(length / 2)
brad.left(120)
brad.fillcolor('green')
brad.penup()
brad.fd(length*3/4)
brad.pendown()
window.exitonclick()
