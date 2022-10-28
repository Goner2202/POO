# import statements
from tkinter import *
from tkinter.messagebox import *
class Help():

    def about(root):
        showinfo(title="About", message="This is a text editor made by GONE.dust using Python     U can find other projects here: github.com/Goner2202")
    
def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="About", command=help.about)
    menubar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menubar)
    
if __name__ == "__main":
    print("Please run 'main.py'")