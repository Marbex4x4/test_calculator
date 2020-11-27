import os, json
import MQReceiver

class Add():
    def run(self):
        MQReceiver.Listener()

if __name__ == '__main__':
    app = Add()
    app.run()

