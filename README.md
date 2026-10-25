# Press Play

# Table of Contents
- General Info
- How It Works
- Features
- Technologies Used
- How to Run Press Play
- Development
- Room for Improvement


 # General Information
Press Play is a personalised playlist generator created in Python. It asks users a series of questions about their current mood, activity, preferred music genre and desired energy level before generating a playlist of 20 song recommendations. The project explores how Python can be used to create a simple recommendation system and an interactive graphical user interface.

With so many songs and playlists available on streaming platforms, choosing what to listen to can sometimes feel overwhelming. Press Play was designed as a simple way of narrowing down these choices based on what the user currently wants to listen to.

The user answers four questions:
  - Mood: Happy, Chill, Sad or Energetic
  - Activity: Studying, Driving, Getting Ready or Relaxing
  - Genre: Pop, R&B, Indie or Rock
  - Energy: Low, Medium or High

Press Play then compares these preferences with attributes assigned to songs in its database to generate a personalised playlist.

# How It Works
The program contains a database of 60 songs. Each song is stored as a Python dictionary containing:
  - Title
  - Artist
  - Genre
  - Mood
  - Activity
  - Energy

When the user selects their preferences, each song is given a score based on how closely it matches their answers. The scoring system is:
  - Genre match: +3 points
  - Mood match: +2 points
  - Activity match: +2 points
  - Energy match: +1 point

The songs are ranked from highest to lowest score. Randomisation is also used before ranking so that songs with equal scores can appear in a different order. The 20 highest-ranking songs are then displayed as the user's personalised Press Play playlist.

# Features
  - Interactive graphical user interface
  - Four-question music preference questionnaire
  - 60-song database
  - Weighted recommendation system
  - 20 personalised song recommendations
  - Randomisation between equally matched songs
  - Scrollable playlist results
  - Start Again function
  - Custom colours and typography

# Technologies Used
  - Python 
  - Tkinter: graphical user interface
  - Random module: playlist randomisation
  - Visual Studio Code: development environment

# How to Run Press Play
  - Make sure Python is installed on your computer.
  - Download or clone this repository.
  - Open the project in Visual Studio Code or another Python-compatible program 
  - Open the main Python file.
  - Run the program.
  - Select an answer from each of the four dropdown menus.
  - Click CREATE MY PLAYLIST.
  - Scroll through the 20 personalised song recommendations.
  - Select START AGAIN to create another playlist.

# Development
Press Play began as a simple terminal-based questionnaire before being developed into a graphical interface using Tkinter.Throughout development, different approaches to recommendation scoring, playlist size and interface design were tested and refined. The song database was gradually expanded to 60 songs, while the final recommendation output was increased to 20 songs to provide greater variety. Testing and debugging were also important throughout development, particularly when working with indentation, functions, variable scope and Tkinter widgets.

# Room for Improvement
Press Play could be developed further by adding:
  - A larger and more diverse song database
  - Album artwork
  - More genres, moods and activities
  - Additional user preference options
  - Integration with music streaming services
  - More advanced recommendation methods


  
