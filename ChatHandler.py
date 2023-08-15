# Links database to Flask template
class ChatHandler():

    # Pulls channels from database. 
    # Builds the channel_html 
    # Returns channel html or false if no channels
    # There should always be a channel
    def get_channel_html(query, selected_channel):
        channels = query.fetch_channels()
        if len(channels) == 0: # Forcing it even though 404 redirects should be automatic
            return False
        channel_html = []
        for channel in channels:
            channel = channel[0]
            selected = ""

            #Allows me to edit the properties of the selected channel
            if channel == selected_channel:
                selected = "selected"
            #The ID is dicey here because there could be overlap with other ids potentially.
            html = """<div class='channel' id='unique-id-%s' name='unique-id-%s'>
                        <button type='submit'><p class='chat-text %s'>%s</p></button>
                    </div>""" % (channel, channel, selected, channel)
            channel_html.append(html)
        return channel_html
    
    # Fetches messages for the given channel
    # Fills in html -> If its the signed-in user's message, appears as 'You' otherwise username
    # Returns list of messages for the channel. Can be empty. 
    def get_message_html(query, username, channel_name):
        # message_content, display_name
        messages = query.fetch_messages(channel_name)
        message_html = []
        print("username: ", username)
        for message in messages:
            html_class = "other"
            h2 = message["display_name"]
            print(message)
            if message["display_name"] == username:
                html_class = "user"
                h2 = "You"            
            # If display_name == username, class = user & h2 = You
            # Else, class = other & h2 = display_name
            html = """
            <div id='chat-bubble' class='%s'>
                <h2>%s</h2>
                <p class='msg-box'>%s</p>
            </div>""" % (html_class, h2, message["message_content"])
            message_html.append(html)

        return message_html

        