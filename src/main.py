import keyboard
import sys


class Test():
    def __init__(self):
        self.showHints()
        self.listenInput()

    def showHints(self):
        print("Click ctrl+c to create new record\n")
        print("Click ctrl+d to delete record")

    def listenInput(self):
        keyboard.add_hotkey("ctrl+c", lambda: print("CTRL+C Pressed!"))

def main():
    Test()
    input()

if __name__ == '__main__':
    main()