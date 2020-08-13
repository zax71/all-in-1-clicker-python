from pynput.keyboard import Controller as keycon
from pynput.keyboard import Key

from pynput.mouse import Button
from pynput.mouse import Controller as mousecon

import time

keyboard = keycon()
mouse = mousecon()

#clicker veriables ----------------------------------------------------------------------------------------
clicklmb = 0 #this is set to 1 or 0 when the left mouse button is pressed (or not) in the clicker window   ¦
clockrmb = 0 #this is set to 1 or 0 when the right mouse button is pressed (or not) in the clicker window  ¦
#                                                                                                          ¦
CPS = 0  #clicks per seccond on the autoclicker                                                            ¦
#                                                                                                          ¦
time = 0  # time to run the autoclicker for (in secconds)                                                  ¦
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
#                                                                                                          ¦
def clicklmb():  #this function activates when the lmb button is pressed in autoclicker menu               ¦
    print("lmb autoclick button pressed") #                                                                ¦
#                                                                                                          ¦
def clickrmb():  #this function activates when the rmb button is pressed in autoclicker menu               ¦
    print("rmb autoclick button pressed")#                                                                 ¦
#                                                                                                          ¦
def clickerstart():  #this functions activates when you press the "start" button in the autocklicker menu  ¦
    print("you tried to start the clicker, it's not done...")#                                             ¦
#mouse button functions -----------------------------------------------------------------------------------
def mbholddown_start(): #when you press start on the MB hold down program, this run's                      ¦
    print("you started the mouse button holder downer!")#                                                  ¦
#text spammer functions------------------------------------------------------------------------------------



