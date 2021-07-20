from tkinter import *
from tkinter.ttk import *
import datetime
from time import *
import winsound
import pytz
from threading import *
# Create Object

clock = Tk()

# checks time and updates lbl every second
def time():
    time_str = strftime("%H:%M:%S %p")
    lbl.config(text=time_str)
    lbl.after(1000, time)

# Set geometry
clock.geometry("400x200")
# setting title
clock.title("Set your Alarm Clock!")
# adding a label to the root window
lbl = Label(clock, font = ('calibri', 12), borderwidth = 1, relief = "ridge")
# position of clock at upper-right corner
lbl.pack(anchor='ne')
time()

def alarm(set_alarm_timer):
    while True:
        sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", foreground="red",background="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",foreground="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,background = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,background = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,background = "pink",width = 15).place(x=200,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",width = 10,command = actual_time).place(x =110,y=70)

mainloop()



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


