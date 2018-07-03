# Project 2

Web Programming with Python and JavaScript
Summary :
This web application allows users to :
- create chat rooms
- join  chat rooms
- send and receive messages in the chat rooms
- it is a single page web app
- insert a username
- remember the username even after closing the browsing window
- remember the last channel the user visited
- it also allows the users to hide messages on click ( personal touch )
Project structure:
this project contains two main folders:
- static: this folder contains all the images and .css files used in this project
- templates: this folder contains all the .html files used in this project
Templates folder:
This section describes the content of the templates folder
- squelette.html :
this file contains all the html elements and javascript that will be executed on the client side.
the buttons "channels" and "message" were meant for functionalities that aren't implemented.
this file contains :
chatbox.html
navabar.html
popup.html
popupcreatechannel.html
and a script : that will execute all the logic of this app on the client side.
-chatbox.html :
this is the container where user will send and receive messages.
-navbar.html :
contains the navigation bar elements, and this is where the user can search for existing channels.
-popup:
contains a form that will be displayed for firstime users to enter their dislpay name
-popupcreateChannel:
contains a form that will be displayed when the users want to create a new channel

application.py:
this file contains the whole logic of our web app where the routes were defined.
