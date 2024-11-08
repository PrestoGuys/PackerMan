from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
import subprocess


def div():
    print("------------------------------------------------------------")

def updateAll():
    div()
    print("Starting Pacman & yay Upgrade")
    subprocess.run("sudo pacman --noconfirm -Syu", shell=True, check=True)
    div()
    subprocess.run("yay --noconfirm -Syu", shell=True, check=True)
    print("Done!")
    div()

def inputIn():
    inputValue = textbox.get()

    div()
    print("Installing " + inputValue + " Pacman package")
    subprocess.run("sudo pacman --noconfirm -S " + inputValue, shell=True)
    print("Done!")
    div()

def inputyayIn():
    inputValue = textbox.get()

    div()
    print("Installing " + inputValue + " Yay package")
    subprocess.run("yay --noconfirm -S " + inputValue, shell=True)
    print("Done!")
    div()





div()
print("INFO: ON FIRST FOR THE SESSION PROGRAM STARTUP, IT WILL ASK")
print("FOR PASSWORD FOR ROOT AND SUDO.")
div()
#subprocess.run("zenity --password --title='Please Provide Password, it is ' --timeout=30", shell=True, check=True)



window_width = 600
window_height = 500
title = 'PackerMan BETA 1'
theme = "breeze"


# Setting theme
root = ThemedTk(theme=theme)
# Setting with and height and centering it
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# Setting Title
root.title(title)

ttk.Label(root, text="PackerMan BETA 1").place(x=6, y=6)

buttonCommit=ttk.Button(root, text="Install Pacman Package", command=inputIn).place(x=6, y=67)

buttonCommit=ttk.Button(root, text="Install Yay Package", command=inputyayIn).place(x=6, y=103)




textbox=ttk.Entry(root, width=82)
textbox.place(x=6, y=30)

ttk.Button(root, text="System Package Update", command=updateAll).place(x=6, y=139)


ttk.Button(root, text="Quit", command=root.destroy).place(x=500, y=465)
root.mainloop()