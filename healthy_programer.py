from gtts import gTTS # pip install gTTS
import os
import time
import datetime
import threading 
import pyautogui #pip install PyAutoGUI
def play_audio(audio_file_name):
    """
    to install mpg123 run (sudo apt install mpg123) on terminal 
    """
    os.system("mpg123 " + audio_file_name)
def history_file(save_line):
    date = datetime.datetime.now()
    cur_date_time=(date.strftime("%D and Day is %A."))
    with open('history_file.txt','a') as write:
        write.write(f"{save_line} at {time_12} and the date is {cur_date_time}\n")

def new_user():
    """
    this function is use to get name of user and add it into audio file
    """
    files=["welcome.mp3","body_exe.mp3","eyes_exe.mp3","drink_water.mp3","good_bye.mp3"]
    for file_name in files:
        if os.path.exists(file_name):
            print("")
        else:
            play_audio('Alarm_Clock.mp3')
            enter_name=input("Enter your name:")
            welcome=f"{enter_name} welcome to job. This program is made by amish ali."
            body_exe= f"Now it's time to do body exercise.{enter_name} Let's do the body exercise."
            eyes_exe= f"Now it's time to do eyes exercise.{enter_name} Let's do the eyes exercise."
            drink_water= f"Now it's time to dirnk water.{enter_name} Let's drink water."
            good_bye=f"{enter_name} Your job time has expired. have a nice evening. good bye."
            language = 'en'
            if(file_name=="welcome.mp3"):
                myobj = gTTS(text=welcome, lang=language, slow=False)
                myobj.save("welcome.mp3")
            elif(file_name=="body_exe.mp3"):
                myobj = gTTS(text=body_exe, lang=language, slow=False) 
                myobj.save("body_exe.mp3") 
            elif(file_name=="eye_exe.mp3"):
                myobj = gTTS(text=eyes_exe, lang=language, slow=False) 
                myobj.save("eyes_exe.mp3")
            elif(file_name=="drink_water.mp3"):
                myobj = gTTS(text=drink_water, lang=language, slow=False) 
                myobj.save("drink_water.mp3")
            elif(file_name=="good_bye.mp3"):
                myobj = gTTS(text=good_bye, lang=language, slow=False) 
                myobj.save("good_bye.mp3")
            else:
                print("")
def enter():
    """ this function is used to press a and enter after 5 sec of waiting from user response and
    continue the loop...
    """
    pyautogui.press('a',presses=1)
    pyautogui.press('enter')
def good_bye():
    play_audio("good_bye.mp3")
def welcome():
    play_audio("welcome.mp3")
def drink_water():
    play_audio("drink_water.mp3")
def body_exe():
    play_audio("body_exe.mp3")
def eyes_exe():
    play_audio("eyes_exe.mp3")

# formula to get total glass of water and time break.
total_water_ml=3500
one_glass_ml=250
total_time_sec=28800
total_glass=total_water_ml/one_glass_ml
time_to_drink=total_time_sec/total_glass-1800
time_12 = time.strftime('%I: %M: %S %P')
time_condi=int(time.strftime("%H"))
if __name__ == '__main__':

    new_user()
    welcome()
    while(True):
        if(time_condi>=9 and time_condi<10):
            time.sleep(1800)
            a="n"
            while(a.lower() !='y'):
                eyes_exe()
                timer = threading.Timer(5.0, enter) 
                timer.start() 
                a=input("\n\tIf you done eyes exercise then press y to stop:")
            eyes="You done eyes exercise"
            history_file(eyes)
            time.sleep(time_to_drink)
            a="n"
            while(a.lower() !='y'):
                drink_water()
                timer = threading.Timer(5.0, enter) 
                timer.start() 
                a=input("\n\tIf you drank water then press y to stop:")
            water="You drank water"
            history_file(water)
            time.sleep(300)
            a="n"
            while(a.lower() !='y'):
                body_exe()
                timer = threading.Timer(5.0, enter) 
                timer.start() 
                a=input("\n\tIf you done body exercise then press y to stop:")
            body="You done body exercise"
            history_file(body)
        else:
            good_bye()
            break
