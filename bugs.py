import turtle as bug
import bugging
class Scarab:
# Scarab class for representing and generating scarab-shaped bug.

    def __init__(self):
        # Create a new scarab bug.

        scarab = bug.Turtle()
        scarab.color(main_color)
        scarab.pensize(5)

        scarab.fill(True)
        scarab.left(90)
        scarab.forward(50)
        scarab.right(45)
        scarab.forward(25)
        scarab.right(45)
        scarab.forward(10)
        scarab.right(45)
        scarab.forward(25)
        scarab.right(45)
        scarab.forward(50)
        scarab.fill(False)

        scarab.pencolor(detail_color)
        scarab.fill(True)
        scarab.circle(-22.5, 180)
        scarab.right(45)
        scarab.forward(30)
        scarab.right(90)
        scarab.forward(30)
        scarab.fill(False)

        scarab.left(180)
        scarab.forward(30)
        scarab.right(45)
        scarab.forward(27)
        scarab.pu()
        scarab.left(90)
        scarab.forward(50)

        # draw legs and detail for top of wings

        scarab.pencolor(legs_color)
        scarab.pd()
        scarab.right(180)
        scarab.forward(25)
        scarab.pencolor(detail_color)
        scarab.forward(50)
        scarab.pencolor(legs_color)
        scarab.forward(30)

        scarab.pu()
        scarab.right(90)
        scarab.forward(25)
        scarab.pd()
        scarab.right(90)
        scarab.forward(30)
        scarab.pu()
        scarab.forward(50)
        scarab.pd()
        scarab.forward(25)

        scarab.pu()
        scarab.left(90)
        scarab.forward(25)
        scarab.pd()
        scarab.left(90)
        scarab.forward(25)
        scarab.pu()
        scarab.forward(50)
        scarab.pd()
        scarab.forward(30)
