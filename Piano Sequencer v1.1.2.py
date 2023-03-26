import os
from winsound import Beep
from time import sleep
from sys import stdout
dir_path = os.environ['USERPROFILE']+"/Piano_Sequencer"
if not os.path.isdir(dir_path):
    os.makedirs(dir_path)
os.system('color B')
def scroller():
    a = '...................................'
    for char in a:
        stdout.write(char)
        stdout.flush()
        sleep(0.06)
def piano_engine(notes,bpm):
    notes_list = notes.split()
    Hz = 0
    for i in notes_list:
        valid = False
        ms = 0
        if len(i) == 2:
            freq = {'c':524,'C':555,'d':588,'D':623,'e':660,'f':699,'F':740,'g':784,'G':831,'a':880,'A':933,'b':988}
            for j in freq:
                if j == i[0]:
                    Hz = freq[j]
                    valid = True
            if i[0] not in freq:
                print("(Invalid Note given", i,")",end=" ")
        if len(i) == 3:
            freq = {'c!':262,'C!':278,'d!':294,'D!':312,'e!':330,'f!':350,'F!':370,'g!':392,'G!':415,'a!':440,'A!':467,'b!':494,'c^':1047,'C^':1109,'d^':1175,'D^':1245,'e^':1319,'f^':1397,'F^':1480,'g^':1568,'G^':1662,'a^':1760,'A^':1865,'b^':1976}
            for j in freq:
                if j == i[:2]:
                    Hz = freq[j]
                    valid = True
            if i[:2] not in freq:
                print("(Invalid Note given", i,")",end=" ")
        if bpm == 0:
            time = {'1':300,'2':600,'3':900,'4':1200}
            for j in time:
                if i[-1] == j:
                    ms = time[j]
            if ms == 0:
                print("(Invalid Time given", i,")",end=" ")
        if bpm >0:
            rate = 60000//bpm
            time = {'1':rate,'2':2*rate,'3':3*rate,'4':4*rate}
            for j in time:
                if i[-1] == j:
                    ms = time[j]
            if ms == 0:
                print("(Invalid Time given", i,")",end=" ")
        if valid == True:
            stdout.write(i)
            print(end=" ")
            stdout.flush() 
            Beep(Hz, ms)         
def file():
    print("Enter it's BPM, put 0 for a default value.")
    file_bpm = int(input())
    print("Enter your song to save!")
    new_song = input()
    print("What's the name of the song?")
    name = input() + '.txt'
    path = os.environ['USERPROFILE']+"/Piano_Sequencer/"
    path += name
    print(path)
    full_text = str(file_bpm)+" "
    full_text+=new_song
    with open(path, 'w') as f:
        f.write(full_text)
    print("You can also find the files at \'%USERPROFILE%/Piano_Sequencer/'.")
def file_make():
    file()
    print("Saving", end="")
    scroller()
    print("File Saved!")    
def run_file():
    print("Enter name of the file")
    name = input()
    print("\n")
    path = os.environ['USERPROFILE']+"/Piano_Sequencer/" + name + '.txt'
    print(path)
    with open(path, 'r') as f:
        notes = f.readlines()
    digit = ""
    for i in notes:
        notes_str = i
    for i in notes_str:
        if i.isnumeric() == True:
            digit+=i
        else:
            a = notes_str.index(i)
            break
    notes_final = notes_str[a+1::]
    piano_engine(notes_final, int(digit))
def del_file():
    print("Enter name of the song you want to delete")
    name = input()
    path = os.environ['USERPROFILE']+"/Piano_Sequencer/" + name + '.txt'
    os.remove(path)
    print("Deleting", end = "")
    scroller()
    print("Deleted!")
def settings():
    print("\nWhat would you like to change?")
    print('''\n1)Change color''')
    setting_choice = input()
    if setting_choice == '1':
        print('''\nEach letter and number represents a color:

    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White

    Enter two characters, the first one represents the background color and the second one being the foreground color. 

    Examples: 2D, 5F, 70, ED
    
    Choose a background and text color:''')
    clr = input()
    cmd = "color "+clr
    os.system(cmd)
print('''************************************************************************************************************************
******                                              Piano Sequencer v1.1.2                                        ******
************************************************************************************************************************
Welcome to the Piano Sequencer. Type your notes in order and let the song play!
To type one note, type the note followed by the time period. Use \'!\' or \'^\' to play lower or a higher octave.
Use Capital letters for sharp notes(No flat keys are used in this sequencer.).
Seperate each note by a space
Example: c4 c!4 C1 c^2

1)Enter notes and play song
2)Save a song 
3)Run a song
4)Delete a song
5)Open Settings
6)Exit''')
while True:
    bpm = 0
    print('''
What would you like to do?
''')
    choice = int(input())
    if choice == 1:
        print("Enter bpm(0 for a default value)")
        bpm = int(input())
        print("Enter your notes below")
        notes = input()
        print("\n")
        piano_engine(notes, bpm)
    elif choice == 2:
        file_make()
    elif choice == 3:
        run_file()
    elif choice == 4:
        del_file()
    elif choice == 5:
        settings()
    elif choice == 6:
        print("Thank you! Exiting", end = "")
        scroller()
        break
