import cv2
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from time import sleep
import numpy as np
import imageio

# Init default value by reading the pdf
filter_index = ...
anim_frames_max = 24
anim_frames = []
anim_frames_count = ...
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
    change_filter_btn.configure(text=f'Apply filter #{filter_index % 4}')

def apply_filter(frame):
    if filter_index % 4 == 0:
        return frame
    elif filter_index % 4 == 1:
        new_frame = filter_one(frame)
    # continue with other filters
    ...
    return new_frame

def save_anim():
    global save

    # Save animation
    if (save == False):
        # Set save flag to True
        ...
        save_btn.configure(text = "Recording... 0 %", state = "disabled")


def get_one_frame():
    global save
    global anim_frames
    global anim_frames_count

    # Get one frame from webcam
    check, frame = cam.read()

    # Apply filter on frame:
    frame2 = apply_filter(frame)

    # Save frame into array
    if (save == True and anim_frames_count < anim_frames_max):
        # Add frame to array and increment counter
        ...
        percentage = int(anim_frames_count / anim_frames_max * 100)
        # Write percentage into button
        save_btn.configure(text=f'Recording: {...} %', state = "disabled")

    # Save array of frames into animated GIF format
    if (save == True and anim_frames_count == anim_frames_max):
        save_btn.configure(text=f'Saving!', state = "disabled")
        imageio.mimsave('animation.gif', anim_frames, 'GIF', duration=0.1)
        # Reset variables
        ...
        save_btn.configure(text = "Record", state = "normal")

    # Convert frame from BGR to RGB for display in UI
    frame3 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    cam_out.imgtk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame3))
    cam_out.configure(image = cam_out.imgtk)

    # Update main window after 100ms
    root.after(100, get_one_frame)


# Init main window
root = tk.Tk()

# Init webcam capture
cam = cv2.VideoCapture(0)

# UI elements
cam_out = tk.Label(root)
save_btn = tk.Button(root, text = "Record", command=save_anim)
# Use old code to complete this button
change_filter_btn = tk.Button(..., text=f'Apply filter #{... % 4}', command = ...)

# Display tk elements
cam_out.pack()
...

# Update main window after 100ms
root.after(..., get_one_frame)

root.mainloop()
