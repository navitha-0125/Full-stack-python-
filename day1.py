import tkinter as tk

def button_click():
    label.config(text="Button Clicked!")

window = tk.Tk()
window.title("snapshort")

label = tk.Label(window, text="Hello, tkinter!")
label.pack(pady=20)

button = tk.Button(window, text="Click me ", command=button_click)
button.pack()

window.mainloop()