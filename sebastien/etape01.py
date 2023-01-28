import cv2
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from time import sleep
import numpy as np
import imageio


# Init main window
root = tk.Tk()

# UI elements

# Init text value for label and button
cam_out = tk.Label(root)
save_btn = tk.Button(root)
change_filter_btn = tk.Button(root)

# Read the document to know how to display elements in the window
cam_out.pack()
save_btn.pack()
change_filter_btn.pack()


# Read the document to know how to display your window
root.mainloop()
