import wolframalpha
import wikipedia
import PySimpleGUI as sg
import pyttsx3

client = wolframalpha.Client('PJH658-LHQUPHXLAL')

sg.theme('dark green3')
layout = [  [sg.Text('Hi, I am your Virtual Assistant PyViA')],
            [sg.Text('Enter a command:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('PyViA', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    try:
        res = client.query(values[0])
        msg = next(res.results).text
    except:
        try:
            msg = wikipedia.summary(values[0], sentences=1)
        except:
            msg = "Sorry, No results found!!"

    sg.PopupNonBlocking(msg)
    engine = pyttsx3.init()
    engine.say(msg)
    engine.runAndWait()

window.close()
