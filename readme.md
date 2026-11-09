<div align="center">

# 🐍 Python Series: Zero to Hero

**A structured, project-driven journey through Python programming — from core language fundamentals to full-stack desktop apps, CLI utilities, and 2D arcade games.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-CE%20%2F%202.x-00B4D8?style=for-the-badge&logo=gamepad&logoColor=white)](https://pyga.me/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter%20%2F%20ttk-FF6B6B?style=for-the-badge&logo=window-restore&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![Packaging](https://img.shields.io/badge/Packaging-pyproject.toml%20%7C%20uv-4CAF50?style=for-the-badge&logo=pypi&logoColor=white)](https://peps.python.org/pep-0621/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()

[Explore Lessons](#1-1_basics--the-foundations) • [Password Generator](#2-2_password_generator--cli-utility) • [Space Defender](#3-3_space_defender--2d-arcade-game) • [Note Keeper](#4-4_note_keeper--desktop-gui-app) • [Quick Start](#-quick-start)

---

</div>

## 📌 Overview

This repository is designed as an end-to-end learning track and reference codebase for Python developers. It bridges theoretical fundamentals with hands-on software development through four progressive modules:

1. **Foundations (`1_BASICS`)**: 32 structured lessons covering language syntax, data structures, control flow, functional programming, OOP, error handling, and unit testing.
2. **CLI Engineering (`2_Password_Generator`)**: An interactive terminal tool with dynamic ANSI cursor management, customizable constraints, and modern PEP 621 packaging.
3. **Game Development (`3_Space_Defender`)**: An arcade space shooter powered by Pygame/Pygame-CE featuring sprite groups, vector physics, collision detection, progressive waves, and high-score persistence.
4. **Desktop GUI Engineering (`4_Note_keeper`)**: A desktop note management app built with Tkinter and themed TTK widgets backed by atomic JSON persistence.

---

## 📂 Repository Directory Map

```text
python_series/
├── 📁 1_BASICS/                     # 32 Step-by-step modular core Python lessons
│   ├── 01-03 Variables & Numbers   # Primitive data types, strings, operators
│   ├── 04-10 Lists & Tuples        # Sequence operations, sorting, comprehensions, slicing
│   ├── 11-14 Logic & Conditions    # Boolean logic, conditionals, deep if statements
│   ├── 15-17 Dictionaries          # Hash maps, key/value iterations, nested structures
│   ├── 18-20 User Input & Loops    # Console input, while loops, iterators
│   ├── 21-24 Functions             # Signatures, *args/**kwargs, return values
│   ├── 25-28 OOP & Modules         # Classes, inheritance, encapsulation, modularity
│   ├── 29-30 File I/O              # File streaming, read/write/append operations
│   ├── 31-32 Robust Code           # Exception handling & unittest test suites
│   ├── cars.py & hello.py          # Helper modules and entrypoint demos
│   └── 📁 text_folder/             # Sample datasets for file handling exercises
│
├── 📁 2_Password_Generator/         # Interactive CLI password utility
│   ├── main.py                     # CLI state loop & ANSI terminal cursor control
│   ├── pyproject.toml              # Modern Python packaging configuration (uv/pip)
│   └── uv.lock                     # Deterministic dependency lockfile
│
├── 📁 3_Space_Defender/             # Full 2D Arcade Space Shooter Game
│   ├── main.py                     # Central game loop, event dispatcher & clock
│   ├── settings.py                 # Game configuration, physics constants, speed scaling
│   ├── ship.py                     # Player spacecraft entity, bounds checking, blitting
│   ├── alien.py                    # Enemy fleet behavior & edge-detection logic
│   ├── bullet.py                   # Sprite-based projectile physics
│   ├── button.py                   # Custom UI click-to-start overlay component
│   ├── game_stats.py               # Player life counters, score state, game flags
│   ├── scoreboard.py               # HUD rendering (lives icons, current level, high score)
│   ├── readme.md                   # Complete 1,700+ line Pygame deep-dive guide
│   └── 📁 resources/               # Vector & raster sprite assets (ship, aliens)
│
├── 📁 4_Note_keeper/                # Minimalist desktop GUI notes manager
│   ├── main.py                     # Tkinter/TTK UI, two-column layout & event bindings
│   └── notes.json                  # Local JSON database for persistent note storage
│
├── .gitignore                      # Git ignored files & environments
└── readme.md                       # Master repository documentation
```

---

## 🗂️ In-Depth Folder Breakdown

### 1. `1_BASICS` — The Foundations

A sequential, hands-on syllabus divided into distinct Python topic files. Each file contains runnable sample code, edge-case demonstrations, and inline documentation.

| # | File | Core Topics Covered |
|---|---|---|
| `01` | [`1_variables.py`](/1_BASICS/1_variables.py) | Variable assignment, memory labels, naming standards, snake_case |
| `02` | [`2_strings.py`](/1_BASICS/2_strings.py) | String formatting (`f-strings`), casing (`.title()`, `.upper()`), stripping whitespace |
| `03` | [`3_numbers.py`](/1_BASICS/3_numbers.py) | Integers, floats, arithmetic operators, floor division, exponentiation |
| `04` | [`4_lists.py`](/1_BASICS/4_lists.py) | List creation, zero-based indexing, negative indexing |
| `05` | [`5_lists_operations.py`](/1_BASICS/5_lists_operations.py) | `.append()`, `.insert()`, `del`, `.pop()`, `.remove()` |
| `06` | [`6_list_organization.py`](/1_BASICS/6_list_organization.py) | Permanent sort (`.sort()`), non-destructive (`sorted()`), `.reverse()`, `len()` |
| `07` | [`7_list_elements.py`](/1_BASICS/7_list_elements.py) | Iterating sequences with `for` loops, loop variable scoping |
| `08` | [`8_indentations.py`](/1_BASICS/8_indentations.py) | PEP 8 indentation standards, block scope, syntax rules |
| `09` | [`9_numerical_lists.py`](/1_BASICS/9_numerical_lists.py) | `range()`, `min()`, `max()`, `sum()`, list comprehensions |
| `10` | [`10_slicing_and_copying.py`](/1_BASICS/10_slicing_and_copying.py) | Slice notation `[start:stop:step]`, shallow copies (`[:]`) vs references |
| `11` | [`11_tuples.py`](/1_BASICS/11_tuples.py) | Immutability, single-element tuples, unpacking |
| `12` | [`12_conditional.py`](/1_BASICS/12_conditional.py) | Comparison operators (`==`, `!=`, `<`, `>`), membership (`in`, `not in`) |
| `13` | [`13_deep_if_statements.py`](/1_BASICS/13_deep_if_statements.py) | `if-elif-else` control flow, logical combinations (`and`, `or`) |
| `14` | [`14_special_things.py`](/1_BASICS/14_special_things.py) | Handling empty lists as falsy values, multiple sequence comparisons |
| `15` | [`15_dictionary.py`](/1_BASICS/15_dictionary.py) | Key-value mapping, dynamic additions, `.get()` method |
| `16` | [`16_deep_dictionary.py`](/1_BASICS/16_deep_dictionary.py) | Iterating `.keys()`, `.values()`, `.items()`, sorting dictionaries |
| `17` | [`17_nesting.py`](/1_BASICS/17_nesting.py) | Dictionaries in lists, lists in dictionaries, multi-level nesting |
| `18` | [`18_input.py`](/1_BASICS/18_input.py) | User interaction with `input()`, type casting (`int()`, `float()`), modulo `%` |
| `19` | [`19_while_loop.py`](/1_BASICS/19_while_loop.py) | Event-driven loops, flag variables, `break` and `continue` |
| `20` | [`20_while_with_iterators.py`](/1_BASICS/20_while_with_iterators.py) | Moving elements between lists, purging values, populating dicts |
| `21` | [`21_functions.py`](/1_BASICS/21_functions.py) | Function signatures, parameters, arguments, docstrings |
| `22` | [`22_function_arguments.py`](/1_BASICS/22_function_arguments.py) | Positional, keyword, default parameter values |
| `23` | [`23_returing.py`](/1_BASICS/23_returing.py) | Return statements, optional arguments, returning dictionaries |
| `24` | [`24_final_functions.py`](/1_BASICS/24_final_functions.py) | Variadic positional arguments (`*args`), keyword arguments (`**kwargs`) |
| `25` | [`25_classes.py`](/1_BASICS/25_classes.py) | Object-oriented paradigm: `class`, `__init__`, `self`, instances |
| `26` | [`26_encapsulation.py`](/1_BASICS/26_encapsulation.py) | Attribute access, setter methods, internal state modification |
| `27` | [`27_inheritance.py`](/1_BASICS/27_inheritance.py) | Parent and subclass relationships, `super().__init__()`, method overrides |
| `28` | [`28_modules.py`](/1_BASICS/28_modules.py) | Importing entire modules, specific functions, aliases (`as`), namespaces |
| `29` | [`29_file_handling.py`](/1_BASICS/29_file_handling.py) | Context manager `with open()`, `.read()`, `.readlines()`, streaming large files |
| `30` | [`30_file_writting.py`](/1_BASICS/30_file_writting.py) | File write (`'w'`), append (`'a'`), and read-write (`'r+'`) modes |
| `31` | [`31_error_handling.py`](/1_BASICS/31_error_handling.py) | `try / except / else / finally`, preventing crashes gracefully |
| `32` | [`32_testing.py`](/1_BASICS/32_testing.py) | Automated testing with standard library `unittest`, test cases & assertions |

---

### 2. `2_Password_Generator` — CLI Utility

An interactive command-line application that generates cryptographically strong random passwords with an optimized terminal UX.

```text
==================================================
              PASSWORD GENERATOR
==================================================
1. Generate Password (Default 8 Characters)
2. Generate Password with Custom Length
3. Generate Multiple Passwords
q. Quit
==================================================
```

#### ✨ Highlights
- **ANSI Terminal Control**: Implements terminal cursor manipulation (`\033[1A`, `\x1b[2K`) to re-render menus in place without terminal clutter.
- **Robust Validation**: Validates user inputs with type safety and user-friendly error messages.
- **Bulk Creation**: Supports batch generation of multiple custom-length passwords in a single run.
- **Modern Packaging**: Ready for deployment via `pyproject.toml` entry points (`password-generator = "main:main"`).

---

### 3. `3_Space_Defender` — 2D Arcade Game

A complete retro 2D arcade shooter built on top of the Pygame engine. Defend planet Earth against descending fleets of hostile aliens!

```text
+-------------------------------------------------------------+
| Score: 1,450   High Score: 8,200   Level: 3   Lives: 🚀 🚀  |
|                                                             |
|         👾   👾   👾   👾   👾   👾   👾   👾               |
|         👾   👾   👾   👾   👾   👾   👾   👾               |
|                                                             |
|                              | (Laser)                      |
|                                                             |
|                             [▲] (Player Ship)               |
+-------------------------------------------------------------+
```

#### ✨ Highlights
- **Sprite Groups & Physics**: Uses `pygame.sprite.Group` for collision detection between bullets, shields, alien swarms, and the player ship.
- **Dynamic Wave Difficulty**: Speed, fire rate, and alien point yields scale geometrically (`speed_scale = 1.1`, `score_scale = 1.5`) as waves are cleared.
- **HUD & Scoreboard**: Real-time rendering of current score, active level, remaining ship lives, and an all-time high score.
- **Clean Architecture**: Decoupled into specialized modules ([`ship.py`](/3_Space_Defender/ship.py), [`alien.py`](/3_Space_Defender/alien.py), [`bullet.py`](/3_Space_Defender/bullet.py), [`settings.py`](/3_Space_Defender/settings.py), [`scoreboard.py`](/3_Space_Defender/scoreboard.py)).
- **Included Masterclass**: Contains a standalone, in-depth **1,700+ line guide** ([`readme.md`](/3_Space_Defender/readme.md)) explaining game loop theory, event dispatching, and rendering from scratch.

#### 🎮 Controls
| Key / Input | Action |
|---|---|
| <kbd>→</kbd> Right Arrow | Move ship right |
| <kbd>←</kbd> Left Arrow | Move ship left |
| <kbd>Spacebar</kbd> | Fire laser bullet |
| <kbd>Mouse Click</kbd> | Click **Play** button to start / restart |
| <kbd>Q</kbd> | Quit game |

---

### 4. `4_Note_keeper` — Desktop GUI App

A lightweight, clean desktop note-taking application created with Python's built-in `tkinter` and `ttk` libraries.

```text
+-------------------+-----------------------------------------+
|  My Notes         |  Title: [ Project Ideas               ] |
|                   |-----------------------------------------|
|  • Python Basics  |  Content:                               |
|  • Project Ideas  |  1. Build a desktop app                 |
|  • ML Roadmaps    |  2. Save notes to JSON                  |
|                   |  3. Add dark mode toggle                |
|  [+ New Note]     |                                         |
|                   |  [ Save Changes ]        [ Delete Note] |
+-------------------+-----------------------------------------+
```

#### ✨ Highlights
- **Two-Column Responsive Layout**: Left sidebar with quick-access note listbox and title search; right workspace for note editing.
- **Clam Themed TTK Design**: Styled with a modern palette (`#f5f5f7` canvas, `#e8e8ed` sidebar, customized typography).
- **CRUD Operations**: Full support to Create, Read, Update, and Delete notes.
- **Safe Persistence**: Automatically syncs state to [`notes.json`](/notes.json) on every mutation with fallback defaults for first-time runs.

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/RishatTalukder/python_series.git
cd python_series
```

### 2. Set Up a Virtual Environment

#### On Linux / macOS:
```bash
python3 -m venv env
source env/bin/activate
```

#### On Windows:
```cmd
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies

The repository uses standard library packages for the basics, Tkinter for GUI, and Pygame for the game:

```bash
# Core requirements (install pygame or pygame-ce)
pip install pygame-ce requests
```

> [!TIP]
> If you are on **Python 3.14+** on Linux/Ubuntu, `pygame-ce` (Pygame Community Edition) offers the best compatibility out-of-the-box:
> ```bash
> pip install pygame-ce
> ```

---

## 💻 Running the Projects

### Running Lessons (`1_BASICS`)
Execute any lesson file directly:
```bash
python 1_BASICS/1_variables.py
python 1_BASICS/25_classes.py
python 1_BASICS/32_testing.py
```

### Launching the Password Generator
```bash
python 2_Password_Generator/main.py
```
*(Or install via `pip install -e 2_Password_Generator` and run `password-generator` anywhere!)*

### Playing Space Defender
```bash
cd 3_Space_Defender
python main.py
```

### Opening Note Keeper
```bash
python 4_Note_keeper/main.py
```

---

## 🛠️ Tech Stack & Tools

| Technology | Purpose |
|---|---|
| **Python 3.10+ / 3.12 / 3.14** | Core programming language |
| **Pygame-CE / Pygame** | 2D game physics, rendering, sprite animation, sound engine |
| **Tkinter & TTK** | Cross-platform desktop native UI styling & window management |
| **JSON** | Lightweight serialization & disk persistence format |
| **Unittest** | Python built-in unit testing framework |
| **UV / Pyproject.toml** | Modern dependency management and Python packaging |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

<div align="center">

Made with ❤️ by [Rishat Talukder](https://github.com/RishatTalukder) • Star ⭐ this repository if you found it helpful!

</div>
