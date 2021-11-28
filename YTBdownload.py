from tkinter import *
from pytube import YouTube

# Create a display window

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)  # set fix size of the window
root.title("JJ- Youtube Video Downloader")

# create input for link
link = StringVar()

Label(root, text='Please enter the link here: ', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


# create a download functions
def videoDownload():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='Downloaded', font='arial 15').place(x=180, y=210)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='violet red', padx=2, command=videoDownload).place(x=180, y=150)
root.mainloop()