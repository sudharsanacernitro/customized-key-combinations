#!/home/sudharsan/myenv/bin/python3
import keyboard
import subprocess
import os
a=0
def on_key_event(e):
    global a
    if (e.event_type == keyboard.KEY_DOWN):
        if 'alt'==e.name :
            a=1
            print(e.name)
        if (('1'==e.name)and(a==1)):
            os.system("gnome-terminal --tab -- bash -c 'echo 'hai'; exec bash'")
            a=0
        elif (('2'==e.name)and(a==1)):
            os.system("google-chrome")
            a=0  
        elif (('3'==e.name)and(a==1)):
            os.system("mousepad")
            a=0  
        else:
            pass
        if(a==1)and(e.name!='alt'):
            a=0
    return e.name

l=keyboard.hook(on_key_event)
keyboard.wait('esc')  # Wait for the 'esc' key to be pressed to exit the program

