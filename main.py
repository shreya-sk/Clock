from tkinter import *
from tkinter.ttk import *
import datetime
from time import strftime
import winsound
import pytz
from threading import *

# checks time and updates lbl every second
def time():
    time_str = strftime("%H:%M:%S %p")
    lbl.config(text = time_str)
    lbl.after(1000, time)

root = Tk()

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
def clicked():
    lbl.configure(text="I just got clicked")



# Execute Tkinter
root.mainloop()

def dt_threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    pass


root.mainloop()
