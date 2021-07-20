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
lbl = Label(root, font = ('calibri', 12), borderwidth = 1, relief = "ridge")
# position of clock at upper-right corner
lbl.pack(anchor = 'ne')
time()
frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('HR', '00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('MIN', '00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

am_pm = StringVar(root)
am_pms = ('AM/PM', 'AM', 'PM')
am_pm.set(am_pms[0])

aps = OptionMenu(frame, am_pm, *am_pms)
aps.pack(side = LEFT)

mainloop()



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


