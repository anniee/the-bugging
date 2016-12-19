import turtle as bug
import random, math

BUG_BACK = [ "orchid", "goldenrod", "lightgrey", "thistle", "rosybrown", "mediumorchid", "darkkhaki", "greenyellow", "mediumvioletred","indianred", "peru", "chocolate", "palegreen", "tan", "darkgoldenrod", "palevioletred", "red", "lightcyan" ]
# POS = 10

class Scarab:
# Scarab class for representing and generating scarab-shaped bug.

    def __init__(self, POS=0):
        # Create a new scarab bug.
        main_color = random.choice(BUG_BACK)
        detail_color = random.choice(BUG_BACK)
        legs_color = random.choice(BUG_BACK)

        scarab = bug.Turtle()
        scarab.hideturtle()
        scarab.setx(POS)
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

# class Moth:


class Lady:

    def __init__(self, POS=0):

        main_color = random.choice(BUG_BACK)
        detail_color = random.choice(BUG_BACK)
        legs_color = random.choice(BUG_BACK)

        lady = bug.Turtle()
        lady.setx(POS)
        lady.color(main_color)
        lady.pensize(3)

        lady.fill(True)
        lady.circle(50)
        lady.fill(False)

class QueenBee:

    def __init__(self, POS=0):

        main_color = random.choice(BUG_BACK)
        detail_color = random.choice(BUG_BACK)
        legs_color = random.choice(BUG_BACK)

        queenbee = bug.Turtle()
        queenbee.hideturtle()
        queenbee.setx(POS)
        queenbee.color(main_color)
        queenbee.pensize(3)

        # queenbee.fill(True)
        # queenbee.left(90)
        # queenbee.forward(50)
        # queenbee.right(45)
        # queenbee.forward(25)
        # queenbee.right(45)

        num_sides = 6
        side_length = 70
        angle = 360.0 / num_sides

        # honeycomb.fill(True)

        for i in range(num_sides):
            queenbee.forward(side_length)
            queenbee.right(angle)

        queenbee.pu()
        queenbee.right(50)
        queenbee.forward(25)
        queenbee.pd()
        queenbee.right(30)
        queenbee.fill(True)
        queenbee.forward(30)
        queenbee.left(10)
        queenbee.forward(60)
        queenbee.left(90)
        queenbee.forward(40)
        queenbee.left(90)
        queenbee.forward(60)
        queenbee.left(20)
        queenbee.forward(30)
        queenbee.left(70)
        queenbee.forward(25)
        queenbee.fill(False)

        queenbee.pencolor(detail_color)
        # queenbee.pu()
        # queenbee.right(50)
        # queenbee.forward(25)
        # queenbee.pd()

        queenbee.left(81)
        # queenbee.fill(True)
        queenbee.forward(30)
        queenbee.left(10)
        queenbee.forward(60)
        queenbee.left(160)
        queenbee.forward(65)
        queenbee.right(143)
        queenbee.forward(65)
        queenbee.left(162)
        queenbee.forward(60)
        queenbee.left(20)
        queenbee.forward(32)
        queenbee.left(70)
        queenbee.forward(30)
        # queenbee.fill(False)

        queenbee.left(81)
        queenbee.pu()
        queenbee.forward(50)
        queenbee.left(95)
        queenbee.forward(22)
        queenbee.pd()
        queenbee.pensize(8)
        queenbee.forward(13)
        queenbee.pu()
        queenbee.right(80)
        queenbee.forward(15)
        queenbee.pd()
        queenbee.right(92)
        queenbee.forward(17)
        queenbee.pu()
        queenbee.left(74)
        queenbee.forward(15)
        queenbee.pd()
        queenbee.left(98)
        queenbee.forward(25)



        queenbee.pu()
        queenbee.forward(10)
        queenbee.left(104)
        queenbee.forward(85)
        queenbee.pd()
        queenbee.pensize(10)
        queenbee.pencolor(legs_color)
        queenbee.left(83)
        queenbee.forward(5)
        queenbee.pu()
        queenbee.forward(18)
        queenbee.pd()
        queenbee.forward(5)
        # queenbee.left(90)
        # queenbee.forward(5)

class Widow:

    def __init__(self, POS=0):

        main_color = random.choice(BUG_BACK)
        detail_color = random.choice(BUG_BACK)
        legs_color = random.choice(BUG_BACK)

        widow = bug.Turtle()
        widow.hideturtle()
        widow.setx(POS)
        widow.color(main_color)
        widow.pensize(3)
        widow.speed(0)
        widow.color()
        size=70

        widow.setheading(90) #Point the top
        for i in range(0,6):
          widow.forward(size)
          widow.penup()
          widow.forward(-size)
          widow.left(60)
          widow.pendown()

        widow.setheading(90) #Point the top
        widow.forward(size)
        widow.setheading(215) #Point the left
        newSize=size
        newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(65))
        for i in range(0,30):
           widow.forward(newSize)
           widow.left(60)
           newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(70))

        widow.color(detail_color)
        widow.fill(True)
        widow.circle(15, 360)
        widow.fill(False)
        widow.pu()
        widow.left(90)
        widow.pd()
        widow.color(legs_color)
        widow.circle(3, 360)
        widow.pu()
        widow.left(45)
        widow.forward(20)
        widow.pd()
        # widow.fill(True)
        widow.circle(3, 360)
        # widow.fill(False)



# class Snail:

#     def __init__(self, POS=0):

#         main_color = random.choice(BUG_BACK)
#         detail_color = random.choice(BUG_BACK)
#         legs_color = random.choice(BUG_BACK)
