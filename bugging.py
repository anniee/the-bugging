# A twee bug game as the programmer's exercise in OOP, with ultimate
# goal of practicing writing Mendelian inheritance algorithms
import turtle as bug
import random
from bug_types import Scarab, Lady

window = bug.Screen()
window.bgcolor("black")


THE_BUGS = [ Scarab, Lady ]


class TheBug:
  # For the unique, dynamically generated bug object.

  def __init__(self):

    the_bug_type = random.choice(THE_BUGS)
    self.bug_type = the_bug_type()


alpha_bug = TheBug()

# make these attributes so in bug_types can set attribute like "if beta bug, change position"

beta_bug = TheBug()

# beta_bug = TheBug()
#pass attribute to change its position

window.exitonclick()
