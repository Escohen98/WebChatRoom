# WebChatRoom
This is the epitomy of what I have been attempting to achieve through these Web Development classes. My goal was to figure out a new portal to display my back-end code. I've successfully learned Python Flask, and can now use Vue.js. Although Vue.js is not displayed in this project, I would say that it was a true success. The main reason vue is not here is due to how it may conflict with Flask. They are fairly similar in concept, at least if running Vue.app, though Flask has a bit of functionality that Vue does not. 

Anyway, this is a web chat room for people to communicate with one another. 

# Setting Up the Database
1. Create a local db file in the home path
2. Open .db file: `.open {database name}.db`
2. Queries:
    ```sql
    CREATE TABLE accounts (
        user_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        email TEXT NOT NULL UNIQUE, 
        password TEXT NOT NULL, 
        display_name TEXT NOT NULL UNIQUE
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

# Dependencies
pip3 install flask<br>
pip3 install firebase_admin<br>
pip3 install bcrypt<br>