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

def alarm(time_object):
    while True:
        sleep(1)

        current_time = datetime.datetime.now().astimezone()
        now = current_time.strftime("%H:%M:%S %z")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == time_object:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()} {gmt.get()}"
    time_object = datetime.datetime.strptime(set_alarm_timer, "%H:%M:%S %z")
    alarm(time_object)


def check(e):
    tz = gmt.get()
    if tz == "":
        data = tz_list
    else:
        data = []
        for timezone in tz_list:
            if tz.lower() in timezone.lower():
                data.append(timezone)
    update(data)


def update(data):
    pass

time_format=Label(clock, text= "Enter time in 24 hour format!", foreground="red",background="black",font="Arial").place(x=90,y=150)
addTime = Label(clock,text = "Hour   Min   Sec      GMT",font=60).place(x = 110, y = 30)
setYourAlarm = Label(clock,text = "Time: ",foreground="blue",relief = "solid",font=("Helevetica", 10,"bold")).place(x=60, y=60)

# List of timezones
tz_list = pytz.all_timezones

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
gmt = StringVar()

# Time required to set the alarm clock:
hourTime = Entry(clock,textvariable = hour,width = 8)
hourTime.place(x = 135, y = 70, anchor = CENTER)

minTime = Entry(clock,textvariable = min,width = 7)
minTime.place(x = 190, y = 70, anchor = CENTER)

secTime = Entry(clock,textvariable = sec,width = 7)
secTime.place(x = 240, y = 70, anchor = CENTER)

timezone = Entry(clock,textvariable = gmt, width = 7)
timezone.place(x = 308, y = 70, anchor = CENTER)
timezone.bind("<KeyRelease>", check)
places = Listbox(clock)

# To take the time input by user:
submit = Button(clock,text = "Set Alarm",width = 10,command = actual_time).place(x =110,y=100)

mainloop()



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


