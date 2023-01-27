import cv2
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from time import sleep
import numpy as np
import imageio

filter_index = 0

def display_image(frame):
    # Convert frame to PIL image
    frame = PIL.Image.fromarray(frame)

    # Convert PIL image to Tkinter image
    cam_out.imgtk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))

    # Display image
    cam_out.configure(image=cam_out.imgtk)

def get_one_frame():
    # Get one frame from webcam
    check, frame = cam.read()

    # Use functions to display frame
    ...

    # Call this function again in 100ms to get the next frame
    ...

# Init main window
root = tk.Tk()

# UI elements

# This is your camera
cam = cv2.VideoCapture(0)

# Init text value for label and button
cam_out = tk.Label(root, text="Webcam Video")
save_btn = tk.Button(root, text = "Record")
change_filter_btn = tk.Button(root, text=f'Apply filter #{filter_index}')


# Read the document to know how to display elements in the window
cam_out.pack()
save_btn.pack()
change_filter_btn.pack()

root.after(100, get_one_frame)

# Read the document to know how to display your window
root.mainloop()
