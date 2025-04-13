
# 🤖 Humanoid Robot OOP Project

## 📌 Overview
This project is a Python-based **Object-Oriented (OOP) system** simulating a humanoid robot. The system enables the robot to:
- **Move** forward and backward
- **Pick up and drop** objects
- **Monitor and recharge** its battery
- **Log and undo** tasks
- **Shutdown** safely

The robot operates via a command-line interface (CLI), supports task management through various data structures (list, stack, queue), and ensures modularity using OOP principles.

---

## ✅ Features
- ✔ **Modular OOP design** using Python classes  
- ✔ **Battery level monitoring** with auto-recharge functionality  
- ✔ **Pick-up and drop operations** with object holding state  
- ✔ **Undo feature** using LIFO logic  
- ✔ **CLI interface** for live simulation  
- ✔ **Task logging** with support for history  
- ✔ **Obstacle simulation** during movement  
- ✔ **Test suite** with `assert`-based validation of features  

---

## 🚀 Setup Instructions

### 1️⃣ Prerequisites
Ensure you have **Python 3.12 or higher** installed:
```bash
python --version
```

### 2️⃣ Clone This Repository
```bash
git clone https://github.com/mobeen-ali/Humanoid_Robot_OOP_Project.git
cd Humanoid_Robot_OOP_Project
```

### 3️⃣ Run the Simulation
```bash
python main.py
```

### 4️⃣ Run Automated Tests
```bash
python test_robot.py
```

---

## Commentary on Development & Design

This project was developed as part of the System Implementation module, with the goal of simulating a basic humanoid robot’s functionality using object-oriented principles and data structure integration. The system builds upon prior design work (Unit 7) which involved the creation of UML diagrams—class, activity, sequence, and state transition—defining the logical flow and component interactions of the robot.

### Design Philosophy & OOP

A modular, scalable architecture was prioritized. The system is built around the `Robot` class, which encapsulates the robot's core functionalities and coordinates with other classes:
- `Battery`: Manages power levels and charging cycles
- `Environment`: Simulates obstacle detection
- `TaskManager`: Manages logging, undoing, and task queueing

These classes showcase encapsulation and single responsibility, making the codebase easier to maintain and extend. For example, all energy-related logic is handled within `Battery`, ensuring separation of concerns.

Polymorphism and inheritance were considered for future scalability, e.g., if different robot types with unique movement logic were to be introduced. While not explicitly implemented in this version, the code is structured to support such extensions.

### Data Structures Used

- **List**: Used to maintain a chronological log of tasks (`task_log`), supporting history review.
- **Stack (LIFO)**: Implemented as `task_stack` to support the "Undo Last Task" feature.
- **Queue (FIFO)**: Simulated with Python’s `deque` to ensure tasks are processed in the order they were received.

Each structure was chosen for its operational advantages—stacks for reversing the most recent task, queues for orderly execution, and lists for easy iteration through task history.

### Testing and Validation

A separate test suite `test_robot.py` was written as per assignment requirements. Using Python’s `assert` statements, this script validates:
- Movement
- Battery drain and recharge
- Pick-up and drop behavior
- Shutdown status
- Undo functionality
- Log accuracy

These tests serve both as evidence of testing and a basic form of regression checks should the code be expanded in the future.

### Challenges and Decisions

One key challenge was designing the task management in a way that supports logging, undoing, and sequential execution without overcomplicating the architecture. To solve this, three parallel structures were implemented. Another challenge was dealing with movement-related constraints, such as low battery or environmental obstacles, which required condition-based flow control.

The decision to keep movement logic simple (forward/backward only) and simulate obstacles randomly was made to ensure the system remained within the assignment scope, yet realistic enough for a real-world use case.

### Limitations and Future Work

Currently, movement is limited to a single axis (Y-axis), and the environment is basic. Future versions could introduce:
- X-Y grid navigation
- Sensor-driven obstacle mapping
- Timed battery drain or asynchronous task processing
- GUI or REST-based interaction layer

### References

- Alchin, M. (2010) *PEP 8 Style Guide for Python*, in: Alchin, M. *Pro Python*. Apress.
- Weber, A. (2024). Humanoid Robots Push the Bounds of Collaborative Manufacturing. *Assembly Magazine*.
- Kheddar, A. et al. (2019). Humanoid Robots in Aircraft Manufacturing. *IEEE Robotics & Automation Magazine*.
- Rao, M.V.S. & Shivakumar, M. (2018). Battery Monitoring and Recharging. *IJRITCC*.
- Mukherjee, D. et al. (2022). Human-Robot Collaboration Strategies. *Robotics & CIM*.

---

## 📂 File Structure
```
/Humanoid_Robot_OOP_Project
├── main.py
├── hmr_robot.py
├── hmr_battery.py
├── hmr_task_manager.py
├── hmr_environment.py
├── test_robot.py        # Automated test script
└── README.md            
```

---

## 👨‍💻 Author
**Mobeen Ali**  
GitHub: [mobeen-ali](https://github.com/mobeen-ali)
