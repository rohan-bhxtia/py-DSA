from tkinter import *
import datetime
import winsound

# ----------------- Functions -----------------
def set_alarm():
    """Calculate target time and start checking with after()"""
    global alarm_time
    try:
        h = int(hour.get())
        m = int(minute.get())
        s = int(second.get())
        alarm_time = datetime.time(h, m, s)
        status_label.config(text=f"Alarm set for {alarm_time}")
        check_alarm()
    except ValueError:
        status_label.config(text="Invalid time!")

def check_alarm():
    """Check every 500ms if current time matches alarm"""
    now = datetime.datetime.now().time().replace(microsecond=0)
    if now == alarm_time:
        status_label.config(text="Time to Wake Up!")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
    else:
        root.after(500, check_alarm)  # check again after 500ms

# ----------------- GUI -----------------
root = Tk()
root.title("Optimized Alarm Clock")
root.geometry("400x200")

Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack(pady=5)

# Hour
hour = StringVar(root)
hours = [f"{i:02d}" for i in range(24)]
hour.set(hours[0])
OptionMenu(frame, hour, *hours).pack(side=LEFT)

# Minute
minute = StringVar(root)
minutes = [f"{i:02d}" for i in range(60)]
minute.set(minutes[0])
OptionMenu(frame, minute, *minutes).pack(side=LEFT)

# Second
second = StringVar(root)
seconds = [f"{i:02d}" for i in range(60)]
second.set(seconds[0])
OptionMenu(frame, second, *seconds).pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=set_alarm).pack(pady=15)

status_label = Label(root, text="", font=("Helvetica 12 bold"))
status_label.pack()

root.mainloop()
