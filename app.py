import tkinter as tk
from tkinter import messagebox

# Main Window
window = tk.Tk()
window.title("Speech and Facial Emotion Detection using VR and ML")
window.geometry("1000x700")
window.configure(bg="#EAF4FC")

# ---------------- Title ----------------
title = tk.Label(
    window,
    text="Speech and Facial Emotion Detection using VR and Machine Learning",
    font=("Arial", 20, "bold"),
    fg="darkblue",
    bg="#EAF4FC"
)
title.pack(pady=20)

subtitle = tk.Label(
    window,
    text="MCA Final Year Project",
    font=("Arial",14),
    bg="#EAF4FC"
)
subtitle.pack()

# ---------------- Functions ----------------

def facial():

    face_window = tk.Toplevel(window)
    face_window.title("Facial Emotion Detection")
    face_window.geometry("500x400")
    face_window.configure(bg="#F5F9FF")

    tk.Label(
        face_window,
        text="Facial Emotion Detection",
        font=("Arial",18,"bold"),
        bg="#F5F9FF",
        fg="darkblue"
    ).pack(pady=20)

    tk.Button(
        face_window,
        text="📷 Upload Image",
        font=("Arial",14),
        width=20,
        command=lambda: messagebox.showinfo(
            "Upload",
            "Upload Image Module Coming Next"
        )
    ).pack(pady=15)

    tk.Button(
        face_window,
        text="🎥 Live Webcam",
        font=("Arial",14),
        width=20,
        command=lambda: messagebox.showinfo(
            "Webcam",
            "Live Webcam Module Coming Next"
        )
    ).pack(pady=15)

    tk.Button(
        face_window,
        text="⬅ Back",
        font=("Arial",12),
        command=face_window.destroy
    ).pack(pady=30)
def speech():
    messagebox.showinfo("Speech Emotion",
                        "Speech Emotion Detection Module")

def fusion():
    messagebox.showinfo("Fusion",
                        "Speech + Facial Emotion Fusion")

def tutorial():
    messagebox.showinfo("Tutorial",
                        "Tutorial Video Coming Soon!")

# ---------------- Buttons ----------------

tk.Button(
    window,
    text="😊 Facial Emotion Detection",
    font=("Arial",15),
    width=30,
    command=facial
).pack(pady=15)

tk.Button(
    window,
    text="🎤 Speech Emotion Detection",
    font=("Arial",15),
    width=30,
    command=speech
).pack(pady=15)

tk.Button(
    window,
    text="🔄 Emotion Fusion",
    font=("Arial",15),
    width=30,
    command=fusion
).pack(pady=15)

tk.Button(
    window,
    text="📹 Tutorial",
    font=("Arial",15),
    width=30,
    command=tutorial
).pack(pady=15)

tk.Button(
    window,
    text="Exit",
    font=("Arial",15),
    width=20,
    bg="red",
    fg="white",
    command=window.destroy
).pack(pady=30)

window.mainloop()