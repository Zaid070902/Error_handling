from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.config(bg="#111")

title_lab = Label(root, text="Please enter login details", bg="#111", fg="cyan")
title_lab.place(x=170, y=10)

username_lab = Label(root, text="Username", bg="#111", fg="cyan")
username_lab.place(x=215, y=50)

username_entry = Entry(root, width=20)
username_entry.place(x=170, y=80)

password_lab = Label(root, text="Password", bg="#111", fg="cyan")
password_lab.place(x=215, y=150)

password_entry = Entry(root, width=20)
password_entry.place(x=170, y=180)

Username = ["Cassiem", "Gary", "Zaid", "Aaliyah", "Uthmaan"]
Password = ["666", "777", "999", "888", "333"]


def log():
    found = False
    for x in range(len(Username)):
        if username_entry.get() == Username[x] and password_entry.get() == Password[x]:
            found = True
    if found == True:
        messagebox.showinfo("STATUS", "Access granted")
    else:
        messagebox.showinfo("STATUS", "Access denied")

    import Second_window


log_btn = Button(root, text="Login", bg="#111", fg="cyan", command=log)
log_btn.place(x=215, y=250)

root.mainloop()
