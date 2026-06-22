**🎲 TFT Reroll (Shop Refresh) Simulator**
This repository features a Python-based Teamfight Tactics (TFT) shop reroll simulator, designed to replicate the core economic mechanics of the game directly within your terminal. Built with a focus on statistical accuracy, the simulator utilizes realistic weighted probabilities to mirror high-level shop dynamics, ensuring each refresh reflects the true odds of hitting your desired champions.
Users start by defining their gold pool and can execute continuous rerolls, with each action dynamically deducting the standard two-gold cost. The tool incorporates a robust game loop and comprehensive error handling via try-except blocks, preventing crashes from invalid inputs and delivering a seamless user experience. Whether you are analyzing late-game pivot odds or just simulating the tension of draining your gold for that crucial final upgrade, this project serves as a practical exploration of Python logic, probability management, and solid foundational algorithmic thinking skills.

**🚀 Features**

Dynamic Gold Economy: Input your starting gold pool. Every reroll automatically deducts the standard 2 gold.

Weighted Probability Engine: Champions are drawn using percentage odds that simulate real in-game probabilities.

Robust Error Handling: Built-in try-except blocks prevent crashes from invalid inputs.

Continuous Game Loop: A while loop keeps the simulation running until your gold is depleted or you choose to exit.


**🛠️ Technologies Used**

Language: Python 3.x

Libraries: random (built-in)


**💻 How to Run**

1. Clone this repository:

```bash
git clone https://github.com/denis-sokener/tft-reroll-simulator.git
```


2. Navigate to the project directory and execute the script:

```bash
cd tft-reroll-simulator
python test.py
```

**🎲 Example Terminal Output**

```bash
Enter your gold amount: 40
Your gold: 40. Press R to reroll, press Q to quit.
Your choice: R
['2', '3', '4', '1', '2']
```

## 🔮 Future Features (Roadmap)

Here are some planned enhancements and features to elevate the simulation's complexity and analytical value:

- Level-Based Probability Scaling: Dynamically adjust pool percentages based on a user-defined player level (e.g., Level 7 vs. Level 8 rolling odds).
- Shop Pool Depletion (Bench Tracking): Simulate a shared champion pool where buying or holding specific units reduces their probability in subsequent rolls.
- Data Logging & Analytics: Export session roll data to a CSV/JSON format for statistical analysis, tracking average gold spent to hit specific tier units.
- Graphical User Interface (GUI): Transition the simulation from a terminal interface to a clean UI web application using frameworks like Streamlit or Tkinter.
