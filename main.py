
from tkinter import *
from tkinter.ttk import *
import datetime
from time import strftime
import winsound
import pytz
from threading import *
# Create Object
root = Tk()

# checks time and updates lbl every second
def time():
    time_str = strftime("%H:%M:%S %p")
    lbl.config(text = time_str)
    lbl.after(1000, time)

# Set geometry
root.geometry("400x200")
# setting title
root.title("Set your Alarm Clock!")
# adding a label to the root window
lbl = Label(root, font = ('calibri', 12))

# position of clock at upper-right corner
lbl.pack(anchor = 'ne')
time()
mainloop()



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


