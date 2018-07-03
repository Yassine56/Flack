import os
import requests

from flask import Flask, render_template, request, json
from flask_socketio import SocketIO, emit
from flask_socketio import join_room, leave_room
from models import *

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = []
channelNames = []
message = None
@app.route("/index")
def appah():
    return render_template('index.html')

@app.route("/")
def index():

    return render_template('squelette.html',channels=channelNames)

@socketio.on("new channel")
def vote(data):
    count = 0
    channelName = data['channelname']
    for channel in channels:
        if channel.name == channelName:
            count = 1
    if count == 0:
        channel = Channel(name=channelName)
        channels.append(channel)
        channelNames.append(channelName)
        emit("channel_created")
    else :
        emit("new channel error")

@socketio.on("submit channel search")
def viewchannel(data):
    count = 0

    channeltoleave = data['currentchannel']
    channelName = data['channelname']
    for name in channelNames:
        if name == channelName:
            count = 1
    if count == 0:
        emit("search channel name error")
    else :
        for channel in channels:
            if channel.name == channelName:
                if channeltoleave :
                    leave_room(channeltoleave)
                messages = []
                counter = 0
                for m in channel.messages:
                    if(counter<100):
                        messages.append(m)
                    counter = counter+1
                join_room(channelName)
                emit("channel details", {"messages":json.dumps([ob.__dict__ for ob in messages])})

@socketio.on("send message to room")
def broadcastmsg(data):
    message = data['message']
    text = message['text']
    print(text)
    sender = message['sender']
    print(sender)
    channel = message['channel']
    time = message['time']
    message = Message(text=text, sender=sender, channel=channel, time=time)
    for channell in channels:
        if channell.name == channel:
            channell.messages.append(message)
    print('emit start')
    emit("message update", {"message": json.dumps(message.__dict__)}, room=channel)
    print('emit ends')
