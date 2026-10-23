import tkinter as tk
import random
from tkinter import Scrollbar, font

song1 = {
    "title": "Espresso",
    "artist": "Sabrina Carpenter",
    "genre": "pop",
    "mood": "happy",
    "activity": "getting ready",
    "energy": "high"
}

song2 = {
    "title": "Pink + White",
    "artist": "Frank Ocean",
    "genre": "r&b",
    "mood": "chill",
    "activity": "relaxing",
    "energy": "low"
}

song3 = {
    "title": "Ribs",
    "artist": "Lorde",
    "genre": "indie",
    "mood": "sad",
    "activity": "driving",
    "energy": "medium"
}

song4 = {
    "title": "good 4 u",
    "artist": "Olivia Rodrigo",
    "genre": "rock",
    "mood": "energetic",
    "activity": "getting ready",
    "energy": "high"
}

song5 = {
    "title": "Sweater Weather",
    "artist": "The Neighbourhood",
    "genre": "indie",
    "mood": "chill",
    "activity": "studying",
    "energy": "medium"
}

song6 = {
    "title": "Cruel Summer",
    "artist": "Taylor Swift",
    "genre": "pop",
    "mood": "energetic",
    "activity": "driving",
    "energy": "high"
}

song7 = {
    "title": "Birds of a Feather",
    "artist": "Billie Eilish",
    "genre": "pop",
    "mood": "chill",
    "activity": "relaxing",
    "energy": "medium"
}

song8 = {
    "title": "Nights",
    "artist": "Frank Ocean",
    "genre": "r&b",
    "mood": "sad",
    "activity": "driving",
    "energy": "medium"
}

song9 = {
    "title": "Good Days",
    "artist": "SZA",
    "genre": "r&b",
    "mood": "chill",
    "activity": "relaxing",
    "energy": "low"
}

song10 = {
    "title": "Snooze",
    "artist": "SZA",
    "genre": "r&b",
    "mood": "happy",
    "activity": "relaxing",
    "energy": "low"
}

song11 = {
    "title": "The Less I Know the Better",
    "artist": "Tame Impala",
    "genre": "indie",
    "mood": "chill",
    "activity": "driving",
    "energy": "medium"
}

song12 = {
    "title": "Somebody Else",
    "artist": "The 1975",
    "genre": "indie",
    "mood": "sad",
    "activity": "relaxing",
    "energy": "low"
}

song13 = {
    "title": "Electric Feel",
    "artist": "MGMT",
    "genre": "indie",
    "mood": "happy",
    "activity": "getting ready",
    "energy": "high"
}

song14 = {
    "title": "Misery Business",
    "artist": "Paramore",
    "genre": "rock",
    "mood": "energetic",
    "activity": "getting ready",
    "energy": "high"
}

song15 = {
    "title": "Mr. Brightside",
    "artist": "The Killers",
    "genre": "rock",
    "mood": "energetic",
    "activity": "driving",
    "energy": "high"
}

song16 = {
    "title": "505",
    "artist": "Arctic Monkeys",
    "genre": "rock",
    "mood": "sad",
    "activity": "driving",
    "energy": "medium"
}

song17 = {
    "title": "Style",
    "artist": "Taylor Swift",
    "genre": "pop",
    "mood": "happy",
    "activity": "driving",
    "energy": "high"
}

song18 = {
    "title": "Ocean Eyes",
    "artist": "Billie Eilish",
    "genre": "pop",
    "mood": "sad",
    "activity": "studying",
    "energy": "low"
}

song19 = {
    "title": "See You Again",
    "artist": "Tyler, The Creator",
    "genre": "r&b",
    "mood": "happy",
    "activity": "studying",
    "energy": "medium"
}

song20 = {
    "title": "Space Song",
    "artist": "Beach House",
    "genre": "indie",
    "mood": "chill",
    "activity": "studying",
    "energy": "low"
}

song21 = {
    "title": "Levitating",
    "artist": "Dua Lipa",
    "genre": "pop",
    "mood": "happy",
    "activity": "getting ready",
    "energy": "high"
}

song22 = {
    "title": "cardigan",
    "artist": "Taylor Swift",
    "genre": "pop",
    "mood": "sad",
    "activity": "relaxing",
    "energy": "low"
}

song23 = {
    "title": "Golden",
    "artist": "Harry Styles",
    "genre": "pop",
    "mood": "happy",
    "activity": "driving",
    "energy": "medium"
}

song24 = {
    "title": "CHIHIRO",
    "artist": "Billie Eilish",
    "genre": "pop",
    "mood": "chill",
    "activity": "studying",
    "energy": "low"
}

song25 = {
    "title": "Green Light",
    "artist": "Lorde",
    "genre": "pop",
    "mood": "energetic",
    "activity": "getting ready",
    "energy": "high"
}

song26 = {
    "title": "Kill Bill",
    "artist": "SZA",
    "genre": "r&b",
    "mood": "sad",
    "activity": "driving",
    "energy": "medium"
}

song27 = {
    "title": "Best Part",
    "artist": "Daniel Caesar",
    "genre": "r&b",
    "mood": "chill",
    "activity": "relaxing",
    "energy": "low"
}

song28 = {
    "title": "Super Rich Kids",
    "artist": "Frank Ocean",
    "genre": "r&b",
    "mood": "chill",
    "activity": "driving",
    "energy": "medium"
}

song29 = {
    "title": "Saturn",
    "artist": "SZA",
    "genre": "r&b",
    "mood": "chill",
    "activity": "studying",
    "energy": "low"
}

song30 = {
    "title": "Redbone",
    "artist": "Childish Gambino",
    "genre": "r&b",
    "mood": "chill",
    "activity": "relaxing",
    "energy": "medium"
}

song31 = {
    "title": "Dog Days Are Over",
    "artist": "Florence + The Machine",
    "genre": "indie",
    "mood": "happy",
    "activity": "driving",
    "energy": "high"
}

song32 = {
    "title": "My Kind of Woman",
    "artist": "Mac DeMarco",
    "genre": "indie",
    "mood": "chill",
    "activity": "relaxing",
    "energy": "low"
}

song33 = {
    "title": "The Adults Are Talking",
    "artist": "The Strokes",
    "genre": "indie",
    "mood": "chill",
    "activity": "driving",
    "energy": "medium"
}

song34 = {
    "title": "Motion Sickness",
    "artist": "Phoebe Bridgers",
    "genre": "indie",
    "mood": "sad",
    "activity": "driving",
    "energy": "medium"
}

song35 = {
    "title": "Lisztomania",
    "artist": "Phoenix",
    "genre": "indie",
    "mood": "energetic",
    "activity": "getting ready",
    "energy": "high"
}

song36 = {
    "title": "Don't Look Back in Anger",
    "artist": "Oasis",
    "genre": "rock",
    "mood": "happy",
    "activity": "driving",
    "energy": "high"
}

song37 = {
    "title": "Do I Wanna Know?",
    "artist": "Arctic Monkeys",
    "genre": "rock",
    "mood": "chill",
    "activity": "driving",
    "energy": "medium"
}

song38 = {
    "title": "Dreams",
    "artist": "Fleetwood Mac",
    "genre": "rock",
    "mood": "chill",
    "activity": "relaxing",
    "energy": "medium"
}

song39 = {
    "title": "Everlong",
    "artist": "Foo Fighters",
    "genre": "rock",
    "mood": "energetic",
    "activity": "driving",
    "energy": "high"
}

song40 = {
    "title": "Iris",
    "artist": "Goo Goo Dolls",
    "genre": "rock",
    "mood": "sad",
    "activity": "relaxing",
    "energy": "medium"
}

song41 = {
    "title": "HOT TO GO!",
    "artist": "Chappell Roan",
    "genre": "pop",
    "mood": "energetic",
    "activity": "getting ready",
    "energy": "high"
}

song42 = {
    "title": "Supercut",
    "artist": "Lorde",
    "genre": "pop",
    "mood": "happy",
    "activity": "driving",
    "energy": "high"
}

song43 = {
    "title": "Liability",
    "artist": "Lorde",
    "genre": "pop",
    "mood": "sad",
    "activity": "relaxing",
    "energy": "low"
}

song44 = {
    "title": "After The Storm",
    "artist": "Kali Uchis",
    "genre": "r&b",
    "mood": "happy",
    "activity": "relaxing",
    "energy": "medium"
}

song45 = {
    "title": "Japanese Denim",
    "artist": "Daniel Caesar",
    "genre": "r&b",
    "mood": "chill",
    "activity": "studying",
    "energy": "low"
}

song46 = {
    "title": "Dark Red",
    "artist": "Steve Lacy",
    "genre": "r&b",
    "mood": "sad",
    "activity": "studying",
    "energy": "medium"
}

song47 = {
    "title": "Tongue Tied",
    "artist": "Grouplove",
    "genre": "indie",
    "mood": "happy",
    "activity": "getting ready",
    "energy": "high"
}

song48 = {
    "title": "Apocalypse",
    "artist": "Cigarettes After Sex",
    "genre": "indie",
    "mood": "sad",
    "activity": "studying",
    "energy": "low"
}

song49 = {
    "title": "Dream On",
    "artist": "Aerosmith",
    "genre": "rock",
    "mood": "sad",
    "activity": "driving",
    "energy": "medium"
}

song50 = {
    "title": "Are You Gonna Be My Girl",
    "artist": "Jet",
    "genre": "rock",
    "mood": "energetic",
    "activity": "getting ready",
    "energy": "high"
}

song51 = {
    "title": "Pink Pony Club",
    "artist": "Chappell Roan",
    "genre": "pop",
    "mood": "happy",
    "activity": "getting ready",
    "energy": "high"
}

song52 = {
    "title": "Lovers Rock",
    "artist": "TV Girl",
    "genre": "indie",
    "mood": "chill",
    "activity": "relaxing",
    "energy": "low"
}

song53 = {
    "title": "No One Noticed",
    "artist": "The Marías",
    "genre": "indie",
    "mood": "sad",
    "activity": "relaxing",
    "energy": "low"
}

song54 = {
    "title": "Good Luck, Babe!",
    "artist": "Chappell Roan",
    "genre": "pop",
    "mood": "energetic",
    "activity": "getting ready",
    "energy": "high"
}

song55 = {
    "title": "Love Galore",
    "artist": "SZA",
    "genre": "r&b",
    "mood": "chill",
    "activity": "driving",
    "energy": "medium"
}

song56 = {
    "title": "Sofia",
    "artist": "Clairo",
    "genre": "indie",
    "mood": "happy",
    "activity": "driving",
    "energy": "medium"
}

song57 = {
    "title": "Still Into You",
    "artist": "Paramore",
    "genre": "rock",
    "mood": "happy",
    "activity": "getting ready",
    "energy": "high"
}

song58 = {
    "title": "I Wanna Be Yours",
    "artist": "Arctic Monkeys",
    "genre": "rock",
    "mood": "chill",
    "activity": "relaxing",
    "energy": "low"
}

song59 = {
    "title": "Wildflower",
    "artist": "Billie Eilish",
    "genre": "pop",
    "mood": "sad",
    "activity": "relaxing",
    "energy": "low"
}

song60 = {
    "title": "Borderline",
    "artist": "Tame Impala",
    "genre": "indie",
    "mood": "chill",
    "activity": "driving",
    "energy": "medium"
}

songs = [
    song1, song2, song3, song4, song5,
    song6, song7, song8, song9, song10,
    song11, song12, song13, song14, song15,
    song16, song17, song18, song19, song20,
    song21, song22, song23, song24, song25,
    song26, song27, song28, song29, song30,
    song31, song32, song33, song34, song35,
    song36, song37, song38, song39, song40,
    song41, song42, song43, song44, song45,
    song46, song47, song48, song49, song50,
    song51, song52, song53, song54, song55,
    song56, song57, song58, song59, song60
]

window = tk.Tk()
window.title("Press Play")
window.geometry("500x800")
window.configure(bg="#F5F3F0")
title = tk.Label(
    window,
    text="PRESS PLAY",
    font=("Gill Sans", 28, "bold"),
    bg="#F5F3F0",
    fg="#41AB58"
)
title.pack(pady=(30, 5))

subtitle = tk.Label(
    window,
    text="Your playlist, matched to you",
    font=("Avenir Next", 13, "bold"),
    bg="#F5F3F0",
    fg="#D674B2",
)
subtitle.pack(pady=(0, 25))

# Mood question
mood_label = tk.Label(
    window,
    text="WHAT MOOD ARE YOU IN?",
    font=("Avenir Next", 12, "bold"),
    bg="#F5F3F0"
)
mood_label.pack(pady=(10, 5))

mood_options = ["Happy", "Chill", "Sad", "Energetic"]

mood_var = tk.StringVar()
mood_var.set("Select a mood")

mood_menu = tk.OptionMenu(
    window,
    mood_var,
    *mood_options
)
mood_menu.config(
    width=20,
    font=("Arial", 11),
    relief="flat",
    highlightthickness=0
)
mood_menu.pack(pady=(0, 15))

# Activity question
activity_label = tk.Label(
    window,
    text="WHAT ARE YOU DOING?",
    font=("Avenir Next", 12, "bold"),
    bg="#F5F3F0"
)
activity_label.pack(pady=(10, 5))

activity_options = ["Studying", "Driving", "Getting Ready", "Relaxing"]

activity_var = tk.StringVar()
activity_var.set("Select an activity")

activity_menu = tk.OptionMenu(
    window,
    activity_var,
    *activity_options
)
activity_menu.config(
    width=20,
    font=("Avenir Next", 11),
    relief="flat",
    highlightthickness=0
)
activity_menu.pack(pady=(0, 15))


# Genre question
genre_label = tk.Label(
    window,
    text="WHAT GENRE DO YOU WANT TO LISTEN TO?",
    font=("Avenir Next", 12, "bold"),
    bg="#F5F3F0"
)
genre_label.pack(pady=(10, 5))

genre_options = ["Pop", "R&B", "Indie", "Rock"]

genre_var = tk.StringVar()
genre_var.set("Select a genre")

genre_menu = tk.OptionMenu(
    window,
    genre_var,
    *genre_options
)
genre_menu.config(
    width=20,
    font=("Avenir Next", 11),
    relief="flat",
    highlightthickness=0
)
genre_menu.pack(pady=(0, 15))


# Energy question
energy_label = tk.Label(
    window,
    text="WHAT ENERGY LEVEL DO YOU WANT?",
    font=("Avenir Next", 12, "bold"),
    bg="#F5F3F0"
)
energy_label.pack(pady=(10, 5))

energy_options = ["Low", "Medium", "High"]

energy_var = tk.StringVar()
energy_var.set("Select an energy level")

energy_menu = tk.OptionMenu(
    window,
    energy_var,
    *energy_options
)
energy_menu.config(
    width=20,
    font=("Avenir Next", 11),
    relief="flat",
    highlightthickness=0
)
energy_menu.pack(pady=(0, 15))

def start_again(questionnaire_widgets):

    # Remove the results page
    for widget in window.winfo_children():
        widget.pack_forget()

    # Show the original questionnaire again
    for widget in questionnaire_widgets:
        widget.pack()

def create_playlist():

    # Get the user's choices from the dropdown menus
    mood = mood_var.get().lower()
    activity = activity_var.get().lower()
    genre = genre_var.get().lower()
    energy = energy_var.get().lower()

    # Create an empty list for the ranked songs
    ranked_songs = []

    # Check every song in the dataset
    for song in songs:

        # Every song starts with a score of 0
        score = 0

        # Mood match = 2 points
        if song["mood"] == mood:
            score = score + 2

        # Activity match = 2 points
        if song["activity"] == activity:
            score = score + 2

        # Genre match = 3 points
        if song["genre"] == genre:
            score = score + 3

        # Energy match = 1 point
        if song["energy"] == energy:
            score = score + 1

        # Save the score to the song
        song["score"] = score

        # Add the song to the ranked list
        ranked_songs.append(song)

    # Randomise songs first so equal-scoring songs
    # can appear in a different order
    random.shuffle(ranked_songs)

    # Sort songs from highest score to lowest score
    ranked_songs.sort(
        key=lambda song: song["score"],
        reverse=True
    )

     # Save the questionnaire widgets before hiding them
    questionnaire_widgets = window.winfo_children()

    # Hide the questionnaire
    for widget in questionnaire_widgets:
        widget.pack_forget()

    # Create the results page title
    results_title = tk.Label(
        window,
        text="YOUR PRESS PLAY",
        font=("Gill Sans", 28, "bold"),
        bg="#F5F3F0",
        fg="#41AB58"
    )

    results_title.pack(pady=(40, 5))

    # Create the results page subtitle
    results_subtitle = tk.Label(
        window,
        text="Your playlist, matched to you.",
        font=("Avenir Next", 14),
        bg="#F5F3F0",
        fg="#D674B2"
    )

    playlist_text = ""

    for number, song in enumerate(ranked_songs[:20], start=1):
        playlist_text += (
            f"{number:02}   {song['title']} — {song['artist']}\n\n"
        )

# Create a frame for the playlist
    playlist_frame = tk.Frame(window)
    playlist_frame.pack(pady=10)

    # Create scrollable playlist box
    playlist_box = tk.Text(
    playlist_frame,
    width=42,
    height=25,
    font=("Avenir Next", 12),
    bg="#F6F4F2",
    fg="black",
    borderwidth=0,
    highlightthickness=0,
    padx=20,
    pady=10,
    wrap="word"
)

    playlist_box.pack(side="left")
    # Add scrollbar
    scrollbar = tk.Scrollbar(
        playlist_frame,
        command=playlist_box.yview
    )

    scrollbar.pack(side="right", fill="y")

    playlist_box.config(yscrollcommand=scrollbar.set)

    playlist_box.insert("1.0", playlist_text)

    playlist_box.config(state="disabled")

    Start_again_button = tk.Button(
        window,
        text="START AGAIN",
        font=("Avenir Next", 10, "bold"),
        bg="#D674B2",
        fg="#D674b2",
        activebackground="#D674B2",
        activeforeground="#D674B2",
        relief="flat",
        borderwidth=0,
        padx=25,
        pady=8,
        cursor="hand2",
        command=lambda: start_again(questionnaire_widgets)
        ) 
    Start_again_button.pack(pady=20)

def start_again(questionnaire_widgets):
    # Close the current program window
    window.destroy()

    # Start the program again
    import os
    import sys
    os.execl(sys.executable, sys.executable, *sys.argv)

create_button = tk.Button(
window,
text="♪ CREATE MY PLAYLIST ♪",
font=("Avenir Next", 12, "bold"),
bg="#D674B2",
fg="#41AB58",
activebackground="#D674B2",
activeforeground="#41AB58",
relief="flat",
borderwidth=0,
padx=30,
pady=12,
cursor="hand2",
command=create_playlist
)
create_button.pack(pady=25)

window.mainloop()