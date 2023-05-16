# The Labyrinth of Ghouls and Treasures

Welcome to "The Labyrinth of Ghouls and Treasures"! In this text-based game, your goal is to navigate through a series of rooms and avoid the lurking monster. The game consists of three rooms, each with its own unique description and connections to other rooms. One of the rooms contains a fearsome monster, and if you enter that room, it's game over.

To create this game in Python, we define a Room class that represents each room in the game. Each Room object has a description, a boolean flag indicating the presence of a monster, and a dictionary of connected rooms. The add_room method is used to connect rooms together by specifying a direction and the adjacent room.

In the game function, we create three instances of the Room class, representing the initial state of the game. We set up the connections between the rooms using the add_room method. We start the game in the first room and use a while loop to repeatedly prompt the player for input.

During each iteration of the loop, we print the current room's description. If the current room has a monster, the game ends. Otherwise, we ask the player which direction they want to go. If the input matches a valid direction for the current room, we update the current_room variable to the connected room in that direction. If the input is not a valid direction, we display an error message.

You can run the game by executing the game function. The program will display the initial message and continue until you either encounter the monster or reach the end of the game.

This game provides a simple framework that can be expanded upon to include additional features such as item collection, puzzles, or multiple levels. Have fun exploring "The Labyrinth of Ghouls and Treasures" and see if you can successfully avoid the monster!

You can see some more complicated versions of this code in the bellow repository.

- https://github.com/iman-n/text-based-game.git
