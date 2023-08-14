import sqlite3, datetime 

class Query():

    #Adds an account to the db
    def create_account(email, hashed_password, hashed_salt, display_name):
        try:
            # Connect to the database
            conn = sqlite3.connect('chatroom.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO accounts (email, hashed_password, hashed_salt, display_name) VALUES (?, ?, ?, ?)", (email, hashed_password, hashed_salt, display_name,))
            conn.commit()
            return "Success!"
        except sqlite3.IntegrityError:
            return "User already exists."
        
    #Creates a new channel
    def create_channel(channel_name):
        try:
            conn = sqlite3.connect('chatroom.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO channels (channel_name) VALUES (?)", (channel_name,))
            conn.commit()
            return "Success!"
        except sqlite3.IntegrityError:
            return "Channel already exists."
            

    #Gets the hashed password of the email if exists
    #Returns hashed_password or None if does not exist.
    def get_hashed_password(email):
        try:
            conn = sqlite3.connect('chatroom.db')
            cursor = conn.cursor()
            cursor.execute("SELECT hashed_password FROM accounts WHERE email = ?", (email,))
            hashed_password = cursor.fetchone()
            conn.close()
            return hashed_password[0] if hashed_password else None
        except Exception as e:
            print(e)
            return None
        
    #Inserts a message into the db    
    def insert_message(channel_id, user_id, message_content):
        try:
            conn = sqlite3.connect('chatroom.db')
            cursor = conn.cursor()
            
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            query = "INSERT INTO messages (channel_ID, user_ID, message_content, timestamp) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (channel_id, user_id, message_content, timestamp))
            
            conn.commit()
            conn.close()
        except Exception as e:
            print("Error:", e)

    #Get all messages from given channel_name in ascending order by timestamp
    def fetch_messages(channel_name):
        try:
            conn = sqlite3.connect('chatroom.db')
            cursor = conn.cursor()

            query = """
                SELECT m.message_content, u.display_name
                FROM messages m
                INNER JOIN users u ON m.user_ID = u.user_ID
                INNER JOIN channels c ON m.channel_ID = c.channel_ID
                WHERE c.channel_name = ?
                ORDER BY m.timestamp ASC
            """
            cursor.execute(query, (channel_name,))
            result_set = cursor.fetchall()

            messages_list = []

            for row in result_set:
                message_content, display_name = row
                message_dict = {"message_content": message_content, "display_name": display_name}
                messages_list.append(message_dict)

            conn.close()

            return messages_list
        except Exception as e:
            print("Error:", e)
            return "Something went wrong."