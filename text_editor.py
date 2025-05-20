from tkinter import filedialog
from tkinter import messagebox

def save_file(text_widget, root):
    """
    Save the text in the Text widget to a file.
    :param text_widget: The Tkinter Text widget containing the text
    :param root: The Tkinter root window
    """
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        with open(file, "w") as f:
            text = text_widget.get(1.0, "end-1c")  # Get all text in the widget
            f.write(text)
        messagebox.showinfo("Save File", "File saved successfully!")

def open_file(text_widget):
    """
    Open a text file and display its content in the Text widget.
    :param text_widget: The Tkinter Text widget to display the file contents
    """
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file:
        with open(file, "r") as f:
            text = f.read()
            text_widget.delete(1.0, "end")  # Clear current content
            text_widget.insert("insert", text)
