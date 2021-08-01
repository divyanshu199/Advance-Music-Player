from tkinter.ttk import Progressbar  # for progress bar
from pygame import mixer  # for music pygame mixer is used,
import os
from mutagen.mp3 import MP3
import datetime
from tkinter import filedialog
from tkinter import *


def searchmusic():  # DEFINING SEARCH MUSIC FUNCTION
    # TO OPEN THE FILE DIALOG TO GET MUSIC
    file = filedialog.askopenfilename(
        filetype=(('*.MP3', '*.mp3'), ('WAV', '*.wav')))
    audiotrack.set(file)  # AUDIO SET TO THE CHOOSEN MUSIC


def playmusic():  # DEFINING PLAYMUSIC
    try:
        ad = audiotrack.get()  # TO GET THE SET SONG IN AD VARIABLE
        mixer.music.load(ad)  # LOADING THE SONG
        mixer.music.play()  # PLAYING SONG
        # PRINTING PLAYING LABEL ON SCREEN.
        statuslabel.configure(text="Playing")
        progressbarmusiclabel.grid()  # PACKING THE LABLE
        #####MUSIC PROGRESS BAR CONFIGURATION########
        song = MP3(ad)  # GETTING THE SONG IN song VARIABLE
        totalsonglength = int(song.info.length)  # GET THE LENGTH OF SONG BY OS
        # MAXIMUM VALUE OF PROGRESS BAR SET TO TOTALLENGTH
        progressbarmusic['maximum'] = totalsonglength
        progressbarmusicendtimelabel.configure(text="{}".format(str(datetime.timedelta(
            seconds=totalsonglength))))  # PROGRESS END LABEL SET TO LENGTH OF SONG IN CLOCK FORMAT

        def musicbar():  # DEFINING MUSICBAR FUNCTION INSIDE PLAY FUNCTION//NESTED FUNCTION
            currentpos = mixer.music.get_pos()//1000  # SYSTEM CLOCK IN MIllISECOND
            # CURRENT VALUE OF MUSIC ON PROGRESSBAR
            progressbarmusic['value'] = currentpos
            progressbarmusicstarttimelabel.configure(
                text="{}".format(str(datetime.timedelta(seconds=currentpos))))
            progressbarmusic.after(2, musicbar)
        musicbar()

    except:
        # IF WE PLAY WITHOUT SELECTING SONG
        audiotrack.set("Error:Select song")


def pausemusic():  # DEFINING PAUSEMUSIC FUNCTION
    mixer.music.pause()  # PAUSING MUSIC
    root.pausebutton.grid_remove()  # REMOVING PAUSEBUTTON
    root.resumebutton.grid()  # PLACING RESUME BUTTON ON SAME PLACE
    statuslabel.configure(text="Pause")  # CHANGING LABEL TO PAUSE


def resumemusic():  # DEFINING RESUME MUSIC FUNCTION
    root.resumebutton.grid_remove()  # REMOVING RESUME BUTTON
    root.pausebutton.grid()  # PLACING PAUSE BUTTON
    mixer.music.unpause()  # PLAYING THE SONG
    statuslabel.configure(text="Playing")


def volumeup():
    vol = mixer.music.get_volume()
    if (vol >= vol * 100):
        mixer.music.set_volume(vol+0.1)
    else:
        mixer.music.set_volume(vol+0.05)
        middlevollabel.configure(text="{}%".format(
            int(mixer.music.get_volume()*100)))
        progressbar['value'] = mixer.music.get_volume()*100


def volumedown():
    vol = mixer.music.get_volume()
    if (vol <= vol * 100):
        mixer.music.set_volume(vol - 0.01)
        middlevollabel.configure(text="{}%".format(int(mixer.music.get_volume() * 100)))
        progressbar['value'] = (mixer.music.get_volume() * 100)
    else:
        mixer.music.set_volume(vol - 0.05)
        middlevollabel.configure(text="{}%".format(int(mixer.music.get_volume() * 100)))
        progressbar['value'] = (mixer.music.get_volume() * 100)


def stopmusic():
    mixer.music.stop()
    statuslabel.configure(text="Stopped")
    progressbarmusicstarttimelabel.configure(
        text="{}".format(str(datetime.timedelta(seconds=00))))


def mutemusic():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)
    statuslabel.configure(text="Muted")


def unmutemusic():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)
    statuslabel.configure(text="Playing")


def createwidget():
    # Images Register:
    global searchimage, playimage, pauseimage, stopimage, volumeupimage, volumedownimage, resumeimage, muteimage, unmuteimage, statuslabel
    global progressbar, progressbarlabel, middlevollabel, progressbarmusiclabel, progressbarmusic
    global progressbarmusicstarttimelabel, progressbarmusicendtimelabel
    searchimage = PhotoImage(file="search.png")
    playimage = PhotoImage(file="play-button.png")
    pauseimage = PhotoImage(file="pause.png")
    stopimage = PhotoImage(file="stop-button.png")
    volumeupimage = PhotoImage(file="speaker.png")
    volumedownimage = PhotoImage(file="sound-on.png")
    resumeimage = PhotoImage(file="end.png")
    muteimage = PhotoImage(file="mute.png")
    unmuteimage = PhotoImage(file="play-button.png")
    # Size of images
    searchimage = searchimage.subsample(15, 15)
    playimage = playimage.subsample(15, 15)
    pauseimage = pauseimage.subsample(15, 15)
    stopimage = stopimage.subsample(15, 15)
    volumeupimage = volumeupimage.subsample(15, 15)
    volumedownimage = volumedownimage.subsample(15, 15)
    resumeimage = resumeimage.subsample(15, 15)
    muteimage = muteimage.subsample(15, 15)
    unmuteimage = unmuteimage.subsample(15, 15)

    ##Labels##################################################################
    tracklabel = Label(root, text="Select Audio Track:",
                       bg="silver", font="lucida 20 italic bold")
    tracklabel.grid(row=0, column=0, padx=20, pady=20)
    statuslabel = Label(root, text="", bg="silver",
                        font="lucida 20 italic bold", width=20)
    statuslabel.grid(row=2, column=1)

    ##Entry Widget############################################################
    trackentry = Entry(root, font="lucida 20 bold",
                       width=30, textvar=audiotrack)
    trackentry.grid(row=0, column=1, padx=20, pady=20)

    # Buttons
    searchbutton = Button(root, text="Search", font="lucida 14 bold", bg="blue", width=200,
                          bd=5, activebackground="skyblue", image=searchimage, compound=RIGHT, command=searchmusic)
    searchbutton.grid(row=0, column=2, padx=10, pady=10)
    playbutton = Button(root, text="Play", font="lucida 14 bold", bg="lightgreen", width=200, bd=5,
                        activebackground="green", image=playimage, compound=RIGHT, command=playmusic)
    playbutton.grid(row=1, column=0, padx=10, pady=10)
    root.pausebutton = Button(root, text="Pause", font="lucida 14 bold", bg="lightyellow", width=200, bd=5,
                              activebackground="yellow", image=pauseimage, compound=RIGHT, command=pausemusic)
    root.pausebutton.grid(row=1, column=1, padx=10, pady=10)
    root.resumebutton = Button(root, text="Resume", font="lucida 14 bold", bg="purple", width=200, bd=5,
                               activebackground="purple4", image=resumeimage, compound=RIGHT, command=resumemusic)
    root.resumebutton.grid(row=1, column=1, padx=10, pady=10)
    root.resumebutton.grid_remove()

    volumeupbutton = Button(root, text="Volume Up", font="lucida 14 bold", bg="lightpink", width=200, bd=5,
                            activebackground="red", image=volumeupimage, compound=RIGHT, command=volumeup)
    volumeupbutton.grid(row=1, column=2, padx=10, pady=10)
    stopbutton = Button(root, text="Stop", font="lucida 14 bold", bg="darkred", width=200, bd=5,
                        activebackground="red", image=stopimage, compound=RIGHT, command=stopmusic)
    stopbutton.grid(row=2, column=0, padx=10, pady=10)

    volumedownbutton = Button(root, text="Volume Down", font="lucida 14 bold", bg="lightpink", width=200, bd=5,
                              activebackground="red", image=resumeimage, compound=RIGHT, command=volumedown)
    volumedownbutton.grid(row=2, column=2, padx=10, pady=10)
    root.mutebutton = Button(root, image=muteimage, font="lucida 10 bold",
                             bg="white", bd=5, activebackground="red", command=mutemusic)
    root.mutebutton.grid(row=3, column=3, padx=10, pady=10)
    root.unmutebutton = Button(root, image=unmuteimage, font="lucida 10 bold", bg="white", bd=5, activebackground="red",
                               command=unmutemusic)
    root.unmutebutton.grid(row=3, column=3, padx=10, pady=10)
    root.unmutebutton.grid_remove()

    # Progressbar:
    progressbarlabel = Label(root, text="", bg="orange")
    progressbarlabel.grid(row=0, column=3, rowspan=3, padx=20, pady=20)
    progressbar = Progressbar(
        progressbarlabel, orient=VERTICAL, mode='determinate', value=0, length=190)
    progressbar.grid(row=0, column=0, ipadx=5)
    middlevollabel = Label(progressbarlabel, text="0%",
                           bg="lightgrey", width=3)
    middlevollabel.grid(row=0, column=0)

    # MusicProgressbar:
    progressbarmusiclabel = Label(root, text="", bg="red")
    progressbarmusiclabel.grid(row=3, column=0, columnspan=3, padx=20, pady=20)
    progressbarmusicstarttimelabel = Label(
        progressbarmusiclabel, text="0:00:0", bg="grey")
    progressbarmusicstarttimelabel.grid(row=0, column=0)

    progressbarmusic = Progressbar(
        progressbarmusiclabel, orient=HORIZONTAL, mode='determinate', value=0)
    progressbarmusic.grid(row=0, column=1, ipadx=370, ipady=5)

    progressbarmusicendtimelabel = Label(
        progressbarmusiclabel, text="0:00:0", bg="grey")
    progressbarmusicendtimelabel.grid(row=0, column=2)
    progressbarmusiclabel.grid_remove()


#####################################################################################################
root = Tk()
root.geometry("1100x500+130+50")  # for permanent position
root.title("Music Player_DivyanshuTheBugMen")
root.iconbitmap("headphones.ico")
root.resizable(False, False)  # For lock the window
root.configure(bg="silver")
# Global variable
audiotrack = StringVar()
totalsonglength = 0
# Create Slider:
ss = "Developed by Divyanshu."

count = 0
text = ""
currentvol = 0
sliderlabel = Label(root, text=ss, bg="silver", font="lucida 20 bold ")
sliderlabel.grid(row=4, column=0, padx=20, pady=20, columnspan=3)


def labeltick():
    global count, text
    if(count >= len(ss)):
        count = -1
        text = ""
        sliderlabel.config(text=text)
    else:
        text = text+ss[count]
        sliderlabel.config(text=text)
        count += 1
        sliderlabel.after(200, labeltick)


labeltick()
mixer.init()  # initialse of mixer
createwidget()
root.mainloop()
