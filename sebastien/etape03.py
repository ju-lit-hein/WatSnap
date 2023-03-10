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
    filter_index += 1

    # The configure method allows us to change the text of a button
    # Edit the varibale that is print as the filter index
    change_filter_btn.configure(text=f"Apply filter #{filter_index % 4}")

def apply_filter(frame):
    # Apply the new filter
    if filter_index % 4 == 0:
        return frame
    elif filter_index % 4 == 1:
        new_frame = filter_one(frame)
        return new_frame 
    elif filter_index % 4 == 3:
        new_frame = filter_three(frame)
        return new_frame 
    elif filter_index % 4 == 2:
        new_frame = filter_two(frame)   
        return new_frame 
    # Continue with other filters
    return frame

def display_image(frame):
    # Convert frame to PIL image
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert PIL image to Tkinter image
    cam_out.imgtk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame1))

    # Display image
    cam_out.configure(image=cam_out.imgtk)

def get_one_frame():
    # Get one frame from webcam
    check, frame = cam.read()

    frame = apply_filter(frame)
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
cam_out = tk.Label(root)

# Use the parameter command to call a function when the button is clicked
save_btn = tk.Button(root, text = "Record",command=None)
change_filter_btn = tk.Button(root, text=f'Apply filter #{filter_index}',command=change_filter)


# Read the document to know how to display elements in the window
cam_out.pack()
save_btn.pack()
change_filter_btn.pack()

# Set the function to call when the window is displayed
root.after(100, get_one_frame)

# Read the document to know how to display your window
root.mainloop()
