# Meals To Go — Python CLI

A small, interactive restaurant ordering application built with Python's standard library. Browse a mini menu, add meals to a basket, change quantities, remove items and check out from a colourful terminal interface.

## Run it

Requires Python 3.10 or newer. No third-party packages are needed.

From the repository root:

```bash
python python_cli/main.py
```

On Windows, use `py python_cli/main.py` if the `python` command is not available.

## Run the tests

```bash
python -m unittest discover -s python_cli -p "test_*.py" -v
```

## What this project demonstrates

| Python concept | Where it is used |
|---|---|
| Dictionaries | The menu stores item names, prices and categories; the basket stores item quantities |
| Lists / iteration | Menu and basket entries are iterated to display the order |
| Classes and objects | `Restaurant` manages the menu and basket; `MenuItem` represents a menu item |
| Functions | Menu display, basket display, checkout, input validation and application loop |
| Parameters | Methods and functions accept item IDs, quantities and restaurant data |
| Data structures | A dictionary-based basket supports adding, counting and removing items |
| Error handling | Invalid menu selections and quantities are handled without crashing |
| Unit testing | `unittest` checks basket operations, totals and input constraints |

## Features

- Seven sample meals, sides and drinks priced in Ghana cedis
- Add multiple quantities of an item
- View basket contents and subtotal
- Remove items from the basket
- Checkout and clear the basket
- Input validation and friendly terminal messages

## Project structure

```text
python_cli/
├── main.py
├── test_main.py
└── README.md
```

## Development transparency

This version was created with AI assistance during a guided development session. It is a learning project: review the code, run it, understand each class and function, and make your own changes before presenting it as independently developed work.

## Possible next improvements

- Save orders to a JSON file
- Add customer names and order numbers
- Add daily specials and menu categories
- Add a discount code feature
