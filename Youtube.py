import pytube
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename,askdirectory



'''Hi, this program is my gift to you'''


print('Hi, which video would u like to take from Youtube?')

correctLink = False

while(True):
    if correctLink is not True:
        url = input("Give URL: ")       #asking user to input URL
    print()
    
    try:
        
        pytube.YouTube(url)  #checking valid URL or not
        correctLink=True    #if valid set flag to True state
            
        #print(pytube.YouTube(url).streams.get_highest_resolution().download(input("Full path to folder to store: ")))
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askdirectory()
        assert filename!=''# show an "Open" dialog box and return the path to the selected file
        pytube.YouTube(url).streams.get_highest_resolution().download(filename)
        
        print()
        break
        
    except AssertionError:
        print('You pressed "Cancel" Button or not such Folder (/*_*\)')
        if input('Do You want to try select Folder again? (y/n): ').lower()=='y':
            continue
        break
    
    except:
        print('no such link in youtube, or access denied (/^_^\)')
        if(input('Would u like to take one more attemption? (y/n): ').lower()=='y'): 
            os.system("CLS")
            continue
        break
        
        

os.system("PAUSE")

