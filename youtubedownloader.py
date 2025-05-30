from tkinter import *
from tkinter import filedialog
from pytube import YouTube

#Functions
#Allows user to select a path from the explorer
def select_path():
  path = filedialog.askdirectory()
  path_label.config(text=path)

#Downloads YouTube video from the link user gave and saves it
def Download():
  youtubeURL = ytLinkField.get()
  userPath = path_label.cget("text")
  screen.title("Downloading...")
  #Download YT video and move to selected directory
  YouTube(youtubeURL).streams.get_highest_resolution().download(userPath)
  screen.title("Download Complete! Download Another File...")

#GUI
screen = Tk()
title = screen.title("YouTube Video Downloader By: Nathan D. Markley")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

title_label = Label(screen, text="YouTube Video Downloader \n By: Nathan D. Markley", font='arial 18 bold')

#YT URL field
ytLinkField = Entry(screen, width= 50)
ytLinkLabel = Label(screen, text="Paste YouTube link here: ", font='arial 15 bold')

#Select Path for saving video file
path_label = Label(screen, text="Select path to save video to", font='arial 15 bold')
select_btn = Button(screen, text="Select", command=select_path)

#Dowload btns
download_btn = Button(screen, text='DOWNLOAD', font='arail 15 bold', padx=2, command=Download)

#Add widgets to window
canvas.create_window(250, 80, window=title_label)
canvas.create_window(250, 170, window=ytLinkLabel)
canvas.create_window(250, 220, window=ytLinkField)
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()