#! /usr/bin/python

def emailProtocol(direction, message):
    error = 0

    if direction == 'sending':
        # send stuff
        pass
    else:
        # recieve stuff
        pass

    return error

def smsProtocol(direction, message):
    error = 0

    if direction == 'sending':
        # send stuff
        pass
    else:
        # recieve stuff
        pass

    return error


protocols = {"email": emailProtocol
             "sms":   smsProtocol}

class Message:
    def __init__(self, sender, reciever, args, protocol):
        self.senderName = sender
        self.recieverName = reciever
        self.argsList = args
        self.protocol = protocol


def sendMessage (reciever, args, protocol):
    error = 0

    if protocol in protocols:
        protocols[protocol]('sending', Message("to be got from config file",
                                               reciever,
                                               args,
                                               protocol))
    else:
        error = 1

    return error

def recieveMessage():
    message = None
    # recieve the message
    return message
