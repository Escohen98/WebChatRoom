# Links database to Flask template
class ChatHandler():

    # Pulls channels from database. 
    # Builds the channel_html 
    # Returns channel html or false if no channels
    # There should always be a channel
    def get_channel_html(query):
        channels = query.fetch_channels()
        if len(channels) == 0: # Forcing it even though 404 redirects should be automatic
            return False
        channel_html = []
        for channel in channels:
            channel = channel[0]
            html = """<div class='channel' id='%s' name='%s'>
                        <button type='button'><p class='chat-text'>%s</p></button>
                    </div>""" % (channel, channel, channel)
            channel_html.append(html)
        return channel_html
    
    # Fetches messages for the given channel
    # Fills in html -> If its the signed-in user's message, appears as 'You' otherwise username
    # Returns list of messages for the channel. Can be empty. 
    def get_message_html(query, username, channel_name):
        # message_content, display_name
        messages = query.fetch_messages(channel_name)
        message_html = []
        for message in messages:
            message = message[0]
            html_class = "other"
            h2 = username
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

        