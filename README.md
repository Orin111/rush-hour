# Rush Hour Game

Welcome to the Rush Hour game! In this classic puzzle game, your goal is to move cars on the game board to clear a path for the red car to exit the grid. The game challenges your logical thinking and strategic planning.

## Table of Contents

- [Game Description](#game-description)
- [Getting Started](#getting-started)
- [Car Class](#car-class)
- [Board Class](#board-class)
- [Game Class](#game-class)
- [Running the Game](#running-the-game)
- [License](#license)
- [Author](#author)

## Game Description

This Rush Hour game is a digital adaptation of the classic sliding block puzzle. You'll be presented with a game board containing cars of various sizes, orientations, and colors. The challenge is to slide the cars horizontally or vertically to create an unobstructed path for the red car to exit the grid.

## Getting Started

To play the Rush Hour game on your local machine, follow these steps:

1. Clone this repository using the command: `git clone <repository_url>`
2. Navigate to the project directory: `cd rush-hour-game`
3. Create a virtual environment (optional but recommended): `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install required libraries: `pip install -r requirements.txt`
6. Run the game: `python3 game.py car_config.json`

Replace `<repository_url>` with the actual URL of your GitHub repository.

## Car Class

The `Car` class represents a car on the game board. Each car has attributes such as its name, length, location, and orientation. You can create, move, and manipulate cars using this class.

For detailed information about the `Car` class, its methods, and usage examples, refer to the [Car Class](#car-class) section in this README.

## Board Class

The `Board` class represents the game board itself. It provides methods to create the board, add cars, check for legal moves, and more. The interaction with the `Board` class is crucial for playing the Rush Hour game.

For detailed information about the `Board` class, its methods, and usage examples, refer to the [Board Class](#board-class) section in this README.

## Game Class

The `Game` class orchestrates the Rush Hour game by managing player turns, processing inputs, and checking for game completion. It utilizes the `Board` class and the `Car` class to create a functional and interactive game experience.

For detailed information about the `Game` class, its methods, and usage examples, refer to the [Game Class](#game-class) section in this README.

## Running the Game

To play the Rush Hour game, follow these steps after setting up the project:

1. Run the game script: `python3 game.py car_config.json`
2. Follow the prompts to input car color and movement direction.
3. Try to move the cars strategically to create a path for the red car to exit.
4. Enter `!` to end the game whenever you want.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it according to the terms of the license.

## Author

This README was written by Orin Pour. If you have any questions or feedback, feel free to reach out!

---

Feel free to explore the provided code, adapt it to your needs, and have fun playing and solving puzzles in the Rush Hour game! If you have any questions about the project, code, or usage, don't hesitate to ask.
