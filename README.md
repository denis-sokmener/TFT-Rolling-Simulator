# TFT-Rolling-Simulator
This repository features a Python-based Teamfight Tactics (TFT) shop reroll simulator, designed to replicate the core economic mechanics of the game directly within your terminal.

# TFT Reroll (Shop Refresh) Simulator

This project is a Python-based terminal application designed to faithfully simulate the shop reroll mechanics from Teamfight Tactics (TFT). It allows users to manage a virtual gold economy and execute shop refreshes, drawing random champion tiers (1-Cost to 5-Cost) based on realistic, weighted probability distributions.

## Features

* **Dynamic Gold Economy:** Input your starting gold pool. Every 'Reroll' action automatically deducts the standard 2 gold.
* **Weighted Probability Engine:** Champions are not drawn at random; the script utilizes percentage odds (simulating late-game shop probabilities) to accurately reflect real in-game draw chances.
* **Robust Error Handling:** Built-in `try-except` blocks ensure the simulation will not crash if invalid characters or text are entered instead of numerical values.
* **Continuous Game Loop:** A structured `while` loop keeps the application running smoothly until your gold is depleted or you choose to exit.

## Technologies Used

* **Language:** Python 3.x
* **Libraries:** `random` (Python built-in library for probability generation)

## How to Run

To run this simulation on your local machine, follow these steps:

1. Clone this repository:
   
   git clone [https://github.com/yourusername/tft-reroll-simulator.git](https://github.com/yourusername/tft-reroll-simulator.git)
   
2. Navigate to the project directory and execute the script:

python test.py

(Note: Ensure Python is installed on your system and added to your environment variables/PATH).

Example Terminal Output

Enter your gold amount: 40

Your gold: 40. Press R to reroll, press Q to quit.

Your choice: R

['2', '3', '4', '1', '2']

Your gold: 38. Press R to reroll, press Q to quit.

Your choice: R

['3', '4', '1', '2', '2']

Your gold: 36. Press R to reroll, press Q to quit.

Your choice: Q

Game over. Your remaining gold: 36

Development Focus

This project was built to practice core programming fundamentals, specifically:

Controlling program flow using while loops and nested if/elif statements.

Managing state variables (gold tracking) across iterations.

Implementing probability-based selections using random.choices.

Sanitizing user inputs with try-except blocks for better application stability.

