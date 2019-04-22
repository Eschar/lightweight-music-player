#!/usr/bin/env python3
print("Importing pygame multimedia library...")
import pygame
print("Importing sys and subprocess libraries...")
import subprocess, sys
state = {"mode":"main"}

def get_song_filenames():
    return os.listdir(os.path.join(os.path.dirname(__file__), "music"))

def get_mdir_path():
    return os.path.join(os.path.dirname(__file__), "music")

if not os.path.isdir(os.path.join(os.path.dirname(__file__), "music")):
    print("No music directory entry found. Empty directory created.")
    os.makedirs(os.path.join(os.path.dirname(__file__), "music"))

while True:
    if state["mode"] == "main":
        command = input("[O]pen a piece\n[L]ist pieces\n[E]xit\n> ")
        if command.strip().lower() in ["o", "open"]:
            state = {"mode":"select_song"}
        elif command.strip().lower() in ["l", "list"]:
            song_filenames = get_song_filenames()
            if len(song_filenames) > 0:
                print("Music:")
                for song_filename in song_filenames:
                    print(song_filename)
            else:
                print("You have no music.")
        elif command.strip().lower() in ["e", "exit"]:
            sys.exit()
        else:
            print("Please enter 'o,' 'l' or 'e.'")

    elif state["mode"] == "select_song":
        if len(get_song_filenames()) > 0:
            print("Songs:")
            for song_choice in enumerate(get_song_filenames()):
                print(str(song_choice[0]) + ": " + song_choice[1])
            song_number = int(input("Enter song number: "))
            if song_number in [song_choice[0] for song_choice in enumerate(get_song_filenames())]:
                pygame.init()
                pygame.mixer.init()
                display = pygame.display.set_mode([800, 1])
                song = pygame.mixer.music.load(os.path.join(get_mdir_path(), list(enumerate(get_song_filenames()))[song_number][1]))
                pygame.display.set_caption(list(enumerate(get_song_filenames()))[song_number][1])
                pygame.event.clear()
                pygame.mixer.music.play()
                state = {"mode":"playing_song", "song_filename":list(enumerate(get_song_filenames()))[song_number][1], "playing":True}
            else:
                print("No song has that number.")
        else:
            print("You have no music.")
            state = {"mode":"main"}

    elif state["mode"] == "playing_song":
        command = input("Now playing: "+state["song_filename"]+"\nAvailable commands: pause, play, restart, close\n>")
        if command.strip().lower() == "pause":
            pygame.mixer.music.pause()

        elif command.strip().lower() == "play":
            pygame.mixer.music.unpause()

        elif command.strip().lower() == "restart":
            pygame.mixer.music.rewind()
        elif command.strip().lower() == "close":
            pygame.quit()
            state = {"mode" :"main"}
