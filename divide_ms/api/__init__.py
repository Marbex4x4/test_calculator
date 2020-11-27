import os, json
import MQReceiver

class Divide():
    def run(self):
        MQReceiver.Listener()

if __name__ == '__main__':
    app = Divide()
    app.run()

