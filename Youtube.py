import os
from urllib.error import URLError
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import glob
import moviepy.editor
import shutil

root = Tk()
root.title("Youtube Downloader")
p = PhotoImage(file='icon.png')
root.iconphoto(False, p)
root.resizable(0, 0)

l1 = Label(root, text="Enter the video link :- ").grid(row=0, column=0)
e = Entry(root, width=60, borderwidth=5)
e.grid(row=0, column=1)
folder = ""

version = ["720p", "480p", "360p"]


def directory():
    global folder
    folder = filedialog.askdirectory()
    if len(folder) > 1:
        locationerror = Label(root, text=folder, width=30)
        locationerror.grid(row=3, column=1, columnspan=3, padx=40)
        locationerror1 = Label(root, text=" ", width=24, bd=2, relief=SUNKEN, anchor=E)
        locationerror1.grid(row=9, column=0, columnspan=2, sticky=W + E)
    else:
        locationerror1 = Label(root, text="Choose Folder Properly", width=24, bd=2, relief=SUNKEN, anchor=E)
        locationerror1.grid(row=9, column=0, columnspan=2, sticky=W + E)
        locationerror = Label(root, text="")
        locationerror.grid(row=3, column=1)


save = Button(root, text="Select Folder", command=directory).grid(row=1, column=1, rowspan=2, padx=20, pady=15)

try:
    def video():
        # noinspection PyGlobalUndefined
        global select1
        name = choose.get()
        red = str(choose.get())
        vid = e.get()
        if e.index("end") != 0 and red != "":
            yt = YouTube(vid)
            dd = Label(root, text=yt.title + " is downloading....", width=24, bd=2, relief=SUNKEN, anchor=E)
            dd.grid(row=9, column=0, columnspan=3, sticky=W + E)
            if name == version[0]:
                try:
                    ac = ['mp4a.40.2', 'mp3']
                    if ac[0] == 'mp4a.40.2':
                        select1 = yt.streams.filter(resolution='720p', file_extension='mp4', audio_codec=ac[0]).first()
                        select1.download(folder)
                    else:
                        select1 = yt.streams.filter(resolution='720p', file_extension='mp4', audio_codec=ac[1]).first()
                        select1.download(folder)
                except AttributeError:
                    qq = Label(root, text="There is no audio, try selecting another resolution", width=24, bd=2,
                               relief=SUNKEN, anchor=E)
                    qq.grid(row=9, column=0, columnspan=3, sticky=W + E)
            elif name == version[1]:
                try:
                    ac = ['mp4a.40.2', 'mp3']
                    if ac[0] == 'mp4a.40.2':
                        select1 = yt.streams.filter(resolution='480p', file_extension='mp4', audio_codec=ac[0]).first()
                        select1.download(folder)
                    else:
                        select1 = yt.streams.filter(resolution='480p', file_extension='mp4', audio_codec=ac[1]).first()
                        select1.download(folder)
                except AttributeError:
                    qq = Label(root, text="There is no audio, try selecting 360p", width=24, bd=2, relief=SUNKEN,
                               anchor=E)
                    qq.grid(row=9, column=0, columnspan=2, sticky=W + E)
            elif name == version[2]:
                try:
                    ac = ['mp4a.40.2', 'mp3']
                    if ac[0] == 'mp4a.40.2':
                        select1 = yt.streams.filter(resolution='360p', file_extension='mp4', audio_codec=ac[0]).first()
                        select1.download(folder)
                    else:
                        select1 = yt.streams.filter(resolution='360p', file_extension='mp4', audio_codec=ac[1]).first()
                        select1.download(folder)
                except AttributeError:
                    qq = Label(root, text="There is no audio, this file cannot be downloaded.", width=24, bd=2,
                               relief=SUNKEN, anchor=E)
                    qq.grid(row=9, column=0, columnspan=2, sticky=W + E)
            f = str(folder)
            for filename in glob.iglob(os.path.join(f, '*.mp4')):
                os.rename(filename, filename[:-4] + '.mkv')
            dd.config(text=yt.title + ".mkv Download Complete.")
        else:
            entryerror = Label(root, text="Enter Url Properly / You have not selected a Video Format. ", width=24, bd=2,
                               relief=SUNKEN, anchor=E)
            entryerror.grid(row=9, column=0, columnspan=2, sticky=W + E)


    def audio1():
        # noinspection PyGlobalUndefined
        global select1
        vid = e.get()
        mm = Label(root, text="The Audio is downloading....", width=24, bd=2, relief=SUNKEN, anchor=E)
        mm.grid(row=9, column=0, columnspan=2, sticky=W + E)
        if e.index("end") != 0:
            yt = YouTube(vid)
            select1 = yt.streams.filter(only_audio=True).first()
            direct = os.getcwd()
            select1.download(direct, filename='Youtubee')
            f = str(folder)
            rt = str(direct+"/"+yt.title+".mp3")
            base = os.path.basename(rt)
            direct = os.getcwd()
            videos = moviepy.editor.AudioFileClip("Youtubee.mp4")
            videos.write_audiofile("Youtube.mp3", bitrate='3000k')
            if base.find("|") != -1:
                base = base.replace("|", "-")
            else:
                base = base
            imput = str(direct + r"\\" + "Youtube.mp3")
            output = str(f+r"\\"+base)
            shutil.move(imput, output)
            os.remove("Youtubee.mp4")
            mm.config(text=yt.title + " .mp3 Download Complete.")
        else:
            entryerror = Label(root, text="Enter URL Properly", width=24, bd=2, relief=SUNKEN, anchor=E)
            entryerror.grid(row=9, column=0, columnspan=2, sticky=W + E)


    b1 = Button(root, text="Download Video", command=video)
    b1.grid(row=6, column=1)
    b2 = Button(root, text="Download Audio", command=audio1)
    b2.grid(row=8, column=1, pady=10)


    def clear():
        e.delete(0, END)
        gg = Label(root, text=" ", width=24, bd=2, relief=SUNKEN, anchor=E)
        gg.grid(row=9, column=0, columnspan=2, sticky=W + E)


    clear = Button(root, text="New URL", command=clear).grid(row=1, column=0, rowspan=2, padx=20, pady=15)
except (ConnectionAbortedError, ConnectionError, ConnectionRefusedError, ConnectionResetError, URLError):
    status = Label(root, text="Connection Error!", width=24, bd=2, relief=SUNKEN, anchor=E)
    status.grid(row=9, column=0, columnspan=2, sticky=W + E)

choose = ttk.Combobox(root, values=version)
sss = Label(root, text="Choose the Video Format :- ").grid(row=5, column=0)
choose.grid(row=5, column=1, padx=10, pady=1)
rr = Label(root, text=" ", width=24, bd=2, relief=SUNKEN, anchor=E)
rr.grid(row=9, column=0, columnspan=2, sticky=W + E)

root.mainloop()
