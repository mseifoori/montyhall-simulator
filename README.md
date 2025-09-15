# Monty Hall Problem Simulator 🚪🐐🚗

A simple simulation and visualization of the famous Monty Hall Problem, built with Python and Streamlit.

This project helps illustrate the probability paradox by simulating the problem multiple times: Is it better to switch doors or stay with your first choice?

## 📚 What is the Monty Hall Problem?

The Monty Hall Problem is a probability puzzle based on a game show scenario:

A player picks one of three doors. Behind one is a car, behind the other two are goats.

The host (Monty), who knows what's behind the doors, opens one of the remaining two doors—revealing a goat.

The player is given a choice: stick with their original door or switch to the other unopened door.

What's the best strategy?

Statistically, switching gives a 66.6% chance of winning the car, while not switching gives only 33.3%.

## 🔍 Features
- ✅ Simulates the Monty Hall game up to 100,000 times!
- ✅ Visulazing winning percentage data on flexible charts.
- ✅ Compares the effectiveness of switching vs. staying.

## 🛠 Project Structure
```
MontyHall_Simulator/
│
├── src/
│   ├── app.py
│   └── main.py
└── README.md
```

## 🚀 How to Run

1. Install dependencies:

```Bash
pip install -r requirements.txt
```

2. Run the app

To run the app, you have to be in the src file:
```Bash
streamlit run app.py
```

## 📄 License
This project is open-source and free to use under the MIT License.
