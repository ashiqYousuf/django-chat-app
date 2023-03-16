# Django Chat Application
This is a simple chat application built using Django. It allows multiple users to join and communicate in real-time via a chat room.

# Getting Started
To get started with this project, follow these steps:

*Clone the repository to your local machine* \
*Create a virtual environment using virtualenv* \
*Activate the virtual environment* \
*Install the required packages using pip install -r requirements.txt* \
*Run the migrations using python manage.py migrate.* \
*Start the development server using python manage.py runserver* \
*Now you can navigate to http://localhost:8000/ to see the chat application in action* \

# Usage
To use the chat application, simply enter a username and click on the "Join Chat" button. You will then be redirected to the chat room where you can communicate with other users in real-time.

# Features
* Real-time communication via websockets.
* Simple and intuitive user interface.

# Technologies and Tools Used
* Python
* Django
* Django Channels
* JavaScript
* HTML
* CSS
* Django Templates
* Redis

# How to Run the project
1. Create superusers from admin panel ex: **john** and  **tim** and Login them from different instances of your web browser
2. If you want to make a websocket connection between them , then from **Johns** Interface type the URL **'127.0.0.1:8000/chat/tim'** implies John wants to talk to tim and from **Tims** interface run  **'127.0.0.1:8000/chat/john'**.
3. Do not forget to run **redis-server**

# Contributions
Contributions to this project are welcome. 

# A short glimpse

![image_2](./screenshots/Screenshot%20from%202023-03-14%2002-54-25.png)

![image_1](./screenshots/Screenshot%20from%202023-03-14%2002-53-33.png)

