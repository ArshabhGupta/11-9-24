class Bird:
    def __init__(self):
        print("Bird is ready!")
    def whoisthis(self):
        print("I am a bird!")
    def swim(self):
        print("Swim faster!")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready!")
    def whoisthis(self):
        print("I am a penguin!")
    def run(self):
        print("Run faster!")

a = Penguin()
a.whoisthis()
a.run()
a.swim()