import os, json
import MQReceiver

class Subtract():
    def run(self):
        MQReceiver.Listener()

if __name__ == '__main__':
    app = Subtract()
    app.run()

