import sqlite3, datetime 

class Query():

    #Adds an account to the db
    #Also checks if account exists
    #Returns true if account exists
    #False if not
    def create_account(email, hashed_password, hashed_salt, display_name):
        try:
            # Connect to the database
            conn = sqlite3.connect('chatroom.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO accounts (email, hashed_password, hashed_salt, display_name) VALUES (?, ?, ?, ?)", (email, hashed_password, hashed_salt, display_name,))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        
    #Adds a new channel to the db
    #If added, returns True
    #Otherwise returns false
    def create_channel(channel_name):
        try:
            conn = sqlite3.connect('chatroom.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO channels (channel_name) VALUES (?)", (channel_name,))
            conn.commit()
            return True
        except sqlite3.IntegrityError: #Channel already exists
            return False
            

    #Gets the hashed password of the email if exists
    #Returns hashed_password or None if does not exist.
    def get_hashed_password(display_name):
        try:
            conn = sqlite3.connect('chatroom.db')
            cursor = conn.cursor()
            cursor.execute("SELECT hashed_password FROM accounts WHERE display_name = ?", (display_name,))
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

    #Returns a list of channels
    def fetch_channels():
        try:
            conn = sqlite3.connect('chatroom.db')
            cursor = conn.cursor()

            query = "SELECT channel_name FROM channels ORDER BY channel_id ASC;"
            cursor.execute(query)
            result_set = cursor.fetchall()
            
            channel_list = []
            
            for row in result_set:
                channel_list.append(row)

            return channel_list
        
        except Exception as e:
            print(e)
            return []

    #Get all messages from given channel_name in ascending order by timestamp
    #Returns in a dictionary of the display name and message in ascending order by timestamp
    #If there's an error, returns empty array b/c there doesn't have to be any messages
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
            return []
        
    #Checks if display name exists. 
    #Returns true if yes, false if not. 
    def display_name_exists(display_name):
        conn = sqlite3.connect('chatroom.db')
        cursor = conn.cursor()

        query_name = """
            SELECT display_name FROM accounts
            WHERE display_name = ?
        """

        cursor.execute(query_name, (display_name,))
        result_set = cursor.fetchall()

        if result_set > 0:
            return True
        return False