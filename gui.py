import PySimpleGUI as sg
import chemLine

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Some text on Row 1')],
          [sg.Text('SiO2%'), sg.InputText(key='-SI-'), sg.Text('Na20+K20%'), sg.InputText(key='-NAK-')],
          [sg.Button('Ok'), sg.Button('Submit')],
          [sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
user_values = []
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):  # if user closes window or clicks cancel
        break

    if event in 'Ok':
        user_values.append([int(values['-SI-']), int(values['-NAK-'])])
    elif event in 'Submit':
        chemLine.make_tas_graph(user_values)

    window['-SI-']('')
    window['-NAK-']('')


window.close()
