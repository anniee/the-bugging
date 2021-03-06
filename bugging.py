# A twee bug game as the programmer's exercise in OOP, with ultimate
# goal of practicing writing Mendelian inheritance algorithms
import turtle as bug
import random
from bug_types import Scarab, Lady, QueenBee, Widow

window = bug.Screen()
window.bgcolor("black")


THE_BUGS = [ Scarab, QueenBee, Widow ]


class TheBug:
  # For the unique, dynamically generated bug object.


  def __init__(self, POS=0):

    # the_bug_type = random.choice(THE_BUGS)
    the_bug_type = THE_BUGS[2]
    self.bug_type = the_bug_type(POS)



alpha_bug = TheBug(100)

beta_bug = TheBug(-100)

# bby_bug = TheBug(-50)
# y pos
window.exitonclick()
