# Import python library
from playsound import playsound
import time 
import sys
from os.path import dirname, join

# Import local module
sys.path.append(join(dirname(sys.path[0]),'clocktimer'))
from clocktimer import ClockTimer

class Clock: 
    # Python doesn't have function overloading
    def __init__(self, name): 
        self.name = name
        self.timer_list = self.get_timer_list
    
    def run(self):
        while (True):
            # Get current time in local machine
            current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
            print(f'{self.name}: {current_time}')  
            
            # This logic need to be fix with something smarter
            for timer in timer_list:
                if (current_time == timer):
                    self.trigger_alarm()
                    
            time.sleep(1)
    
    def trigger_alarm(self): 
        print("Ring ring ring! Motherfucker!")
        playsound("../../resources/sounds/RickandMorty.mp3")

if __name__ == "__main__":
    new_clock = Clock("Clock 1")
    new_clock.trigger_alarm()
    