import turtle
import time
import random
score = 0
points = 0

#creatingscreen
screen = turtle.Screen()
screen.title("snake by codeplateau")
screen.bgcolor("black")
screen.setup(width=600, height=600)

#creating snake head
head = turtle.Turtle()
head.penup() #do not drag while moving
head.speed(0)
head.shape("circle")
head.color("red")
head.goto(0,0)
head.direction = "stop" #default direction

#creating the food
food = turtle.Turtle()
food.penup()
food.speed(0)
food.shape("square")
food.color("white")
food.goto(150,105)
food.direction = "stop"

#for snake body
snake = []

#Creating the movements
#to do that we use functions
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_right():
    head.direction = "right"
def go_left():
    head.direction = "left"
def pause():
    head.direction = "stop"
def reset ():
    head.direction = "reset"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "stop":
        head.direction = "stop"
    elif head.direction == "reset":
        head.goto(0,0)

#adding the keyboard command or setup
screen.listen()
screen.onkey(go_up, "i")
screen.onkey(go_down, "k")
screen.onkey(go_right, "l")
screen.onkey(go_left, "j")
screen.onkey(pause, "a")
screen.onkey(reset, "s")

#the main game loop

while True:
    screen.update()
    if head.distance(food) <20: #setting how the food disappears
        x = random.randint(-290, 290) #setting how the food appears
        y = random.randint(-290, 290)
        food.goto(x,y)
        score = score + 5
        points = points + 1
        print ("Score:",score)
        print ("Oga I don chop ", points, "times")
        #snake new body after eating
        new_segment = turtle.Turtle()
        new_segment.penup()
        new_segment.shape("circle")
        new_segment.color("yellow")
        new_segment.speed(0)

        snake.append(new_segment)

        #moving the segment first in reverse other
    for index in range(len(snake)-1, 0, -1):
        x = snake[index-1].xcor()
        y = snake[index-1].ycor()
        snake[index].goto(x,y)
        #moving segment 0 to where the head is
    if len(snake) >0:
        x = head.xcor()
        y = head.ycor()
        snake[0].goto(x,y)

        

    move()
    time.sleep(0.1)


screen.mainloop()

