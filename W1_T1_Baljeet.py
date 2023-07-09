#                                        *Welcome to Baljeet's Alarm Clock* 
#                                        * (Sync Intern) Week 1 Task 1: Alarm Clock Using Tkinter ,Datetime and winsound libraries.

from tkinter import *
import datetime
import time
import winsound



def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")
        if now == set_alarm_timer:
            print("Time to Wake up")
            print("Time to Wake up")
            print("Time to Wake up")
            print("Time to Wake up")
            print("Time to Wake up")
            winsound.PlaySound("ab.wav",winsound.SND_ASYNC)
            break

def act_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Baljeet Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Note: Enter time in 24 hour format", fg="blue",bg="grey",font="Arial").place(x=50,y=150)
addTime = Label(clock,text = "  Hour        Mins ",font=('Calibri',15, 'bold')).place(x = 120, y= 30)
setYourAlarm = Label(clock,text = "Wake Up Time: ",fg="blue",font=("Calibri",12,"bold")).place(x=0, y=60)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "yellow",width = 15).place(x=120,y=60)
minTime= Entry(clock,textvariable = min,bg = "yellow",width = 15).place(x=200,y=60)

#time input button by user:
submit = Button(clock,text = "Set Alarm",fg="black",width = 10,command = act_time).place(x =160,y=100)

clock.mainloop()
#Execution of the window.

