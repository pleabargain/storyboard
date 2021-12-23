import PySimpleGUI as sg

# Add some color
# to the window
sg.theme('SandyBeach')	

# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
	[sg.Text('Please enter your Name, Age, Phone')],
	[sg.Text('Name', size =(15, 1)), sg.InputText()],
	[sg.Text('Age', size =(15, 1)), sg.InputText()],
	[sg.Text('Phone', size =(15, 1)), sg.InputText()],
	[sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()

# The input data looks like a simple list
# when automatic numbered
print(event, values[0], values[1], values[2])
