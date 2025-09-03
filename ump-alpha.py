import tkinter as tk
from PIL import Image, ImageTk
import Palinka

# ------------------------------
# Funktionen für die Buttons
# ------------------------------

def play():
    selection = playlist.curselection()
    if selection:
        filename = playlist.get(selection[0])
        result = Palinka.PlaySound(filename)
        status_label.config(text=result)
    else:
        status_label.config(text="Keine Auswahl getroffen")

def pause():
    Palinka.PauseSound()
    status_label.config(text="Pausiert")

def resume():
    Palinka.ResumeSound()
    status_label.config(text="Fortgesetzt")

def stop():
    Palinka.EndSound()
    status_label.config(text="Gestoppt")

def resize_background(event=None):
    """Skaliert das Hintergrundbild auf die Fenstergröße"""
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    if new_width > 0 and new_height > 0:
        resized = bg_image.resize((new_width, new_height))
        new_bg = ImageTk.PhotoImage(resized)
        bg_label.config(image=new_bg)
        bg_label.image = new_bg

def on_close():
    Palinka.Cleanup()
    root.destroy()

# ------------------------------
# Hauptfenster
# ------------------------------

root = tk.Tk()
root.title("Untitled MP3 Player")
root.state("zoomed")  # Vollbild

# ------------------------------
# Hintergrund
# ------------------------------

bg_image = Image.open("C:/Users/admin/Python/ump-alpha/umpbg.jpeg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Ganze Fensterfläche

root.bind("<Configure>", resize_background)

# ------------------------------
# Playlist links
# ------------------------------

playlist_width = 300  # feste Breite

playlist = tk.Listbox(root, font=("Arial", 14), bg="white", fg="black", selectbackground="#B7E4B9")
playlist.place(x=0, y=0, width=playlist_width, relheight=0.8)

Palinka.MakeMediaFolder()
for file in Palinka.GetMediaFileNames():
    playlist.insert(tk.END, file)

# ------------------------------
# Buttons unten – Hintergrund auf #984138
# ------------------------------

button_frame = tk.Frame(root, bg="#984138")
button_frame.place(x=playlist_width, rely=0.85, relwidth=1, height=50)

button_play = tk.Button(button_frame, text="Play", command=play,
                        bg="#B7E4B9", fg="white", font=("Arial", 14), width=12,
                        relief="flat")
button_pause = tk.Button(button_frame, text="Pause", command=pause,
                         bg="#DABF6E", fg="white", font=("Arial", 14), width=12,
                         relief="flat")
button_resume = tk.Button(button_frame, text="Resume", command=resume,
                          bg="#6EA9DA", fg="white", font=("Arial", 14), width=12,
                          relief="flat")
button_stop = tk.Button(button_frame, text="Stop", command=stop,
                        bg="#CF7E78", fg="white", font=("Arial", 14), width=12,
                        relief="flat")

button_play.pack(side="left", padx=10, pady=5)
button_pause.pack(side="left", padx=10, pady=5)
button_resume.pack(side="left", padx=10, pady=5)
button_stop.pack(side="left", padx=10, pady=5)

# ------------------------------
# Statuszeile – Hintergrund auf #984138
# ------------------------------

status_label = tk.Label(root, text="Bereit", bg="#984138", fg="white", font=("Arial", 12))
status_label.place(x=playlist_width, rely=0.95, relwidth=1, height=25)

# ------------------------------
# FMOD initialisieren
# ------------------------------

Palinka.InitFmod()

# ------------------------------
# Event für Fenster schließen
# ------------------------------

root.protocol("WM_DELETE_WINDOW", on_close)

# ------------------------------
# GUI starten
# ------------------------------

resize_background()  # einmal initial
root.mainloop()