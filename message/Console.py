from message.FontColor import FontColor

class Console:
    def __init__(this, typee, message):
        this.type = typee
        this.message = message
        this.showConsoleMessage()

    def showConsoleMessage(this):
        if this.type == 'message':
            print(FontColor.CBLACK + 'Message: '+this.message)
        elif this.type == 'success':
            print(FontColor.CGREEN + 'Sucess: '+this.message)
        elif this.type == 'alert':
            print(FontColor.CYELLOW + 'Alert: '+this.message)
        elif this.type == 'error':
            print(FontColor.CRED + 'Error: '+this.message)
        else:
            print(this.message)