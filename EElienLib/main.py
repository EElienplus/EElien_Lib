from tkinter import *
from tkinter import colorchooser, filedialog, messagebox
from tkinter import ttk  # For Combobox and Notebook
from PIL import Image, ImageTk, ImageFilter
import random
import json
import csv
import webbrowser
import socket
import os
import winsound  # For simple sound on Windows (platform-dependent!)
import threading
import time
import math # For pie chart
import subprocess # For Linux/macOS sound
import requests
from bs4 import BeautifulSoup

print("Thanks for using my lib!")

def add(num1, num2):
    return int(num1) + int(num2)

def subtract(num1, num2):
    return int(num1) - int(num2)

def multiply(num1, num2):
    return int(num1) * int(num2)

def divide(num1, num2):
    return int(num1) / int(num2)

def helloWorld():
    print("Hello, World")

def createWindow(width, height, bcgColor, title):
    root = Tk()
    root.title(title)
    root.geometry(f"{width}x{height}")
    root.configure(background=bcgColor)
    return root

def addWindowText(root, text):
    lbl = Label(root, text=text)
    lbl.pack()

def addButton(root, text, command=None):
    btn = Button(root, text=text, command=command)
    btn.pack()
    return btn

def addRadioButton(root, text, variable, value):
    radio = Radiobutton(root, text=text, variable=variable, value=value)
    radio.pack()
    return radio

def addCheckButton(root, text, variable):
    check = Checkbutton(root, text=text, variable=variable)
    check.pack()
    return check

def getColor(root):
    color_code = colorchooser.askcolor(title="Choose color")
    return color_code

def addTextField(root):
    entry = Entry(root)
    entry.pack()
    return entry

def getTextFieldText(textField):
    return textField.get()

def addImage(root, image_path):
    try:
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
        img_label = Label(root, image=photo)
        img_label.image = photo
        img_label.pack()
        return img_label
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        return None

def addListener(widget, action=None):
    if isinstance(widget, Button) and callable(action):
        widget.config(command=action)
    elif isinstance(widget, (Radiobutton, Checkbutton)):
        if callable(action):
            widget.config(command=action)

def clearWindow(root):
    for widget in root.winfo_children():
        widget.destroy()

def enableMovement(root, img_label, movementSpeed):
    def moveUp(Scene):
        img_label.place(x=img_label.winfo_x(), y=img_label.winfo_y()-movementSpeed)
    def moveDown(Scene):
        img_label.place(x=img_label.winfo_x(), y=img_label.winfo_y()+movementSpeed)
    def moveRight(Scene):
        img_label.place(x=img_label.winfo_x()+movementSpeed, y=img_label.winfo_y())
    def moveLeft(Scene):
        img_label.place(x=img_label.winfo_x()-movementSpeed, y=img_label.winfo_y())

    root.bind("<w>", moveUp)
    root.bind("<a>", moveLeft)
    root.bind("<s>", moveDown)
    root.bind("<d>", moveRight)

def addDropdown(root, values, variable):
    combo = ttk.Combobox(root, textvariable=variable, values=values)
    combo.pack()
    return combo

def getDropdownValue(dropdown):
    return dropdown.get()

def addListbox(root, values, selectmode=SINGLE):
    listbox = Listbox(root, selectmode=selectmode)
    for item in values:
        listbox.insert(END, item)
    listbox.pack()
    return listbox

def getListboxSelection(listbox):
    selected_indices = listbox.curselection()
    return [listbox.get(i) for i in selected_indices]

def addScale(root, from_, to, variable, label=""):
    scale = Scale(root, from_=from_, to=to, variable=variable, label=label, orient=HORIZONTAL)
    scale.pack()
    return scale

def getScaleValue(scale):
    return scale.get()

def addProgressBar(root, max_value):
    progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate', maximum=max_value)
    progressbar.pack()
    return progressbar

def updateProgressBar(progressbar, value):
    progressbar['value'] = value

def showInfoDialog(title, message):
    messagebox.showinfo(title, message)

def showErrorDialog(title, message):
    messagebox.showerror(title, message)

def askYesNoDialog(title, message):
    return messagebox.askyesno(title, message)

def openFileDialog():
    filepath = filedialog.askopenfilename()
    return filepath

def saveFileDialog():
    filepath = filedialog.asksaveasfilename()
    return filepath

def createFrame(root, bd=2, relief=SUNKEN):
    frame = Frame(root, bd=bd, relief=relief)
    frame.pack(padx=5, pady=5)
    return frame

def packWidgets(widgets, **kwargs):
    for widget in widgets:
        widget.pack(**kwargs)

def gridWidgets(widgets, rows, cols, **kwargs):
    index = 0
    for r in range(rows):
        for c in range(cols):
            if index < len(widgets):
                widgets[index].grid(row=r, column=c, **kwargs)
                index += 1

def bindEvent(widget, event, action):
    widget.bind(event, action)

def setWindowIcon(root, icon_path):
    try:
        root.iconbitmap(icon_path) # For .ico files (Windows)
    except TclError:
        try:
            img = PhotoImage(file=icon_path) # For other formats (Linux, macOS)
            root.tk.call('wm', 'iconphoto', root._w, img)
        except TclError as e:
            print(f"Error setting icon: {e}")

def getScreenSize(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return screen_width, screen_height

def delay(root, ms, func=None, *args):
    if func:
        root.after(ms, func, *args)
    else:
        time.sleep(ms / 1000) # Blocking delay if no function

def addScrolledText(root, width=40, height=10):
    text_area = Text(root, width=width, height=height, wrap=WORD)
    scrollbar = Scrollbar(root, command=text_area.yview)
    text_area.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_area.pack(side=LEFT, fill=BOTH, expand=True)
    return text_area

def insertText(scrolled_text, text):
    scrolled_text.insert(END, text)

def getText(scrolled_text):
    return scrolled_text.get("1.0", END)

def tagText(scrolled_text, tag_name, start, end, **kwargs):
    scrolled_text.tag_configure(tag_name, **kwargs)
    scrolled_text.tag_add(tag_name, start, end)

def addNotebook(root):
    notebook = ttk.Notebook(root)
    notebook.pack(fill=BOTH, expand=True)
    return notebook

def addTab(notebook, title):
    tab = Frame(notebook)
    notebook.add(tab, text=title)
    return tab

def setTheme(root, theme="default"):
    if theme == "dark":
        root.config(bg="gray15")
        for widget in root.winfo_children():
            widget.config(bg="gray30", fg="white")
            if isinstance(widget, Entry) or isinstance(widget, Text) or isinstance(widget, Listbox) or isinstance(widget, ttk.Combobox):
                widget.config(bg="gray20", fg="white", insertbackground="white")
            if isinstance(widget, Frame):
                widget.config(bg="gray15")
    elif theme == "light":
        root.config(bg="SystemButtonFace")
        for widget in root.winfo_children():
            widget.config(bg="SystemButtonFace", fg="SystemWindowText")
            if isinstance(widget, Entry) or isinstance(widget, Text) or isinstance(widget, Listbox) or isinstance(widget, ttk.Combobox):
                widget.config(bg="white", fg="black", insertbackground="black")
            if isinstance(widget, Frame):
                widget.config(bg="SystemButtonFace")

def copyToClipboard(root, text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

def pasteFromClipboard(root):
    return root.clipboard_get()

def makeDraggable(root):
    def move_window(event):
        root.geometry(f'+{event.x_root - root.offsetx}+{event.y_root - root.offsety}')

    def save_last_pos(event):
        root.offsetx = event.x
        root.offsety = event.y

    root.bind('<Button-1>', save_last_pos)
    root.bind('<B1-Motion>', move_window)

def displayJSON(root, json_data):
    text_area = Text(root, wrap=WORD)
    text_area.pack(fill=BOTH, expand=True)
    try:
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data
        formatted_json = json.dumps(data, indent=4)
        text_area.insert(END, formatted_json)
    except json.JSONDecodeError as e:
        text_area.insert(END, f"Error decoding JSON: {e}")
    except TypeError as e:
        text_area.insert(END, f"Invalid JSON data type: {e}")

def displayCSV(root, csv_filepath):
    try:
        with open(csv_filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row_text = ", ".join(row)
                addWindowText(root, row_text)
    except FileNotFoundError:
        addWindowText(root, f"Error: CSV file not found at {csv_filepath}")
    except Exception as e:
        addWindowText(root, f"Error reading CSV file: {e}")

def createBarChart(root, data_dict, title="", x_label="", y_label=""):
    canvas = Canvas(root, bg="white")
    canvas.pack(fill=BOTH, expand=True, padx=10, pady=10)

    max_value = max(data_dict.values()) if data_dict else 1
    width = 600
    height = 400
    x_padding = 50
    y_padding = 50
    bar_width = 40
    spacing = 20

    canvas.create_text(width / 2, 20, text=title, font=("Arial", 16))
    canvas.create_text(width / 2, height - 10, text=x_label)
    canvas.create_text(20, height / 2, text=y_label, angle=90)

    x = x_padding + spacing / 2
    for label, value in data_dict.items():
        bar_height = (value / max_value) * (height - 2 * y_padding)
        y1 = height - y_padding
        y2 = y1 - bar_height
        canvas.create_rectangle(x, y1, x + bar_width, y2, fill="steelblue")
        canvas.create_text(x + bar_width / 2, y1 + 10, text=label, anchor=N)
        canvas.create_text(x + bar_width / 2, y2 - 10, text=str(value), anchor=S)
        x += bar_width + spacing

def createPieChart(root, data_dict, title=""):
    canvas = Canvas(root, bg="white", width=400, height=400)
    canvas.pack(padx=10, pady=10)

    total = sum(data_dict.values())
    start_angle = 0
    center_x = 200
    center_y = 200
    radius = 150
    colors = ["red", "green", "blue", "yellow", "orange", "purple"]
    color_index = 0

    canvas.create_text(center_x, 20, text=title, font=("Arial", 16))

    for label, value in data_dict.items():
        fraction = value / total
        extent = 360 * fraction
        canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                          start=start_angle, extent=extent, fill=colors[color_index % len(colors)], outline="black")
        angle_mid = start_angle + extent / 2
        x_text = center_x + (radius + 20) * math.cos(math.radians(angle_mid))
        y_text = center_y + (radius + 20) * math.sin(math.radians(angle_mid))
        canvas.create_text(x_text, y_text, text=f"{label} ({value})", anchor="w" if x_text < center_x else "e")
        start_angle += extent
        color_index += 1

def fetchWebpageTitle(url):
    try:
        import requests
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.title
        return title_tag.string.strip() if title_tag else "No Title Found"
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"
    except ImportError:
        return "Error: 'requests' and 'beautifulsoup4' libraries are needed. Please install them."

def getPublicIP():
    try:
        response = requests.get("https://httpbin.org/ip", timeout=5)
        response.raise_for_status()
        return response.json()['origin']
    except requests.exceptions.RequestException as e:
        return f"Error getting IP: {e}"
    except ImportError:
        return "Error: 'requests' library is needed. Please install it."

def openFileExplorer(path="."):
    try:
        os.startfile(path) # For Windows
    except AttributeError:
        try:
            subprocess.Popen(['xdg-open', path]) # For Linux
        except FileNotFoundError:
            try:
                subprocess.Popen(['open', path]) # For macOS
            except FileNotFoundError:
                return "Error: Could not open file explorer."
    except Exception as e:
        return f"Error opening file explorer: {e}"

def openWebbrowser(url):
    webbrowser.open_new_tab(url)

def createDraggableWindow(root):
    def move_window(event):
        root.geometry(f'+{event.x_root - root.offsetx}+{event.y_root - root.offsety}')
    def save_last_pos(event):
        root.offsetx = event.x
        root.offsety = event.y
    root.bind('<Button-1>', save_last_pos)
    root.bind('<B1-Motion>', move_window)

def saveDataToFile(filepath, data):
    try:
        with open(filepath, 'w') as f:
            f.write(str(data))
        return f"Data saved to {filepath}"
    except Exception as e:
        return f"Error saving data: {e}"

def loadDataFromFile(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        return f"Error loading data: {e}"

def playSimpleSound(filepath):
    try:
        if os.name == 'nt': # Windows
            winsound.PlaySound(filepath, winsound.SND_FILENAME)
        elif os.name == 'posix': # Linux or macOS
            subprocess.Popen(['aplay', filepath]) # Requires 'aplay' to be installed
        else:
            print("Sound playback is not supported on this platform by this function.")
    except FileNotFoundError:
        print(f"Error: Sound file not found at {filepath}")
    except Exception as e:
        print(f"Error playing sound: {e}")

def gridLayout(root, widgets, num_columns):
    row = 0
    col = 0
    for index, widget in enumerate(widgets):
        widget.grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col >= num_columns:
            col = 0
            row += 1

def placeWidget(widget, x, y, anchor=NW):
    widget.place(x=x, y=y, anchor=anchor)

def addValidatedTextField(root, validation_type=None, error_message=""):
    entry = Entry(root)
    error_label = Label(root, text="", fg="red")
    error_label.pack()

    def validate_input(event):
        text = entry.get()
        is_valid = True
        if validation_type == "int":
            if not text.isdigit() and text != "":
                is_valid = False
        elif validation_type == "float":
            try:
                float(text)
            except ValueError:
                is_valid = False
        elif validation_type == "email":
            # Simple email validation (can be improved)
            if "@" not in text or "." not in text:
                is_valid = False

        if is_valid:
            error_label.config(text="")
        else:
            error_label.config(text=error_message)
        return True # Return True to allow input

    entry.pack()
    entry.bind("<KeyRelease>", validate_input)
    return entry

def displayTable(root, data, headers=None):
    if headers:
        for col, header in enumerate(headers):
            lbl = Label(root, text=header, font=("Arial", 10, "bold"), bd=1, relief=SUNKEN)
            lbl.grid(row=0, column=col, padx=5, pady=5)
        start_row = 1
    else:
        start_row = 0

    for row_idx, row_data in enumerate(data):
        for col_idx, cell_data in enumerate(row_data):
            lbl = Label(root, text=cell_data, bd=1, relief=SUNKEN)
            lbl.grid(row=start_row + row_idx, column=col_idx, padx=5, pady=5)

def resizeImage(image_path, new_width, new_height, save_path=None):
    try:
        img = Image.open(image_path)
        resized_img = img.resize((new_width, new_height))
        if save_path:
            resized_img.save(save_path)
        return resized_img
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        return None

def rotateImage(image_path, angle, save_path=None):
    try:
        img = Image.open(image_path)
        rotated_img = img.rotate(angle)
        if save_path:
            rotated_img.save(save_path)
        return rotated_img
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        return None

def applyImageFilter(image_path, filter_type, save_path=None):
    try:
        img = Image.open(image_path)
        applied_filter = None
        if filter_type == "blur":
            applied_filter = img.filter(ImageFilter.BLUR)
        elif filter_type == "sharpen":
            applied_filter = img.filter(ImageFilter.SHARPEN)
        elif filter_type == "grayscale":
            applied_filter = img.convert("L")
        elif filter_type == "contour":
            applied_filter = img.filter(ImageFilter.CONTOUR)
        elif filter_type == "edge_enhance":
            applied_filter = img.filter(ImageFilter.EDGE_ENHANCE)
        elif filter_type == "emboss":
            applied_filter = img.filter(ImageFilter.EMBOSS)
        elif filter_type == "find_edges":
            applied_filter = img.filter(ImageFilter.FIND_EDGES)
        elif filter_type == "detail":
            applied_filter = img.filter(ImageFilter.DETAIL)
        elif filter_type == "smooth":
            applied_filter = img.filter(ImageFilter.SMOOTH)
        else:
            print(f"Error: Unknown filter type '{filter_type}'")
            return None

        if applied_filter:
            if save_path:
                applied_filter.save(save_path)
            return applied_filter
        return None
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        return None

def displayAnimatedGIF(root, gif_path):
    try:
        img = Image.open(gif_path)
        frames = []
        try:
            while True:
                frames.append(ImageTk.PhotoImage(img.copy()))
                img.seek(img.tell() + 1)
        except EOFError:
            pass

        if not frames:
            print(f"Error: No frames found in GIF: {gif_path}")
            return

        current_frame = 0
        label = Label(root, image=frames[0])
        label.pack()

        def update_gif(ind):
            frame = frames[ind % len(frames)]
            label.config(image=frame)
            root.after(50, update_gif, ind + 1) # Adjust delay as needed

        root.after(0, update_gif, 0)
    except FileNotFoundError:
        print(f"Error: GIF not found at {gif_path}")
    except Exception as e:
        print(f"Error displaying GIF: {e}")

def runInBackground(target_function, *args):
    thread = threading.Thread(target=target_function, args=args)
    thread.start()
    return thread

def saveAppState(filepath, data_dict):
    try:
        with open(filepath, 'w') as f:
            json.dump(data_dict, f)
        return f"Application state saved to {filepath}"
    except Exception as e:
        return f"Error saving application state: {e}"

def loadAppState(filepath):
    try:
        with open(filepath, 'r') as f:
            data = f.read()
            if data:
                return json.loads(data)
            else:
                return None  # File is empty
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return "Error: Invalid JSON format in state file."
    except Exception as e:
        return f"Error loading application state: {e}"

def askForText(root, title, prompt):
    dialog = Toplevel(root)
    dialog.title(title)
    Label(dialog, text=prompt).pack(padx=10, pady=10)
    entry = Entry(dialog)
    entry.pack(padx=10, pady=5)
    result = StringVar()
    def on_ok():
        result.set(entry.get())
        dialog.destroy()
    Button(dialog, text="OK", command=on_ok).pack(pady=5)
    dialog.wait_window()
    return result.get()

def askForNumber(root, title, prompt):
    text_result = askForText(root, title, prompt)
    try:
        return int(text_result)
    except ValueError:
        try:
            return float(text_result)
        except ValueError:
            messagebox.showerror(root, "Error", "Invalid number entered.")
            return None
def chooseFromList(root, title, prompt, options):
    dialog = Toplevel(root)
    dialog.title(title)
    Label(dialog, text=prompt).pack(padx=10, pady=10)
    listbox = Listbox(dialog, selectmode=SINGLE)
    for option in options:
        listbox.insert(END, option)
    listbox.pack(padx=10, pady=5)
    selected_item = StringVar()
    def on_select():
        selected_indices = listbox.curselection()
        if selected_indices:
            selected_item.set(listbox.get(selected_indices[0]))
        dialog.destroy()
    Button(dialog, text="Select", command=on_select).pack(pady=5)
    dialog.wait_window()
    return selected_item.get()