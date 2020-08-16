from pynput.keyboard import Controller as keycon #importing pynput - the thing that presses the buttons
from pynput.keyboard import Key

from pynput.mouse import Button
from pynput.mouse import Controller as mousecon #you finnished importing pynput, yay! that was on ly 4 whole lines!

import time #importing time, do i realy need to say that?

keyboard = keycon()  #more pynput junk
mouse = mousecon()   #another bit of this modules junk (pynput)

#clicker veriables ----------------------------------------------------------------------------------------
clickerlmb = 0 #this is set to 1 or 0 when the left mouse button is pressed (or not) in the clicker window ¦
clickermb = 0 #this is set to 1 or 0 when the right mouse button is pressed (or not) in the clicker window ¦
#                                                                                                          ¦
CPS = 0  #clicks per seccond on the autoclicker                                                            ¦
#                                                                                                          ¦
clickertime = 0  # time to run the autoclicker for (in secconds)                                           ¦
#mouse button hold down veriables--------------------------------------------------------------------------
mbholddown_rmb = 0 #if the right mouse button button is pressed, this whill be set to 1                    ¦
mbholddown_lmb = 0 #if the left mouse button button is pressed, this whill be set to 1                     ¦
#                                                                                                          ¦
mbholddown_time = 0 #the time that the mouse button whill be held down for (in secconds)                   ¦
#text spammer veriables -----------------------------------------------------------------------------------
text_to_spam = "" #the text to spam                                                                        ¦
#                                                                                                          ¦
ammount_to_spam = 0 #the ammount of time to spam "text_to_spam" veriable                                   ¦
spam_delay = 0 #the delay between text while spaming (in secconds)                                         ¦
#clicker functions---------------------------------------------------------------------------------------------
def clickerstart():  #this functions activates when you press the "start" button in the autocklicker menu      ¦
#                                                                                                              ¦
    if clickerlmb == 1: #if you sellected to click the LMB then this block of code whill be run                ¦
#                                                                                                              ¦
        for i in range(0, clickertime): #looping for "clickertime" so we get more than 1 second of clicking    ¦
#                                                                                                              ¦
            for i in range(0, CPS): #looping for the CPS so we get more than 1 click                           ¦
#                                                                                                              ¦
                delay = 1 / CPS #working out the delay from the CPS value                                      ¦
                mouse.press(Button.left) #pressing the LMB...                                                  ¦
#                                                                                                              ¦
                time.sleep(int(delay)) #sleeping for the before worked out time                                ¦
                mouse.release(Button.left) #...and releasing it                                                ¦
#                                                                                                              ¦
#                                                                                                              ¦
    if clickerrmb == 1: #if you sellected to click the LMB then this block of code whill be run                ¦
#                                                                                                              ¦
        for i in range(0, clickertime): #looping for "clickertime" so we get more than 1 second of clicking    ¦
#                                                                                                              ¦
            for i in range(0, CPS): #looping for the CPS so we get more than 1 click                           ¦
#                                                                                                              ¦
                delay = 1 / CPS #working out the delay from the CPS value                                      ¦
                mouse.press(Button.right) #pressing the RMB...                                                 ¦
#                                                                                                              ¦
                time.sleep(int(delay)) #sleeping for the before worked out time                                ¦
                mouse.release(Button.right) #...and releasing it                                               ¦
#mouse button functions ---------------------------------------------------------------------------------------
def mbholddown_start(): #when you press start on the MB hold down program, this run's                          ¦
#                                                                                                              ¦ 
    if mbholddown_rmb == 1: #if you click the rmb hold down button on the mb holddown page this whill activcate¦
        mouse.press(Button.right) #press RMB...                                                                ¦
        time.sleep(mbholddown_time) #sleep for the time specified in the GUI                                   ¦
        mouse.release(Button.right) #...and release it                                                         ¦
#                                                                                                              ¦
    if mbholddown_lmb == 1: #if you click the lmb hold down button on the mb holddown page this whill activcate¦
        mouse.press(Button.left) #press RMB...                                                                 ¦
        time.sleep(mbholddown_time) #sleep for the time specified in the GUI                                   ¦
        mouse.release(Button.left) #...and release it                                                          ¦
#text spammer functions----------------------------------------------------------------------------------------
def text_spam_start(): #this function whill run when you click start on the text spamer                    ¦
    for i in range(0, ammount_to_spam): #loop for the ammount of stuff to spam                             ¦
        keyboard.type(text_to_spam) #typing the spam text                                                  ¦
        time.sleep(spam_delay)#sleeping for the spam delay                                                 ¦
#----------------------------------------------------------------------------------------------------------
