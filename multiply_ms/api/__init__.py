import os, json
import MQReceiver

class Multiply():
    def run(self):
        MQReceiver.Listener()

if __name__ == '__main__':
    app = Multiply()
    app.run()

