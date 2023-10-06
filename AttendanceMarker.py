import webbrowser  #Imports the ability to use the web browser
import pyautogui as PG #Imports the library used to input keystrokes
import time


#The url to the google form used to mark student attendances
form_url = 'https://forms.gle/ExampleFormLink'

#A list of example ID card numbers
ID_numbers_list = ["019283746" #JohnDoe
    ,"657483920" #JaneDoe
    ,"129836475" #LeyreRomea
    ,"009988772" #JohnCena
    ,"198124987" #TonySoprano
        ]

#Registers the web browser (Chrome in this case)
webbrowser.register(
    'GChrome', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
)

#Goes through the list of ID numbers and marks the attendance for each one:
##Opens the attendance form in a new tab
##Presses the keys required to get to the page which asks for ID
##Enters the ID number and finishes the procedure
for ID_number in ID_numbers_list:
    webbrowser.get('GChrome').open_new_tab(form_url)
    time.sleep(3.5)
    PG.press('tab')
    PG.press('enter')
    time.sleep(1.5)
    PG.press("tab")
    time.sleep(0.5)
    PG.write(ID_number)
    PG.press('tab')
    time.sleep(0.5)
    PG.press("space")
    time.sleep(0.5)
    PG.press('tab')
    PG.press('tab')
    PG.press('enter')
    time.sleep(2)

#Once its done, it displays the success gif in a new tab
success_gif = r"https://media.tenor.com/ho7tPHaTCyIAAAAC/brent-rambo-thumbsup.gif"
webbrowser.get('GChrome').open_new_tab(success_gif)








