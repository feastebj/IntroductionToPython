"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Benjamin Feaster.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

purple_turtle = rg.SimpleTurtle('turtle')
purple_turtle.pen = rg.Pen('purple', 1)
purple_turtle.speed = 100

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 1)
red_turtle.speed = 100

size = 150

for i in range(20):
    purple_turtle.draw_circle(size)
    red_turtle.draw_circle(size - 20)

    purple_turtle.right(100)
    purple_turtle.forward(10)
    purple_turtle.left(45)

    red_turtle.right(100)
    red_turtle.forward(10)
    red_turtle.left(45)

window.close_on_mouse_click()
