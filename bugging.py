# A twee bug game as the programmer's exercise in OOP, with ultimate
# goal of practicing writing Mendelian inheritance algorithms
import turtle as bug
import random

BEETLE_BACK = [ "orchid", "goldenrod", "lightgrey", "thistle", "rosybrown", "mediumorchid",
                "darkkhaki", "greenyellow", "mediumvioletred", "indianred", "peru", "chocolate",
                "palegreen", "tan", "darkgoldenrod", "palevioletred", "red", "lightcyan" ]

window = bug.Screen()
window.bgcolor("black")

main_color = random.choice(BEETLE_BACK)
detail_color = random.choice(BEETLE_BACK)
legs_color = random.choice(BEETLE_BACK)

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

window.exitonclick()


# 1. make bugs with random patterns/colors first
# 2. classes of them, with specific atttributes for their colors/patterns and shapes, methods for movement/growing in size
# 3. solidfy inheritance/generation of bby bug
