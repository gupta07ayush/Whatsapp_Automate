import pywhatkit
from tkinter import Tk, Button, Entry, Label

root = Tk()
root.geometry('570x280')
root.title('Send')
root.config(bg='orange')


# send function
def send():
    number = mobile_entry.get()
    msg = msg_entry.get()
    pywhatkit.sendwhatmsg_instantly(number, msg)


# Heading
heading = Label(root, text='Send Whatsapp Message', font=('arial', 25, 'bold'))
heading.place(x=20, y=20, width=530)

# Mobile Number
mobile_label = Label(root, text="Mobile Number:")
mobile_label.place(x=20, y=100)
mobile_entry = Entry(root, )
mobile_entry.place(x=150, y=100, width=400)

# Message
msg_label = Label(root, text="Your Message:")
msg_label.place(x=20, y=140)
msg_entry = Entry(root, )
msg_entry.place(x=150, y=140, width=400)

# send button
send_button = Button(root, command=send, text="Send")
send_button.place(x=250, y=200, width=150, height=50)

# start the gui
root.mainloop()
