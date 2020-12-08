import time 

class Clock: 
    def __init__(self, name): 
        self.name = name
    
    def run(self):
        while (True):
            time.sleep(1)
            currentTime = time.time()
            print(f'{self.name}: {currentTime}')  

if __name__ == "__main__":
    newClock = Clock("Clock 1")
    newClock.run()
    