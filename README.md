![StickWarLegacy.jpg](https://quera.org/qbox/view/WKDZpqX2GO/StickWarLegacy.jpg)

# :Game: Stickman: Legacy 


This Python script implements a troop management system for a game. It allows players to add and manage troops, perform attacks, generate income, and monitor the status of troops and enemies. The system includes different troop types, each with its own characteristics.
## Table of Contents

- [Getting Started](#getting-started)
- [Files](#files)
- [Add a Troop to Your Army](#add-a-troop-to-your-army)
- [Army Status](#get-army-status)
- [Enemy Status](#get-enemy-status)
- [Money Status](#Get-money-status)
- [Give Damage to Troops](#give-damage-into-troops)
- [License](#license)
- [Contract](#contact)

## Prerequisites

- Python 3.x

# Getting Started
just run `main.py`:
```bash
python main.py
```


## Files
- ### command
      {user command inputs handler}
- - Command_Manager  -> execute functions based on user command
- - Get_Command      -> manage command inputs and give to Command_Manager
- ### core
      {The core of the program and management of all functions}
- - Actions          -> execute based on user commands and handle game actions
- - Automate         -> handel function that should be automate, These are functions that are executed indirectly by the user
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


## License

This project is provided under the terms of the Custom Project License (CPL).

You are free to:
- Use this project for educational and non-commercial purposes.
- Modify the code for personal or non-commercial use.

You are not allowed to:
- Use this project or its code for any commercial purposes without explicit permission from the project author.

If you would like to use this project for commercial purposes, please contact the project author to discuss licensing options.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

For more details, please contact the project author at [Contract](#contact).

© [2023] [Yousof.A.Asadi]
## Contact

For any questions or inquiries, you can contact the project author:

- GitHub: [github.com/Y-A-Asd](https://github.com/Y-A-Asd/)
- Email: yosofasady2@gmail.com