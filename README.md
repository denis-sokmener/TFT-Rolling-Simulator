# 🎲 TFT Reroll (Shop Refresh) Simulator

This repository features a Python-based Teamfight Tactics (TFT) shop reroll simulator, designed to replicate the core economic mechanics of the game directly within your terminal. Built with a focus on statistical accuracy, the simulator utilizes realistic weighted probabilities to mirror high-level shop dynamics, ensuring each refresh reflects the true odds of hitting your desired champions. Users start by defining their gold pool and can execute continuous rerolls, with each action dynamically deducting the standard two-gold cost. The tool incorporates a robust game loop and comprehensive error handling via try-except blocks, preventing crashes from invalid inputs and delivering a seamless user experience. Whether you are analyzing late-game pivot odds or just simulating the tension of draining your gold for that crucial final upgrade to secure a win in an intense EUW Challenger lobby, this project serves as a practical exploration of Python logic, probability management, and solid foundational algorithmic thinking skills.

## 🚀 Features

* **Dynamic Gold Economy:** Input your starting gold pool. Every 'Reroll' action automatically deducts the standard 2 gold.
* **Weighted Probability Engine:** Champions are not drawn at random; the script utilizes percentage odds (simulating late-game shop probabilities) to accurately reflect real in-game draw chances.
* **Robust Error Handling:** Built-in `try-except` blocks ensure the simulation will not crash if invalid characters or text are entered instead of numerical values.
* **Continuous Game Loop:** A structured `while` loop keeps the application running smoothly until your gold is depleted or you choose to exit.

## 🛠️ Technologies Used

* **Language:** Python 3.x
* **Libraries:** `random` (Python built-in library for probability generation)

## 💻 How to Run

To run this simulation on your local machine, follow these steps:

1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/tft-reroll-simulator.git](https://github.com/yourusername/tft-reroll-simulator.git)
