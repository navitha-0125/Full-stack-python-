import tkinter as tk

def button_click():
    label.config(text="Move Here!")
    
window = tk.Tk()
window.title("android")

label = tk.Label(window, text="Hello, samsung!")
label.pack(pady=40)

button = tk.Button(window, text="Click", command=button_click)
button.pack()

window.mainloop()