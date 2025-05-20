import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password
from text_editor import save_file, open_file

# Password Generator Function
def generate_password_gui(root, text_widget):  # Accept text_widget as an argument
    def on_generate_button_click():
        length = int(length_entry.get())
        use_special_chars = special_chars_var.get()
        password = generate_password(length, use_special_chars)
        password_label.config(text=f"Generated Password: {password}")
        
        # Insert password into the text editor
        if text_widget:
            text_widget.insert(tk.END, f"\nGenerated Password: {password}\n")

    password_window = tk.Toplevel(root)
    password_window.title("Password Generator")

    tk.Label(password_window, text="Password Length:").pack(pady=10)
    length_entry = tk.Entry(password_window)
    length_entry.insert(0, "12")
    length_entry.pack(pady=5)

    special_chars_var = tk.BooleanVar()
    tk.Checkbutton(password_window, text="Include Special Characters", variable=special_chars_var).pack()

    generate_button = tk.Button(password_window, text="Generate Password", command=on_generate_button_click)
    generate_button.pack(pady=10)

    password_label = tk.Label(password_window, text="Generated Password: ")
    password_label.pack(pady=5)

# Main Text Editor
def create_text_editor_gui():
    root = tk.Tk()
    root.title("Text Editor")

    # Create Text widget
    text_widget = tk.Text(root, wrap="word", width=100, height=30)
    text_widget.pack(padx=10, pady=10)

    # Menu Bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=lambda: open_file(text_widget))
    file_menu.add_command(label="Save", command=lambda: save_file(text_widget, root))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # Add Password Generator to Menu
    menu_bar.add_command(label="Password Generator", command=lambda: generate_password_gui(root, text_widget))  # Pass text_widget here

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    create_text_editor_gui()
