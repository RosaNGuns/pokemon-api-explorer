Pokémon API Explorer

A Python command-line Pokémon information tool that uses the PokéAPI to retrieve Pokémon data and provides several ways to explore and save that information.

Features
🔎 Search for any Pokémon by name
📋 Display basic Pokémon information
⚡ View Pokémon abilities
📏 Display height and weight
🧬 View Pokémon types
⚔️ Display type strengths and weaknesses
📊 View base stats
🖼️ Download and save Pokémon sprites
🔄 Switch between Pokémon without restarting the program
❌ Handles invalid Pokémon names
What It Does

The program starts by asking the user for a Pokémon name.

It sends a request to the PokéAPI and retrieves the Pokémon's information as JSON.

Once the Pokémon has been found, the user can choose between several options:

Basic Info — Displays abilities, height, and weight.
Pokémon Type — Displays the Pokémon's types along with their strengths and weaknesses.
Pokémon Stats — Displays base HP, attack, defense, and other available stats.
Save Pokémon Sprite — Downloads the Pokémon's default sprite and organizes it into folders based on its type.
Change Pokémon — Search for a different Pokémon.
Exit — Closes the program.
Sprite Organization

Downloaded sprites are automatically organized into folders based on Pokémon type.

For example:

pokemon/
├── fire/
│   └── charizard.png
├── flying/
│   └── charizard.png
└── water/
    └── squirtle.png

This allows sprites to be automatically categorized without manually creating the folders.

Technologies Used
Python
requests
pathlib
REST API
JSON
File handling
API

This project uses PokéAPI to retrieve Pokémon data.

PokéAPI: https://pokeapi.co/

Installation

Clone the repository and install the required dependency:

pip install requests

Then run:

python Pokemon_API.py
What I Practiced

This project was created to practice working with external APIs and handling real-world JSON data in Python.

Key concepts practiced:

HTTP requests
REST APIs
JSON data parsing
Functions
Loops
Conditional logic
User input
HTTP status codes
File handling
Directory creation
Downloading files
pathlib
Basic error handling
Future Improvements

Possible improvements include:

Better input validation
More detailed Pokémon information
Support for shiny sprites
Saving additional Pokémon data
Improved type-effectiveness calculations
Configuration for the sprite download location
A graphical user interface
Project Status

🚧 Personal learning project
