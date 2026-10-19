#!/usr/bin/env python3
"""
A simple digital clock using Python's built-in tkinter library.

Run:
    python clock.py

No third-party packages are required.
"""

import tkinter as tk
from time import strftime


def update_clock():
    """Update the clock display every 250 milliseconds."""
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    root.after(250, update_clock)


root = tk.Tk()
root.title("Digital Clock")
root.geometry("440x200")
root.resizable(False, False)
root.configure(bg="#101820")

time_label = tk.Label(
    root,
    font=("Consolas", 42, "bold"),
    fg="#00E5FF",
    bg="#101820",
)
time_label.pack(pady=(35, 5))

date_label = tk.Label(
    root,
    font=("Arial", 14),
    fg="#FFFFFF",
    bg="#101820",
)
date_label.pack()

update_clock()
root.mainloop()
