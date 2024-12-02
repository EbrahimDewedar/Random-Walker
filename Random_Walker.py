import random
import turtle as tu
colors = ["dark slate blue", "deep pink", "rosy brown", "gold", "dark green", "dodger blue", "black", "red", "maroon", "pale green"]

tim = tu.Turtle()
tim.pensize(13)

list = []
for i in range(1,4):
    list.append(i)

def to_left(dis):
    tim.color(random.choice(colors))
    tim.left(dis*90)
    tim.forward(50)
def to_right(dis):
    tim.color(random.choice(colors))
    tim.right(dis*90)
    tim.forward(50)

start = True
while start:
    distance = random.choice(list)
    to_left(distance)
    to_right(distance)

