import turtle


def draw_kc(brad):
	# turn down to the middle of k
	brad.right(90)
	brad.fd(100)
	
	# turn left to draw right of k
	brad.left(135)
	brad.fd(150)
	brad.bk(150)

	# turn down to continue
	brad.right(135)
	brad.fd(100)
	brad.bk(100)
	
	# turn left to draw right of k
	brad.left(45)
	brad.fd(150)
	
	# move back and move to draw c
	brad.penup()
	brad.home()
	brad.fd(250)
	brad.down()
	
	# turn to point left, and draw c
	brad.right(180)
	brad.fd(100)
	brad.left(90)
	brad.fd(200)
	brad.left(90)
	brad.fd(100)

# init the drawing screen
window = turtle.Screen()
window.bgcolor('red')
brad = turtle.Turtle()
brad.color('yellow')
brad.shape('turtle')
draw_kc(brad)
window.exitonclick()

