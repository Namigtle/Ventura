from mainFrame import MainFrame
from tkinter import Tk

def main():
    root=Tk()
    root.wm_title("Impresora Braille")
    app=MainFrame(root)
    app.configure(bg=("#%02x%02x%02x" % (70,70,71)))
    app.mainloop()
main()  



