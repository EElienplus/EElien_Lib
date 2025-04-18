EElienLib
Thank you for using EElienLib! This library provides a collection of useful Python functions for various tasks, including basic arithmetic, Tkinter GUI development, image manipulation using PIL, data handling (JSON, CSV), web interactions, system utilities, and more.
Installation
To use this library, simply copy the provided Python code into a .py file (e.g., EElienLib.py) and ensure it's in the same directory as your project or within your Python path. No formal installation via pip is required for this single-file library.
Getting Started
To start using the functions in your Python project, import the library:
import EElienLib

Then, you can call the functions directly using the module name:
result = EElienLib.add(5, 3)
print(result)
```python
import EElienLib
from tkinter import Tk

root = Tk()
root.title("My First Window")
root.geometry("400x300")
root.configure(background="lightblue")
EElienLib.addWindowText(root, "Hello Tkinter!")
root.mainloop()

Function Documentation
Here's a detailed overview of the functions available in this library:
Basic Arithmetic
* add(num1, num2)
   * Parameters: num1 (int/str), num2 (int/str)
   * Returns: int - The sum of num1 and num2.
result = EElienLib.add("10", 5)
print(result)  # Output: 15

* subtract(num1, num2)
   * Parameters: num1 (int/str), num2 (int/str)
   * Returns: int - The difference between num1 and num2.
result = EElienLib.subtract(20, "7")
print(result)  # Output: 13

* multiply(num1, num2)
   * Parameters: num1 (int/str), num2 (int/str)
   * Returns: int - The product of num1 and num2.
result = EElienLib.multiply("3", 6)
print(result)  # Output: 18

* divide(num1, num2)
   * Parameters: num1 (int/str), num2 (int/str)
   * Returns: float - The quotient of num1 divided by num2.
result = EElienLib.divide(15, "4")
print(result)  # Output: 3.75

* helloWorld()
   * Parameters: None
   * Returns: None
EElienLib.helloWorld()  # Output: Hello, World

Tkinter GUI Functions
* createWindow(width, height, bcgColor, title)
   * Parameters:
      * width (int): The width of the window in pixels.
      * height (int): The height of the window in pixels.
      * bcgColor (str): The background color of the window (e.g., "lightblue", "#f0f0f0").
      * title (str): The title of the window.
   * Returns: Tk - The Tkinter Tk object (the main window).
from tkinter import Tk
root = EElienLib.createWindow(400, 300, "lightblue", "My First Window")
root.mainloop()

* addWindowText(root, text)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * text (str): The text to display in the label.
   * Returns: Label - The Tkinter Label object.
from tkinter import Tk
root = Tk()
label = EElienLib.addWindowText(root, "Hello Tkinter!")
label.pack()
root.mainloop()

* addButton(root, text, command=None)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * text (str): The text to display on the button.
      * command (function, optional): The function to be called when the button is clicked.
   * Returns: Button - The Tkinter Button object.
from tkinter import Tk
def say_hello():
   print("Hello!")
root = Tk()
button = EElienLib.addButton(root, "Click Me", command=say_hello)
button.pack()
root.mainloop()

* addRadioButton(root, text, variable, value)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * text (str): The text to display next to the radio button.
      * variable (StringVar): A Tkinter StringVar object to hold the selected value.
      * value: The value associated with this radio button.
   * Returns: Radiobutton - The Tkinter Radiobutton object.
from tkinter import Tk, StringVar
root = Tk()
var = StringVar()
radio1 = EElienLib.addRadioButton(root, "Option 1", var, "option1")
radio2 = EElienLib.addRadioButton(root, "Option 2", var, "option2")
radio1.pack()
radio2.pack()
root.mainloop()

* addCheckButton(root, text, variable)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * text (str): The text to display next to the check button.
      * variable (IntVar): A Tkinter IntVar object (0 for unchecked, 1 for checked).
   * Returns: Checkbutton - The Tkinter Checkbutton object.
from tkinter import Tk, IntVar
root = Tk()
var = IntVar()
check = EElienLib.addCheckButton(root, "Check this box", var)
check.pack()
root.mainloop()

* getColor(root)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
   * Returns: tuple - A tuple containing the selected color's RGB values and hexadecimal code (e.g., ((255, 0, 0), '#ff0000')), or None if the user cancels.
from tkinter import Tk
root = Tk()
color = EElienLib.getColor(root)
if color:
   print(color)
root.mainloop()

* addTextField(root)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
   * Returns: Entry - The Tkinter Entry object.
from tkinter import Tk
root = Tk()
entry = EElienLib.addTextField(root)
entry.pack()
root.mainloop()

* getTextFieldText(textField)
   * Parameters:
      * textField (Entry): The Tkinter Entry object.
   * Returns: str - The text in the entry field.
from tkinter import Tk
root = Tk()
entry = EElienLib.addTextField(root)
entry.pack()
text = EElienLib.getTextFieldText(entry)
print(text)
root.mainloop()

* addImage(root, image_path)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * image_path (str): The path to the image file.
   * Returns: Label - The Tkinter Label object displaying the image, or None if the image is not found.
from tkinter import Tk
root = Tk()
image_label = EElienLib.addImage(root, "image.png") # Replace image.png
if image_label:
   image_label.pack()
root.mainloop()

* addListener(widget, action=None)
   * Parameters:
      * widget (Widget): The Tkinter widget object.
      * action (function, optional): The function to be called when the widget is interacted with.
   * Returns: None
from tkinter import Tk, Button
root = Tk()
def on_click():
   print("Button clicked!")
button = Button(root, text="Click")
EElienLib.addListener(button, on_click)
button.pack()
root.mainloop()

* clearWindow(root)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
   * Returns: None
from tkinter import Tk, Label, Button
root = Tk()
label = Label(root, text="Label")
button = Button(root, text="Button")
label.pack()
button.pack()
EElienLib.clearWindow(root) # Destroys label and button
root.mainloop()

* enableMovement(root, img_label, movementSpeed)
   * Parameters:
      * root (Tk): The Tkinter Tk window object.
      * img_label (Label): The Tkinter Label object displaying the image.
      * movementSpeed (int): The number of pixels to move the image per key press.
   * Returns: None
from tkinter import Tk
root = Tk()
image_label = EElienLib.addImage(root, "image.png") # Replace with image
if image_label:
 EElienLib.enableMovement(root, image_label, 10)
 image_label.pack()
root.mainloop()

* addDropdown(root, values, variable)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * values (list): A list of strings to be displayed in the dropdown.
      * variable (StringVar): A Tkinter StringVar object to hold the selected value.
   * Returns: ttk.Combobox - The Tkinter ttk.Combobox object.
from tkinter import Tk, StringVar
from tkinter import ttk
root = Tk()
var = StringVar()
dropdown = EElienLib.addDropdown(root, ["Option 1", "Option 2", "Option 3"], var)
dropdown.pack()
root.mainloop()

* getDropdownValue(dropdown)
   * Parameters:
      * dropdown (ttk.Combobox): The Tkinter ttk.Combobox object.
   * Returns: str - The selected value.
from tkinter import Tk, StringVar
from tkinter import ttk
root = Tk()
var = StringVar()
dropdown = EElienLib.addDropdown(root, ["A", "B", "C"], var)
dropdown.pack()
value = EElienLib.getDropdownValue(dropdown)
print(value)
root.mainloop()

* addListbox(root, values, selectmode=SINGLE)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * values (list): A list of strings to be displayed in the listbox.
      * selectmode (str): The selection mode for the listbox (e.g., SINGLE, MULTIPLE).
   * Returns: Listbox - The Tkinter Listbox object.
from tkinter import Tk
root = Tk()
listbox = EElienLib.addListbox(root, ["Item 1", "Item 2", "Item 3"], selectmode="SINGLE")
listbox.pack()
root.mainloop()

* getListboxSelection(listbox)
   * Parameters:
      * listbox (Listbox): The Tkinter Listbox object.
   * Returns: list - A list of the selected strings.
from tkinter import Tk
root = Tk()
listbox = EElienLib.addListbox(root, ["X", "Y", "Z"], selectmode="MULTIPLE")
listbox.pack()
selection = EElienLib.getListboxSelection(listbox)
print(selection)
root.mainloop()

* addScale(root, from_, to, variable, label="")
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * from_ (int/float): The minimum value of the scale.
      * to (int/float): The maximum value of the scale.
      * variable (IntVar or DoubleVar): A Tkinter variable to hold the current value.
      * label (str, optional): An optional label for the scale.
   * Returns: Scale - The Tkinter Scale object.
from tkinter import Tk, IntVar
root = Tk()
var = IntVar()
scale = EElienLib.addScale(root, 0, 100, var, label="Volume")
scale.pack()
root.mainloop()

* getScaleValue(scale)
   * Parameters:
      * scale (Scale): The Tkinter Scale object.
   * Returns: int or float - The current value of the scale.
from tkinter import Tk, IntVar
root = Tk()
var = IntVar()
scale = EElienLib.addScale(root, 0, 100, var)
scale.pack()
value = EElienLib.getScaleValue(scale)
print(value)
root.mainloop()

* addProgressBar(root, max_value)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * max_value (int): The maximum value of the progress bar.
   * Returns: ttk.Progressbar - The Tkinter ttk.Progressbar object.
from tkinter import Tk
from tkinter import ttk
root = Tk()
progressbar = EElienLib.addProgressBar(root, 100)
progressbar.pack()
root.mainloop()

* updateProgressBar(progressbar, value)
   * Parameters:
      * progressbar (ttk.Progressbar): The Tkinter ttk.Progressbar object.
      * value (int): The current value to set for the progress bar.
   * Returns: None
from tkinter import Tk
from tkinter import ttk
root = Tk()
progressbar = EElienLib.addProgressBar(root, 100)
progressbar.pack()
EElienLib.updateProgressBar(progressbar, 50)
root.mainloop()

* showInfoDialog(title, message)
   * Parameters:
      * title (str): The title of the message box.
      * message (str): The message to display.
   * Returns: None
from tkinter import Tk
root = Tk()
EElienLib.showInfoDialog("Information", "This is an info message.")
root.mainloop()

* showErrorDialog(title, message)
   * Parameters:
      * title (str): The title of the message box.
      * message (str): The error message to display.
   * Returns: None
from tkinter import Tk
root = Tk()
EElienLib.showErrorDialog("Error", "An error occurred!")
root.mainloop()

* askYesNoDialog(title, message)
   * Parameters:
      * title (str): The title of the dialog.
      * message (str): The question to ask.
   * Returns: bool - True if the user clicks "Yes", False if they click "No".
from tkinter import Tk
root = Tk()
result = EElienLib.askYesNoDialog("Question", "Do you want to continue?")
print(result)
root.mainloop()

* openFileDialog()
   * Parameters: None
   * Returns: str - The path to the selected file, or an empty string if the user cancels.
from tkinter import Tk
root = Tk()
filepath = EElienLib.openFileDialog()
if filepath:
   print("Selected file:", filepath)
root.mainloop()

* saveFileDialog()
   * Parameters: None
   * Returns: str - The path where the user wants to save the file, or an empty string if the user cancels.
from tkinter import Tk
root = Tk()
savepath = EElienLib.saveFileDialog()
if savepath:
   print("Save path:", savepath)
root.mainloop()

* createFrame(root, bd=2, relief=SUNKEN)
   * Parameters:
      * root (Tk or Toplevel): The parent Tkinter window object.
      * bd (int, optional): The border width of the frame (default is 2).
      * relief (str, optional): The type of border relief (e.g., SUNKEN, RAISED, GROOVE, RIDGE, SOLID, FLAT, default is SUNKEN).
   * Returns: Frame - The Tkinter Frame object.
from tkinter import Tk, Frame
root = Tk()
frame = EElienLib.createFrame(root, bd=5, relief="raised")
frame.pack()
root.mainloop()

* packWidgets(widgets, **kwargs)
   * Parameters:
      * widgets (list): A list of Tkinter widget objects.
      * **kwargs: Keyword arguments to be passed to the pack() method (e.g., side=LEFT, fill=X, padx=5, pady=5).
   * Returns: None
from tkinter import Tk, Label, Button
root = Tk()
label = Label(root, text="Label 1")
button = Button(root, text="Button 1")
EElienLib.packWidgets([label, button], side="left", padx=10)
root.mainloop()

* gridWidgets(widgets, rows, cols, **kwargs)
   * Parameters:
      * widgets (list): A list of Tkinter widget objects.
      * rows (int): The number of rows in the grid.
      * cols (int): The number of columns in the grid.
      * **kwargs: Keyword arguments to be passed to the grid() method (e.g., padx=5, pady=5, sticky=NSEW).
   * Returns: None
from tkinter import Tk, Label, Button
root = Tk()
label1 = Label(root, text="Label 1")
button1 = Button(root, text="Button 1")
label2 = Label(root, text="Label 2")
button2 = Button(root, text="Button 2")
EElienLib.gridWidgets([label1, button1, label2, button2], 2, 2, padx=5, pady=5)
root.mainloop()

* bindEvent(widget, event, action)
   * Parameters:
      * widget (Widget): The Tkinter widget object.
      * event (str): The event to bind (e.g., <Button-1>, <Key-Return>).
      * action (function): The function to be called when the event occurs.
   * Returns: None
from tkinter import Tk, Button
root = Tk()
def on_click(event):
   print("Clicked at", event.x, event.y)
button = Button(root, text="Click Me")
EElienLib.bindEvent(button, "<Button-1>", on_click)
button.pack()
root.mainloop()

* setWindowIcon(root, icon_path)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * icon_path (str): The path to the icon file (e.g., "icon.ico", "icon.png").
   * Returns: None
from tkinter import Tk
root = Tk()
EElienLib.setWindowIcon(root, "icon.ico") # Replace
root.mainloop()

* getScreenSize(root)
   * Parameters:
      * root (Tk): A Tkinter Tk window object.
   * Returns: tuple - A tuple containing the screen width and screen height in pixels (integers).
from tkinter import Tk
root = Tk()
screen_width, screen_height = EElienLib.getScreenSize(root)
print(f"Screen size: {screen_width} x {screen_height}")
root.mainloop()

* delay(root, ms, func=None, *args)
   * Parameters:
      * root (Tk): The Tkinter Tk window object.
      * ms (int): The delay time in milliseconds.
      * func (function, optional): An optional function to be called after the delay (for non-blocking delay).
      * *args: Optional arguments to be passed to func.
   * Returns: None
from tkinter import Tk
root = Tk()
def delayed_action():
   print("Delayed action")
EElienLib.delay(root, 2000, delayed_action) # Non-blocking
print("Continuing...")
root.mainloop()

* addScrolledText(root, width=40, height=10)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * width (int, optional): The width of the text area in characters (default is 40).
      * height (int, optional): The height of the text area in lines (default is 10).
   * Returns: Text - The Tkinter Text widget.
from tkinter import Tk
root = Tk()
text_area = EElienLib.addScrolledText(root, width=50, height=15)
text_area.pack()
root.mainloop()

* insertText(scrolled_text, text)
   * Parameters:
      * scrolled_text (Text): The Tkinter Text widget.
      * text (str): The text to insert.
   * Returns: None
from tkinter import Tk
root = Tk()
text_area = EElienLib.addScrolledText(root)
text_area.pack()
EElienLib.insertText(text_area, "This is some text.\n")
root.mainloop()

* getText(scrolled_text)
   * Parameters:
      * scrolled_text (Text): The Tkinter Text widget.
   * Returns: str - The text content.
from tkinter import Tk
root = Tk()
text_area = EElienLib.addScrolledText(root)
text_area.pack()
EElienLib.insertText(text_area, "Get this text")
text = EElienLib.getText(text_area)

print(text)
root.mainloop()
```
* tagText(scrolled_text, tag_name, start, end, **kwargs)
   * Parameters:
      * scrolled_text (Text): The Tkinter Text widget.
      * tag_name (str): A unique name for the tag.
      * start (str): The starting index of the text to tag (e.g., "1.0", INSERT, END).
      * end (str): The ending index of the text to tag (e.g., "1.end").
      * **kwargs: Keyword arguments for the tag configuration (e.g., foreground="red", font=("Arial", 12, "bold")).
   * Returns: None
from tkinter import Tk
root = Tk()
text_area = EElienLib.addScrolledText(root)
text_area.pack()
EElienLib.insertText(text_area, "This is important text.")
EElienLib.tagText(text_area, "important", "8.0", "16.end", foreground="red", font=("Arial", 12, "bold"))
root.mainloop()

* addNotebook(root)
   * Parameters:
      * root (Tk): The Tkinter root window.
   * Returns: ttk.Notebook - A ttk.Notebook widget.
from tkinter import Tk
from tkinter import ttk
root = Tk()
notebook = EElienLib.addNotebook(root)
notebook.pack()
root.mainloop()

* addTab(notebook, title)
   * Parameters:
      * notebook (ttk.Notebook): A ttk.Notebook widget.
      * title (str): The title of the tab.
   * Returns: Frame - A Tkinter Frame, the tab.
from tkinter import Tk
from tkinter import ttk
root = Tk()
notebook = EElienLib.addNotebook(root)
tab1 = EElienLib.addTab(notebook, "Tab 1")
tab2 = EElienLib.addTab(notebook, "Tab 2")
notebook.pack()
root.mainloop()

* setTheme(root, theme="default")
   * Parameters:
      * root (Tk): The main Tkinter window.
      * theme (str, optional): The theme to set. "dark" or "light". Default is "default".
   * Returns: None
from tkinter import Tk
root = Tk()
EElienLib.setTheme(root, "dark")
root.mainloop()

* copyToClipboard(root, text)
   * Parameters:
      * root (Tk): The main Tkinter window.
      * text (str): The text to copy.
   * Returns: None
from tkinter import Tk
root = Tk()
EElienLib.copyToClipboard(root, "Text to copy")
root.mainloop()

* pasteFromClipboard(root)
   * Parameters:
      * root (Tk): The main Tkinter window.
   * Returns: str: The text from the clipboard.
from tkinter import Tk
root = Tk()
text = EElienLib.pasteFromClipboard(root)
print(text)
root.mainloop()

* makeDraggable(root)
   * Parameters:
      * root (Tk): The main Tkinter window.
   * Returns: None
from tkinter import Tk
root = Tk()
EElienLib.makeDraggable(root)
root.mainloop()

JSON and CSV
* displayJSON(root, json_data)
   * Parameters:
      * root: The Tkinter Tk or Toplevel window object.
      * json_data: A JSON string or a Python dictionary.
   * Returns: None
from tkinter import Tk
root = Tk()
json_data = '{"name": "John", "age": 30, "city": "New York"}'
EElienLib.displayJSON(root, json_data)
root.mainloop()
from tkinter import Tk
root = Tk()
json_data = {"name": "John", "age": 30, "city": "New York"}
EElienLib.displayJSON(root, json_data)
root.mainloop()

* displayCSV(root, csv_filepath)
   * Parameters:
      * root: The Tkinter Tk or Toplevel window object.
      * csv_filepath: The path to the CSV file (string).
   * Returns: None
from tkinter import Tk
root = Tk()
EElienLib.displayCSV(root, "data.csv") #  Create a data.csv
root.mainloop()

Charts
* createBarChart(root, data_dict, title="", x_label="", y_label="")
   * Parameters:
      * root: The Tkinter Tk or Toplevel window object.
      * data_dict: A dictionary containing the data for the chart (keys as labels, values as data).
      * title (str, optional): The title of the chart.
      * x_label (str, optional): The label for the x-axis.
      * y_label (str, optional): The label for the y-axis.
   * Returns: None
from tkinter import Tk
root = Tk()
data = {"A": 20, "B": 40, "C": 30, "D": 50}
EElienLib.createBarChart(root, data, title="Bar Chart", x_label="Categories", y_label="Values")
root.mainloop()

* createPieChart(root, data_dict, title="")
   * Parameters:
      * root: The Tkinter Tk or Toplevel window object.
      * data_dict: A dictionary containing the data for the chart (keys as labels, values as data).
      * title (str, optional): The title of the chart.
   * Returns: None
from tkinter import Tk
root = Tk()
data = {"Apples": 30, "Bananas": 20, "Oranges": 40, "Grapes": 10}
EElienLib.createPieChart(root, data, title="Pie Chart")
root.mainloop()

Web Interaction
* fetchWebpageTitle(url)
   * Parameters:
      * url (str): The URL of the webpage (string).
   * Returns: str - The title of the webpage, or an error message if the fetch fails.
title = EElienLib.fetchWebpageTitle("[https://www.google.com](https://www.google.com)")
print(title)

* getPublicIP()
   * Parameters: None
   * Returns: str - The public IP address of the machine running the script, or an error message.
ip_address = EElienLib.getPublicIP()
print(ip_address)

* openWebbrowser(url)
   * Parameters:
      * url (str): The URL to open in the web browser.
   * Returns: None
EElienLib.openWebbrowser("[https://www.python.org](https://www.python.org)")

System Interaction
* openFileExplorer(path=".")
   * Parameters:
      * path (str, optional): The path to open. Defaults to the current directory.
   * Returns: None
EElienLib.openFileExplorer() # Opens current directory
EElienLib.openFileExplorer("C:/") # Opens C: drive on Windows

Data Management
* saveDataToFile(filepath, data)
   * Parameters:
      * filepath (str): The path to the file where the data should be saved.
      * data: The data to save (can be any data type, will be converted to a string).
   * Returns: str - A message indicating success or failure.
EElienLib.saveDataToFile("mydata.txt", "This is some data")

* loadDataFromFile(filepath)
   * Parameters:
      * filepath (str): The path to the file to load data from.
   * Returns: str - The data read from the file, or None if the file does not exist or an error occurs.
data = EElienLib.loadDataFromFile("mydata.txt")
if data:
   print("Loaded data:", data)

Sound
* playSimpleSound(filepath)
   * Parameters:
      * filepath (str): The path to the sound file. Supports .wav on Windows, and uses aplay on Linux/macOS.
   * Returns: None
EElienLib.playSimpleSound("sound.wav")

Layout
* gridLayout(root, widgets, num_columns)
   * Parameters:
      * root (Tk or Toplevel): The parent Tkinter window.
      * widgets (list): A list of Tkinter widget objects.
      * num_columns (int): The number of columns in the grid layout.
   * Returns: None
from tkinter import Tk, Label, Button
root = Tk()
label1 = Label(root, text="Label 1")
button1 = Button(root, text="Button 1")
label2 = Label(root, text="Label 2")
button2 = Button(root, text="Button 2")
EElienLib.gridLayout(root, [label1, button1, label2, button2], 2)
root.mainloop()

* placeWidget(widget, x, y, anchor=NW)
   * Parameters:
      * widget (Widget): The Tkinter widget object.
      * x (int): The x-coordinate.
      * y (int): The y-coordinate.
      * anchor (str, optional): The anchor point (e.g., NW, CENTER, SE). Default is NW.
   * Returns: None
from tkinter import Tk, Label
root = Tk()
label = Label(root, text="Placed Label")
EElienLib.placeWidget(label, 50, 100, anchor="center")
label.pack()
root.mainloop()

Validation
* addValidatedTextField(root, validation_type=None, error_message="")
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * validation_type (str, optional): The type of validation ("int", "float", "email"). Default is None.
      * error_message (str, optional): The error message to display.
   * Returns: Entry: The Tkinter Entry (text field) object.
from tkinter import Tk
root = Tk()
entry = EElienLib.addValidatedTextField(root, validation_type="int", error_message="Invalid integer")
entry.pack()
root.mainloop()

Table Display
* displayTable(root, data, headers=None)
   * Parameters:
      * root (Tk or Toplevel): The Tkinter window object.
      * data (list of lists): A 2D list (rows and columns) representing the table data.
      * headers (list, optional): A list of strings representing the table headers.
   * Returns: None
from tkinter import Tk
root = Tk()
table_data = [
   ["Name", "Age", "City"],
   ["Alice", "30", "New York"],
   ["Bob", "25", "London"],
   ["Charlie", "40", "Paris"]
]
EElienLib.displayTable(root, table_data, headers=["Name", "Age", "City"])
root.mainloop()
from tkinter import Tk
root = Tk()
table_data = [
   ["Alice", "30", "New York"],
   ["Bob", "25", "London"],
   ["Charlie", "40", "Paris"]
]
EElienLib.displayTable(root, table_data)
root.mainloop()

Image Manipulation
* resizeImage(image_path, new_width, new_height, save_path=None)
   * Parameters:
      * image_path (str): Path to the image file.
      * new_width (int): The new width.
      * new_height (int): The new height.
      * save_path (str, optional): Path to save the resized image.
   * Returns: Image or None: A PIL Image object, or None on error.
from tkinter import Tk
root = Tk()
resized_image = EElienLib.resizeImage("image.jpg", 100, 100, save_path="resized_image.jpg")
if resized_image:
   print("Image resized")
root.mainloop()

* rotateImage(image_path, angle, save_path=None)
   * Parameters:
      * image_path (str): Path to the image file.
      * angle (int or float): The angle of rotation in degrees.
      * save_path (str, optional): Path to save the rotated image.
   * Returns: Image or None: A PIL Image object, or None on error.
from tkinter import Tk
root = Tk()
rotated_image = EElienLib.rotateImage("image.jpg", 90, save_path="rotated_image.jpg")
if rotated_image:
   print("Image Rotated")
root.mainloop()

* cropImage(image_path, left, top, right, bottom, save_path=None)
   * Parameters:
      * image_path (str): Path to the image file.
      * left (int): Left coordinate of the cropping rectangle.
      * top (int): Top coordinate of the cropping rectangle.
      * right (int): Right coordinate of the cropping rectangle.
      * bottom (int): Bottom coordinate of the cropping rectangle.
      * save_path (str, optional): Path to save the cropped image.
   * Returns: Image or None: A PIL Image object, or None on error.
from tkinter import Tk
root=Tk()
cropped_image = EElienLib.cropImage("image.jpg", 100, 100, 200, 200, save_path="cropped_image.jpg")
if cropped_image:
   print("Image Cropped")
root.mainloop()

* changeImageColor(image_path, color_to_replace, new_color, threshold=0, save_path=None)
   * Parameters:
      * image_path (str): Path to the image file.
      * color_to_replace (tuple): RGB tuple of the color to replace.
      * new_color (tuple): RGB tuple of the new color.
      * threshold (int, optional): Color distance threshold. Default is 0.
      * save_path (str, optional): Path to save the recolored image.
   * Returns: Image or None: A PIL Image object, or None on error.
from tkinter import Tk
root = Tk()
recolored_image = EElienLib.changeImageColor("image.jpg", (255, 0, 0), (0, 255, 0), threshold=100, save_path="recolored_image.jpg")
if recolored_image:
  print("Image recolored")
root.mainloop()

* mergeImages(image_path1, image_path2, save_path=None)
   * Parameters:
      * image_path1 (str): Path to the first image file.
      * image_path2 (str): Path to the second image file.
      * save_path (str, optional): Path to save the merged image.
   * Returns: Image or None: A PIL Image object, or None on error.
from tkinter import Tk
root = Tk()
merged_image = EElienLib.mergeImages("image1.jpg", "image2.jpg", save_path="merged_image.jpg")
if merged_image:
   print("Images Merged")
root.mainloop()

* addImageWatermark(image_path, watermark_text, position="bottomright", font_size=12, color=(255, 255, 255), save_path=None)
   * Parameters:
      * image_path (str): Path to the image file.
      * watermark_text (str): The text of the watermark.
      * position (str, optional): "topleft", "topright", "bottomleft", "bottomright", or a tuple (x, y). Default is "bottomright".
      * font_size (int, optional): Font size of the watermark text. Default is 12.
      * color (tuple, optional): RGB tuple of the text color. Default is (255,255,255) (white).
      * save_path (str, optional): Path to save the watermarked image.
   * Returns: Image or None: A PIL Image object, or None on error.
from tkinter import Tk
root = Tk()
watermarked_image = EElienLib.addImageWatermark("image.jpg", "My Watermark", position="bottomright", font_size=10, color=(0, 0, 0), save_path="watermarked_image.jpg")
if watermarked_image:
   print("Watermark added")
root.mainloop()
