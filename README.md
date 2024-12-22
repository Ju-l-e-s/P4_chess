# Chess Tournament Management

This project is a console application in Python for managing chess tournaments using the Swiss system. It offers the following features:

- **Player Management**: Add and list players with their information.
- **Tournament Management**: Create and manage tournaments with multiple rounds.
- **Pairing Generation**: Pair players according to the Swiss system rules.
- **Result Recording**: Enter match results and update points.
- **Reports**: Generate reports on players and tournaments.

## Prerequisites

- **Python 3.7** or higher installed on your machine.
- Python dependencies listed in `requirements.txt`.

## Installation

1. **Clone the project repository:**

```bash
git clone <REPOSITORY_URL>
```

2. **Navigate to the project directory:**

```bash
cd nom_du_projet
```

3. **Create a virtual environment:**

```bash
python -m venv env
```

**On Windows:**
```bash
env\Scripts\activate
```

**On macOS/Linux:**
```bash
source env/bin/activate
```

4. **Install the dependencies:**
```bash
pip install -r requirements.txt
```



**Usage**
```bash
src/main.py
```
The program displays a main menu allowing you to perform the following actions:

1. **Add a player**: Enter the information of a new player.
2. **List players**: Display the list of registered players.
3. **Create a tournament**: Initialize a new tournament.
4. **List tournaments**: Display the list of existing tournaments.
5. **Start a tournament**: Start the selected tournament.
6. **Quit**: Close the program.

### General Instructions

- **Menu navigation**: Enter the number corresponding to the action you want to perform.
- **Entering information**: Follow the on-screen instructions to enter the required data.
- **Date format**: Dates must be in the format `dd/mm/yyyy`.
- **National ID**: Must consist of two uppercase letters followed by five digits (example: `AB12345`).


## Project Structure:
```
P4/
├── src/
│    ├── main.py
│    ├── controllers/
│    │   ├── match_controller.py
│    │   ├── player_controller.py
│    │   ├── report_controller.py
│    │   ├── round_controller.py
│    │   └── tournament_controller.py
│    ├── models/
│    │   ├── match_model.py
│    │   ├── player_model.py
│    │   ├── round_model.py
│    │   └── tournament_model.py
│    ├── views/
│    │   ├── menu_view.py
│    │   ├── match_view.py
│    │   ├── player_view.py
│    │   └── tournament_view.py
│    ├── data/
│    │    ├── players.json
│    │    └── tournaments.json
│    └── utils/
│         ├── clear.py
├── .gitignore
├── README.md
└── requirements.txt


```