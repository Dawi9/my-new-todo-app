import FreeSimpleGUI as sg


# Function to convert feet & inches to meters
def convert_to_meters(feet, inches):
    return (feet * 0.3048) + (inches * 0.0254)


# Define GUI layout 
layout = [
    [sg.Text("Enter feet:"), sg.InputText(key="feet", size=(20, 1))],
    [sg.Text("Enter inches:"), sg.InputText(key="inches", size=(20, 1))],
    [sg.Button("Convert")],
    [sg.Text("", key="result", size=(20, 1))]
]

# Create window
window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Convert":
        try:
            feet = float(values["feet"] or 0)  # Default to 0 if empty
            inches = float(values["inches"] or 0)  # Default to 0 if empty

            if feet < 0 or inches < 0:
                window["result"].update("Please enter positive numbers!")
            else:
                meters = convert_to_meters(feet, inches)
                window["result"].update(f"{meters:.3f} m")  # Format to 3 decimal places
        except ValueError:
            window["result"].update("Please enter valid numbers!")

window.close()
