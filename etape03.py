import cv2
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from time import sleep
import numpy as np
import imageio

filter_index = 0
anim_frames_max = 24
anim_frames = []
anim_frames_count = 0
save = False

def filter_one(frame):
    return cv2.filter2D(frame, -1, np.array([[-1, -1, -1, -1, -1], [-1, 1, 2, 1, -1], [-1, 2, 4, 2, -1], [-1, 1, 2, 1, -1], [-1, -1, -1, -1, -1]]))

def filter_two(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    return cv2.Laplacian(gray, cv2.CV_8U, gray, ksize = 15)

def filter_three(frame):
    B, G, R = cv2.split(frame)
    M = np.maximum(np.maximum(B, G), R)
    R[R < M] = 0
    B[B < M] = 0
    G[G < M] = 0
    return cv2.merge([R, G, B])

def change_filter():
    global filter_index
    # Increment filter index
    ...

    # Edit button text
    change_filter_btn.configure(text=f"")

def apply_filter(frame):
    # Apply the new filter
    if filter_index % 4 == 0:
        return frame
    elif filter_index % 4 == 1:
        new_frame = filter_one(frame)
    # Continue with other filters
    ...

    return frame

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
    display_image(frame)

    # Call this function again in 100ms to get the next frame
    root.after(100, get_one_frame)

# Init main window
root = tk.Tk()

# UI elements

# This is your camera
cam = cv2.VideoCapture(0)

# Init text value for label and button
cam_out = tk.Label(root, text="Webcam Video")

# Use the parameter coomancd to call a function when the button is clicked
save_btn = tk.Button(root, text = "Record")
change_filter_btn = tk.Button(root, text=f'Apply filter #{filter_index}')


# Read the document to know how to display elements in the window
cam_out.pack()
save_btn.pack()
change_filter_btn.pack()

# Set the function to call when the window is displayed
root.after(100, get_one_frame)

# Read the document to know how to display your window
root.mainloop()
