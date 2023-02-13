import time
import os
import winsound
path = os.environ['USERPROFILE']+"/Piano_Sequencer"
if not os.path.isdir(path):
   os.makedirs(path)
os.system('color B')
def piano_engine(notes):
    notes_list = notes.split()
    global freq
    freq  = 0
    global time
    time = 0
    for i in notes_list:
        if len(i) == 2:
            if i[0] == 'c': 
                freq = 524
            elif i[0] == 'C':
                freq = 555
            elif i[0] == 'd':
                freq = 588
            elif i[0] == 'D':
                freq = 623
            elif i[0] == 'e':
                freq = 660
            elif i[0] == 'f':
                freq = 699
            elif i[0] == 'F':
                freq = 740
            elif i[0] == 'g':
                freq = 784
            elif i[0] == 'G':
                freq = 831
            elif i[0] == 'a':
                freq = 880
            elif i[0] == 'A':
                freq = 933
            elif i[0] == 'b':
                freq = 988
            else:
                print("Invalid note given", i)
        if len(i) == 3:
            if i[:2] == 'c!':
                freq = 262
            elif i[:2] == 'C!':
                freq = 278
            elif i[:2] == 'd!':
                freq = 294
            elif i[:2] == 'D!':
                freq = 312
            elif i[:2] == 'e!':
                freq = 330
            elif i[:2] == 'f!':
                freq = 350
            elif i[:2] == 'F!':
                freq = 370
            elif i[:2] == 'g!':
                freq = 392
            elif i[:2] == 'G!':
                freq = 415
            elif i[:2] == 'a!':
                freq = 440
            elif i[:2] == 'A!':
                freq = 467
            elif i[:2] == 'b!':
                freq = 494
            elif i[:2] == 'c^':
                freq = 1047
            elif i[:2] == 'C^':
                freq = 1109
            elif i[:2] == 'd^':
                freq = 1175
            elif i[:2] == 'D^':
                freq = 1245
            elif i[:2] == 'e^':
                freq = 1319
            elif i[:2] == 'f^':
                freq = 1397
            elif i[:2] == 'F^':
                freq = 1480
            elif i[:2] == 'g^':
                freq = 1568
            elif i[:2] == 'G^':
                freq = 1662
            elif i[:2] == 'a^':
                freq = 1760
            elif i[:2] == 'A^':
                freq = 1865
            elif i[:2] == 'b^':
                freq = 1976
            else:
                print("Invalid note given", i)
        if i[-1] == '1':
            time = 300
        elif i[-1] == '2':
            time = 600
        elif i[-1] == '3':
            time = 900
        elif i[-1] == '4':
            time = 1200
        else:
            print("Invalid Time given", i)
        if freq == 0 or time == 0:
            break
        winsound.Beep(freq, time)
        import time
import os
from PianoEngine import piano_engine
def file_make():
    def file():
        print("Enter your song to save!")
        new_song = input()
        print("What's the name of the song?")
        name = input() + '.txt'
        path = os.environ['USERPROFILE']+"/Piano_Sequencer/"
        path += name
        print(path)
        with open(path, 'w')as f:
            f.write(new_song)
        print("You can also find the files at \'%USERPROFILE%/Piano_Sequencer/'.")
    def loader():
        def scroller():
            a = ".............................................."
            a.split()
            for i in a:
                i.split()
                for j in i:
                    print(j, end="")
                time.sleep(0.08)
        print("Loading", end="")
        scroller()
        print("File Saved!")
    file()
    loader()
def run_file():
    print("Enter name of the file")
    name = input()
    path = os.environ['USERPROFILE']+"/Piano_Sequencer/" + name + '.txt'
    with open(path) as f:
        notes = f.readlines()
    notes_str = ""
    for i in notes:
        notes_str += i
    piano_engine(notes_str)
def del_file():
    print("Enter name of the song you want to delete")
    name = input()
    path = os.environ['USERPROFILE']+"/Piano_Sequencer/" + name + '.txt'
    os.remove(path)
    def scroller():
            a = ".............................................."
            a.split()
            for i in a:
                i.split()
                for j in i:
                    print(j, end="")
                time.sleep(0.08)
    print("Deleting", end = "")
    scroller()
    print("Deleted!")
def scroller():
            a = ".............................................."
            a.split()
            for i in a:
                i.split()
                for j in i:
                    print(j, end="")
                time.sleep(0.08)
print('''******************************************************************************************************************
*                                               Piano Sequecner v1.0.0                                            *
******************************************************************************************************************
Welcome to the Piano Sequencer. Type your notes in order and let the song play!
To type one note, type the note followed by the time period. Use \'!\' or \'^\' to play lower or a higher octave.
Use Capital letters for sharp notes(No flat keys are used in this sequencer.).
Seperate each note by a space
Example: c4 c!4 C1 c^2''')
while True:
    print('''
What would you like to do?
1)Enter notes and play song
2)Save a song 
3)Run a song
4)Delete a song
5)Quit''')
    choice = int(input())
    if choice == 1:
        print("Enter your notes below")
        notes = input()
        piano_engine(notes)
    elif choice == 2:
        file_make()
    elif choice == 3:
        run_file()
    elif choice == 4:
        del_file()
    elif choice == 5:
        print("Thank you! Exiting", end = "")
        scroller()
        break
    