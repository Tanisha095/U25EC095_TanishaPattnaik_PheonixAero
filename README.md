# 🚁 Python & OpenCV — Drone Systems Programming Assignment

A collection of 20 Python programs covering core programming concepts and OpenCV image processing, themed around drone systems, mission control, and aerial operations.

---

## 📁 Repository Structure

```
├── Q01_drone_movement.py
├── Q02_weight_checker.py
├── Q03_drone_specs.py
├── Q04_telemetry_parser.py
├── Q05_flight_path_analyser.py
├── Q06_waypoint_planner.py
├── Q07_fleet_health_monitor.py
├── Q08_airspace_conflict_checker.py
├── Q09_auto_return_to_home.py
├── Q10_data_structures_justification.py
├── Q11_recursive_waypoint_distance.py
├── Q12_oops_concepts.py
├── Q13_drone_movement_coordinates.py
├── Q14_drone_authentication.py
├── Q15_vowel_counter.py
├── Q16_ascii_uppercase_converter.py
├── Q17_landing_pad_detection.py
├── Q18_red_object_tracker.py
├── Q19_aerial_grid_view.py
├── Q20_colour_detection_description.md
├── assets/
│   └── sample.jpg
├── outputs/
│   └── sahi.jpg
└── README.md
```

---

## 📋 Table of Contents

| # | Question | Topic |
|---|----------|-------|
| Q1 | Drone Movement Selector | Input / Conditionals |
| Q2 | Weight Checker | Input / Arithmetic |
| Q3 | Drone Specs Calculator | Variables / Types |
| Q4 | Telemetry Log Parser | Strings |
| Q5 | Flight Path Analyser | Lists |
| Q6 | Waypoint Mission Planner | Tuples |
| Q7 | Fleet Health Monitor | Dictionaries |
| Q8 | Airspace Conflict Checker | Sets |
| Q9 | Auto Return-to-Home System | Conditionals / Loops |
| Q10 | Data Structure Justification | Theory |
| Q11 | Recursive Waypoint Distance | Recursion |
| Q12 | OOP Concepts | Object-Oriented Programming |
| Q13 | Coordinate Movement | Input / Loops |
| Q14 | Drone Authentication | Strings |
| Q15 | Vowel Counter | Strings / Loops |
| Q16 | ASCII Uppercase Converter | ASCII / ord() / chr() |
| Q17 | Landing Pad Detection | OpenCV |
| Q18 | Red Object Tracker | OpenCV / HSV |
| Q19 | Aerial Grid View | OpenCV / Mouse Events |
| Q20 | Colour Detection Logic | OpenCV Theory |

---

## 🛠️ Requirements

### Python Version
```
Python 3.8+
```

### Libraries Required
```
opencv-python
numpy
```

### Installation
```bash
pip install opencv-python numpy
```

---

## 🚀 How to Run

Clone the repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

Run any individual question file:
```bash
python Q01_drone_movement.py
python Q17_landing_pad_detection.py
```

For OpenCV questions (Q17, Q18, Q19), make sure `sample.jpg` is placed inside the `assets/` folder before running.

---

## 📌 Question Summaries

### Q1 — Drone Movement Selector
Takes a number input (1, 2, or 3) and prints the corresponding drone movement — Roll, Pitch, or Yaw — with a description of motor behavior.

### Q2 — Weight Checker
Accepts drone body weight and payload weight, calculates total, and checks if it exceeds 2 kg.

### Q3 — Drone Specs Calculator
Uses predefined drone specifications to calculate maximum payload, print variable types, check if a 1.8 kg camera can be carried, and convert weight to grams.

### Q4 — Telemetry Log Parser
Parses a raw telemetry string to extract drone ID, altitude, speed, battery, GPS coordinates, and status. Formats and prints a clean summary.

### Q5 — Flight Path Analyser
Analyses an altitude list to find max altitude, average, climb rates, steepest climb and descent, and a trimmed flight path without zero entries.

### Q6 — Waypoint Mission Planner
Works with a tuple of waypoints to print details, find highest altitude, check membership, and demonstrate tuple immutability with proper error handling.

### Q7 — Fleet Health Monitor
Manages a dictionary-based drone fleet — adds, removes, filters, and updates drone records based on battery and altitude conditions.

### Q8 — Airspace Conflict Checker
Uses Python sets to find restricted zones, safe zones, symmetric differences, subsets, and unique zone counts across three zone sets.

### Q9 — Auto Return-to-Home System
Checks multiple RTH trigger conditions independently and simulates a descent loop from current altitude to ground with battery drain at each step.

### Q10 — Data Structure Justification
Written explanation (200–300 words) justifying the use of list, tuple, and set for three different drone data storage scenarios.

### Q11 — Recursive Waypoint Distance Calculator
Two pure recursive functions — one calculates total path distance across all waypoints, another finds the longest single leg in the journey.

### Q12 — OOP Concepts
Covers all four pillars of Object-Oriented Programming — Encapsulation, Abstraction, Inheritance, and Polymorphism — with Python code examples.

### Q13 — Coordinate Movement Simulator
Takes starting coordinates and movement direction (horizontal/vertical) and prints updated coordinates at each step of the movement.

### Q14 — Drone Authentication
Takes user ID and password, converts to lowercase, and compares against predefined credentials to authenticate the drone connection.

### Q15 — Vowel Counter
Accepts a string input, prints it, and counts the total number of vowels present.

### Q16 — ASCII Uppercase Converter
Converts a lowercase character to uppercase using only `ord()` and `chr()` functions, without any built-in string methods.

### Q17 — Landing Pad Detection (OpenCV)
Detects a white rectangular landing pad on a dark background from a drone camera image and saves the result as `sahi.jpg`.

### Q18 — Red Object Tracker (OpenCV)
Simulates a drone camera tracking a red object in live video using HSV color filtering. Draws a circle around the detected object and displays status text.

### Q19 — Aerial Grid View (OpenCV)
Opens an image, overlays an 8x8 grid, and highlights any grid cell the user clicks on with blue color, displaying its grid coordinates.

### Q20 — Colour Detection Logic
A short written description and flowchart explaining the step-by-step logic behind color detection using OpenCV and HSV masking.

---

## 🧠 Key Concepts Covered

- Python fundamentals — data types, loops, conditionals, functions
- String manipulation and f-strings
- Lists, tuples, sets, and dictionaries
- Recursion
- Object-Oriented Programming (OOP)
- OpenCV — image reading, color spaces, masking, contour detection
- HSV color filtering and mouse callback events

---

## 👤 Author

**Tanisha Pattnaik**
- GitHub: [@Tanisha095](https://github.com/Tanisha095)

---

## 📅 Submission Details

- **Course:** Drone Programming / Python & OpenCV
- **Deadline:** 30th June, 8:00 PM
- **Submission:** PDF with screenshots + GitHub repository link
