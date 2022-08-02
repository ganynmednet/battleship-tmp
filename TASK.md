Battleship task
Your task is to implement the backend for a Battleship game. There should be a RESTful API that can later be used to create a web UI to display the state of a game and provide controls to interact with the backend. 
The rationale for asking you to do this task is to have a base to facilitate a technical discussion between engineers. When asked about particular aspects or details you should be able to argue why you chose to do things a certain way, what alternatives/options you considered and explain how things work in practice. See this as an opportunity to prepare a stage for presenting your skills the way you would like them to be seen.

For example, one API call to make a move might be:

URL
method
Headers
/move/1/3
POST
Authentication: Bearer e1e7466d-f25d-4781-8132-3dd928a87d2a


, where one player with a specific authentication token makes a move on row 1, column 3. You can also choose other authentication methods and you can also design your API in another way. It is only necessary to fulfill the requirements mentioned below.

Product requirements:
A single game can include multiple rounds
It should be possible for multiple pair of players to play games at the same time
The grids should be 10 by 10 and there should be at least three differently sized ships for each player.
It is up to you to choose how to implement placement of the ships (e.g. by players or random), but you should implement validity checks, e.g. ships of one player must not (partially) overlap/stack/be outside of the board
The backend should check whether a move is actually possible and report a failure if it is not
You can assume that the frontend polls about updates, i.e. it manually checks your API regularly if there are any updates (i.e. the other player has made a move, if a game has been finished, etc.)
The won games should be stored per user and there should be an API endpoint to get a high score list
You should be prepared to present and explain your code for other developers
You should be prepared to give a live demo in some way (a frontend is not needed, but a way could be to use tools like “Postman” to present it)

Technical requirements:
Please implement this project in Python with a framework and additional libraries of your choice (you can choose Django, Flask, FastAPI, or just Python network libraries)
In the end, there should be a working server where it is possible to call API endpoints (a real web server setup is not needed, it is fine if the server needs to be started manually, you can find a fast/easy way to do it to present a live demo)
Some basic authentication mechanism should work and endpoints should be checked against it (i.e. if it’s Player1’s turn, Player2 should not be able to make the move)
Your code and architecture should be clean and follow guidelines that you would also like to see in a professional project (also taking in consideration how the project could be extended later but there is no need to over-engineer or bloat the code with design patterns if they have no use; find a reasonable trade-off yourself)
Some basic persistence/storage mechanism, like a database or file storage, should be used.

Please upload your project to a public Github/Gitlab/… repository where it’s possible to view the code online.

If you feel that information is missing in this task, please make reasonable decisions yourself. If you cannot implement all features of this project as you would like to (e.g. because there is just not enough time), be prepared to explain extension points or to-dos clearly.




Product requirements:
A single game can include multiple rounds
It should be possible for multiple pair of players to play games at the same time
The grids should be 10 by 10 and there should be at least three differently sized ships for each player.
It is up to you to choose how to implement placement of the ships (e.g. by players or random), but you should implement validity checks, e.g. ships of one player must not (partially) overlap/stack/be outside of the board
The backend should check whether a move is actually possible and report a failure if it is not
You can assume that the frontend polls about updates, i.e. it manually checks your API regularly if there are any updates (i.e. the other player has made a move, if a game has been finished, etc.)
The won games should be stored per user and there should be an API endpoint to get a high score list
You should be prepared to present and explain your code for other developers
You should be prepared to give a live demo in some way (a frontend is not needed, but a way could be to use tools like “Postman” to present it)
