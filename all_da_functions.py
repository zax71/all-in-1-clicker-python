from pynput.keyboard import Controller as keycon
from pynput.keyboard import Key

from pynput.mouse import Button
from pynput.mouse import Controller as mousecon

import time

keyboard = keycon()
mouse = mousecon()

#clicker veriables ----------------------------------------------------------------------------------------
clickerlmb = 0 #this is set to 1 or 0 when the left mouse button is pressed (or not) in the clicker window   ¦
clickermb = 0 #this is set to 1 or 0 when the right mouse button is pressed (or not) in the clicker window  ¦
#                                                                                                          ¦
CPS = 0  #clicks per seccond on the autoclicker                                                            ¦
#                                                                                                          ¦
clickertime = 0  # time to run the autoclicker for (in secconds)                                                  ¦
#mouse button hold down veriables--------------------------------------------------------------------------
mbholddown_rmb = 0 #if the right mouse button button is pressed, this whill be set to 1                    ¦
mbholddown_lmb = 0 #if the left mouse button button is pressed, this whill be set to 1                     ¦
#                                                                                                          ¦
mbholddown_time = 0 #the time that the mouse button whill be held down for                                 ¦
#text spammer veriables -----------------------------------------------------------------------------------
text_to_spam = "" #the text to spam                                                                        ¦
#                                                                                                          ¦
ammount_to_spam = 0 #the ammount of time to spam "text_to_spam" veriable                                   ¦
#clicker functions-----------------------------------------------------------------------------------------
def clickerstart():  #this functions activates when you press the "start" button in the autocklicker menu  ¦

    if clickerlmb == 1: #if you sellected to click the LMB then this block of code whill be run

        for i in range(0, clickertime): #looping for "clickertime" so we get more than 1 second of clicking

            for i in range(0, CPS): #looping for the CPS so we get more than 1 click

                delay = 1 / CPS #working out the delay from the CPS value
                mouse.press(Button.left) #pressing the LMB...
                print("click")
                time.sleep(int(delay)) #sleeping for the before worked out time
                mouse.release(Button.left) #...and releasing it

    
    if clickerrmb == 1: #if you sellected to click the LMB then this block of code whill be run

        for i in range(0, clickertime): #looping for "clickertime" so we get more than 1 second of clicking

            for i in range(0, CPS): #looping for the CPS so we get more than 1 click

                delay = 1 / CPS #working out the delay from the CPS value
                mouse.press(Button.right) #pressing the RMB...
                print("click")
                time.sleep(int(delay)) #sleeping for the before worked out time
                mouse.release(Button.right) #...and releasing it
#mouse button functions -----------------------------------------------------------------------------------
def mbholddown_start(): #when you press start on the MB hold down program, this run's                      ¦
    print("you started the mouse button holder downer!")#                                                  ¦
#text spammer functions------------------------------------------------------------------------------------
def text_spam_start(): #this function whill run when you click start on the text spamer                    ¦
    print("you started the text spammer!") #                                                               ¦
#----------------------------------------------------------------------------------------------------------
