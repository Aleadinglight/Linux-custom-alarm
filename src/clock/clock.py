import time 

class Clock: 
    def __init__(self, name, ): 
        self.name = name
    
    def run(self):
        while (True):
            # Get current time in local machine
            current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
            print(f'{self.name}: {current_time}')  
            
            time.sleep(1)

if __name__ == "__main__":
    new_clock = Clock("Clock 1")
    new_clock.run()
    