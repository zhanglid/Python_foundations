import turtle


# draw a diamond shape, maintain the original direction
def draw_diamond(brad):
	brad.right(18)
	brad.fd(100)
	brad.left(36)
	brad.fd(100)
	brad.left(144)
	brad.fd(100)
	brad.left(36)
	brad.fd(100)
	brad.left(180-18)

window = turtle.Screen()
window.bgcolor('red')
brad = turtle.Turtle()
brad.shape('turtle')
brad.speed(10)
brad.color('blue')
numberOfDiamond = 72
for i in range(numberOfDiamond):
	draw_diamond(brad)
	brad.left(360/numberOfDiamond)
window.exitonclick()

