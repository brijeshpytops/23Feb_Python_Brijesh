import tkinter as tk
from tkinter import font
import os
import pygame


screen = tk.Tk()

screen.title("Top10 Musics")

screen.geometry('400x500')

icon_path = r'images\logo.ico'

screen.iconbitmap(icon_path)

# Initialize Pygame mixer for audio playback
pygame.mixer.init()

# Create a custom font with a cursive style for the in-window title
cursive_font = font.Font(family="Comic Sans MS", size=20, slant="italic")

# Create a Label widget to act as a styled title within the window
title_label = tk.Label(screen, text="My musics", fg="red", font=cursive_font)
title_label.pack(pady=10)

musics = os.listdir('musics')

listbox = tk.Listbox(screen)  
  
  
for index, music in enumerate(musics):
    listbox.insert(index+1,f"{music}")

def play_music():
    selected_music = listbox.get(tk.ANCHOR)  # Get the selected music from the Listbox
    if selected_music:
        music_path = os.path.join('musics', selected_music)
        pygame.mixer.music.load(music_path)  # Load the selected music file
        pygame.mixer.music.play()            # Play the selected music file

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()  # Pause the currently playing music

def unpause_music():
    pygame.mixer.music.unpause()  # Unpause the music

listbox.pack()  

# Button to play the selected music
play_button = tk.Button(screen, text="Play Music", command=play_music)
play_button.pack(pady=10)

# Button to stop the music
stop_button = tk.Button(screen, text="Stop Music", command=stop_music)
stop_button.pack(pady=10)

# Button to pause the music
pause_button = tk.Button(screen, text="Pause Music", command=pause_music)
pause_button.pack(pady=10)

# Button to unpause the music
unpause_button = tk.Button(screen, text="Unpause Music", command=unpause_music)
unpause_button.pack(pady=10)


screen.mainloop()