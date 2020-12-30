# Import python library
from playsound import playsound
import time 
import sys
from os.path import dirname, join, abspath
from pathlib import Path

# Import local module
a= Path(__file__).resolve().parents[1].joinpath('clocktimer')
print(a)
#sys.path.append(join(dirname(sys.path[0]),'clocktimer'))
sys.path.append(str(a))
from clocktimer import ClockTimer

sys.path.append(join(dirname(sys.path[0]),'timerio'))
import timerio

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
    print("aSD")
    