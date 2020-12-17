from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('Erkin gramofoni')
root.geometry("500x300")

pygame.mixer.init()

#Add song
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    song = song.replace("C:/Users/pikku/Projects/python_project/audio/", "")
    song = song.replace(".mp3", "")
    song_box.insert(END, song)

song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)

# Add many songs
def add_many_song():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

    for song in songs:
        song = song.replace("C:/Users/pikku/Projects/python_project/audio/", "")
        song = song.replace(".mp3", "")
        song_box.insert(END, song)

#Play song
def play():
    song = song_box.get(ACTIVE)
    song = f'C:/Users/pikku/Projects/python_project/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)  

#Stop current play
def stop():
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)

global paused
paused = False

# Pause/Unpause play
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True
    
# Next song
def next_song():
    next_one = song_box.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)
    
    song = f'C:/Users/pikku/Projects/python_project/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)

# Play previous song
def prev_song():
    prev_one = song_box.curselection()
    prev_one = prev_one[0]-1
    song = song_box.get(prev_one)
    
    song = f'C:/Users/pikku/Projects/python_project/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)
    song_box.activate(prev_one)
    song_box.selection_set(prev_one, last=None)

# Delete single
def delete_single():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

# Delete All
def delete_multiple():
    song_box.delete(0, END)
    pygame.mixer.music.stop()

# Define control button images
back_btn_img = PhotoImage(file='gui/rewind.png')
play_btn_img = PhotoImage(file='gui/play.png')
pause_btn_img = PhotoImage(file='gui/pause.png')
next_btn_img = PhotoImage(file='gui/forward.png')
stop_btn_img = PhotoImage(file='gui/stop.png')

# Create control frame
controls_frame = Frame(root)
controls_frame.pack()

# Control buttons
back_btn = Button(controls_frame, image=back_btn_img, borderwidth=0, command=prev_song)
play_btn = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_btn = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
next_btn = Button(controls_frame, image=next_btn_img, borderwidth=0, command=next_song)
stop_btn = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_btn.grid(row=0, column=0, padx=10)
play_btn.grid(row=0, column=1, padx=10)
pause_btn.grid(row=0, column=2, padx=10)
next_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add a song
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add", menu=add_song_menu)
add_song_menu.add_command(label="Add One", command=add_song)
# Add multiple
add_song_menu.add_command(label="Add Multiple", command=add_many_song)
# Delete song
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove", menu=remove_song_menu)
remove_song_menu.add_command(label="Remove Singular", command=delete_single)
remove_song_menu.add_command(label="Remove All", command=delete_multiple)

root.mainloop()
