# WebChatRoom
This is the epitome of what I have been attempting to achieve through these Web Development classes. My goal was to figure out a new portal to display my back-end code. I've successfully learned Python Flask, and can now use Vue.js. Although Vue.js is not displayed in this project, I would say that it was a true success. The main reason vue is not here is due to how it may conflict with Flask.

I also gave up on Firebase. It was a pain in the butt so I decided to revert back to what I am comfortable with; SQL(ITE). Way better. Makes more sense, though I will have to set up sockets for the chat to auto-update without refreshing the page manually. We'll see...

I am so extremely proud that I got user authentication working and chat messaging in the sense that the system knows who is typing the message and will display accordingly. Muahaha. 

There's a lot of lacking features and bugs in code [see below]. Probably should have focused on the chat functions instead of the user authentication, but I'm pretty proud of that part. I also like working on things sequentially. Sorry this took me a while. If you are viewing this before patching the bugs and completing the to-dos, I am sorry, I ran out out of time 😢

Anyway, this is a web chat room for people to communicate with one another - sort of. 

# Setting Up the Database
1. Create a local db file in the home path
2. Open .db file: `.open {database name}.db`
2. Queries:
    ```sql
    CREATE TABLE accounts (
        user_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        display_name TEXT NOT NULL UNIQUE,
        hashed_password TEXT NOT NULL,
        salt TEXT NOT NULL
        );
    ```
    ```sql
    CREATE TABLE channels (
        channel_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        channel_name TEXT NOT NULL UNIQUE
        );
    ```
    ```sql
    CREATE TABLE messages (    
        message_ID INTEGER PRIMARY KEY AUTOINCREMENT,    
        channel_ID INTEGER,    
        user_ID INTEGER,    
        message_content TEXT NOT NULL,    
        timestamp DATETIME NOT NULL,    
        FOREIGN KEY (channel_ID) REFERENCES channels (channel_ID),    
        FOREIGN KEY (user_ID) REFERENCES users (user_ID)
        );
    ```

# Bugs
* If someone else logs in, everyone becomes logged in to that account???     

# TO-DO:
## I don't know if I will have time to get to any of these. Please have mercy on me for not getting this to work 
* Set up socket.io so things can auto-update on every user's end when a message is sent
* Get changing of the channels to work (idk if this is going to work)

## If I want to go above and beyond ...
* Delete channels and edit channel names
* Delete account option? Idk. 

# Dependencies
pip3 install flask<br>
pip3 install bcrypt