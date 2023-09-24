# Python Troop Management System

This Python script implements a troop management system for a game. It allows players to add and manage troops, perform attacks, generate income, and monitor the status of troops and enemies. The system includes different troop types, each with its own characteristics.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Troop Classes](#troop-classes)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.x

# Getting Started
RUN test.py


## FILES
- ### command
      {user command inputs handler}
- - Command_Manager  -> execute functions based on user command
- - Get_Command      -> manage command inputs and give to Command_Manager
- ### core
      {The core of the program and management of all functions}
- - Actions          -> execute based on user commands and handle game actions
- - Automate         -> handel function that should be automate and cant call from user
- - Enemy            -> contain enemy attr
- - Player           -> contain player attr
- - Troops           -> contain troops attr

### Add a troop to your army
###### Stick_Man.Action.Add_Troops
   ```python
   add_troop(TYPE: (troops_class_objec)t,TIMESTAMPS: (mm:ss:fff))
```

### Get army status
###### Stick_Man.Action.Army_Status
   ```python
   army_status(TIMESTAMPS: (mm:ss:fff))
```

#### Get enemy status
###### Stick_Man.Action.Enemy_Status
   ```python
   enemy_status(TIMESTAMPS: (mm:ss:fff))
```

#### Get money status
###### Stick_Man.Action.Money_Status
   ```python
   money_status(TIMESTAMPS: (mm:ss:fff))
```
#### Give damage into troops
###### Stick_Man.Action.Damage
   ```python
   damage(troops_id: int, damage_amount: int, TIMESTAMPS: (mm:ss:fff))
```
