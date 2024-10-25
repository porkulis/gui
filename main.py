import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()

root.geometry("600x400")
root.title("Auto Combo 2000")

frame_buttons = ttk.Frame()
frame_buttons.pack()

frame_output = ttk.Frame()
frame_output.pack()

rectangle_1 = ttk.Label(frame_buttons, text="Rectangle 1", background="green")
rectangle_1.pack(fill="x",ipadx=10, ipady=10)

rectangle_1 = ttk.Label(frame_buttons, text="Rectangle 2", background="red")
rectangle_1.pack(fill="x", ipadx=10, ipady=10)

output = ScrolledText(frame_output, state="disabled")
output.pack(fill="both", expand=True)

def display_message():
    message="test message"
    output.config(state="normal")
    output.insert(tk.END, message + "\n")
    output.config(state="disabled")
    output.see(tk.END)

message = ttk.Button(frame_buttons, command=display_message, text="Display Message")
message.pack(fill="x", ipadx=10, ipady=10)

root.mainloop()