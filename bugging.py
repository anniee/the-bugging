# A twee bug game as the programmer's exercise in OOP, with ultimate
# goal of practicing writing Mendelian inheritance algorithms
from flask import Flask

import wx
import wx.aui
import wx.lib.buttons
import wx.lib.scrolledpanel

import turtle as bug
import random
from bug_types import Scarab, Lady

app = Flask(__name__)

@app.route("/")
def generate_bugs():
  # window = bug.Screen()
  # the_window = Tkinter.Tk()
  # window = bug.TurtleScreen(the_window.ScrolledCanvas)
  # window = bug.TurtleScreen(the_window.ScrolledText)
  class ApplicationWindow(wx.Frame):
    """
    The main window of PythonTurtle.
    """
    def __init__(self,*args,**keywords):
        wx.Frame.__init__(self,*args,**keywords)


        self.bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.bottom_sizer.Add(self.shell, 1, wx.EXPAND)
        self.bottom_sizer.Add(self.help_open_button_panel, 0, wx.EXPAND)

        self.bottom_sizer_panel.SetSizer(self.bottom_sizer)

        self.Centre()
        self.Maximize()
        self.Show()

        self.Layout()



  def run():
    app = wx.PySimpleApp()
    my_app_win = ApplicationWindow(None,-1,"Bugz",size=(600,600))
    #import cProfile; cProfile.run("app.MainLoop()")
    app.MainLoop()

  # w = Canvas(top, bg="blue", height=250, width=300)
  # window = bug.Screen()
  # window.bgcolor("black")

  # window.setbg("black")


  # THE_BUGS = [ Scarab, Lady ]


  # class TheBug:
  #   # For the unique, dynamically generated bug object.

  #   def __init__(self):

  #     the_bug_type = random.choice(THE_BUGS)
  #     self.bug_type = the_bug_type()


  # alpha_bug = TheBug()

  # # make these attributes so in bug_types can set attribute like "if beta bug, change position"

  # beta_bug = TheBug()

  # beta_bug = TheBug()
  #pass attribute to change its position

  # bby_bug

  # window.exitonclick()
  return generate_bugs()

if __name__ == "__main__":
  app.run(debug=True)
