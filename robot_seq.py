import turtle

window = turtle.Screen()
window.title("Turtle")

#Create turtle

turtle = turtle.Turtle()
turtle.speed(1)
turtle.shape('turtle')
turtle.goto(0,0)
turtle.color('orange')


for i in range(3):
    #turtle.fd(100)
    for j in range(2):
        turtle.fd(50)
    turtle.lt(90)


window.mainloop()