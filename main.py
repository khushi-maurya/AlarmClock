# import all necessary libraries
from tkinter import *
import datetime
import winsound
from PIL import ImageTk,Image

# the main function starts here

# Function to Play Sound for Alarm
def sound_alarm():
    winsound.PlaySound("sample-15s.wav", winsound.SND_FILENAME)


# Function to Set Alarm Using Datetime module
def set_alarm():
    alarm_hour = int(hour.get())
    alarm_minute = int(minute.get())
    alarm_sec = int(sec.get())

    now = datetime.datetime.now()
    alarm_time = now.replace(hour=alarm_hour, minute=alarm_minute, second=alarm_sec)

    time_diff = alarm_time - now
    if time_diff.total_seconds() <= 0:
        print("Invalid time! Please set a time in the future.")
    else:
        print("Alarm set for:", alarm_time)
        root.after(int(time_diff.total_seconds() * 1000), sound_alarm)


# Working on the designing of the Alarm Project's Accessibility

# Create the main window
root=Tk()
root.title("DataFlair Alarm Clock")
root.geometry("460x300")
root.configure(bg="pink")

# Create GUI components
frame=Frame(root,width=460,height=15,bg="purple")
frame.grid(row=0,column=0)
frame1=Frame(root,width=460,height=7,bg="grey")
frame1.grid(row=16,column=0)

# Inserting Image in Frame Body
img=Image.open('clock2.jpg')
img.thumbnail((200,150))
img=ImageTk.PhotoImage(img)
app_image=Label(root,height=160,width=140,image=img)
app_image.place(x=20,y=100)


Label(root, text="Hour          Min          Sec", font=("Arial", 13)).place(x=200, y=90)
Label(root, text="When to wake you up", fg="purple", font=("Helvetica", 16, "bold")).place(x=125, y=40)

hour = Spinbox(root, bg="pink", width=10, from_=0, to=23)
minute = Spinbox(root, bg="pink", width=10, from_=0, to=59)
sec = Spinbox(root, bg="pink", width=10, from_=0, to=59)

hour.place(x=185, y=120)
minute.place(x=265, y=120)
sec.place(x=345, y=120)

Button(root, text="Set Alarm", fg="white", width=13, activebackground="red", bg="#34A2FE", height=1,
                font=("Arial", 16, "bold"),bd=8, command=set_alarm).place(x=220, y=160)

Label(root, text="Enter time in 24-hour format!", fg="black",bd=5, bg="grey", height=1, width=26,
      font=("Arial", 11, "bold")).place(x=190, y=240)

# Run the main event loop
root.mainloop()
