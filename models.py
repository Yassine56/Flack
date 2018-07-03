class Message:

    def __init__(self, text, sender, channel, time):
        self.text = text
        self.sender = sender
        self.channel = channel
        self.time = time

class Channel:

    def __init__(self, name):
        self.name = name
        self.messages = []

    def add_message(self, m):
        self.messages.append(m)
        
