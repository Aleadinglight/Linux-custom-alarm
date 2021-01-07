# Import python library
from playsound import playsound
import time 
import sys
from pathlib import Path

# Import local module
currentFilePath = Path(__file__).resolve().parents[1]

sys.path.append(str(currentFilePath.joinpath('clocktimer')))
from clocktimer import ClockTimer

sys.path.append(str(currentFilePath.joinpath('timerio')))
from timerio import TimerIO

class Clock: 
    # Python doesn't have function overloading
    def __init__(self, name = None): 
        if name:
            self.name = name
        else:
            self.name = "Everyday Assistant"
        self.timerIO = TimerIO()
        self.timerIO.loadTimerList()
        self.timer_list = self.timerIO.getTimerList()
        
    def run(self):
        
        while (True):
            # Get current time in local machine
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"{self.name}: {current_time}")  
            
            # This logic need to be fix with something smarter
            for timer in self.timer_list:
                print(f"Compare to: {timer['time']}")
                if (current_time == timer['time']):
                    self.trigger_alarm()
                    
            time.sleep(1)
    
    def trigger_alarm(self): 
        print("Ring ring ring! Motherfucker!")
        #playsound("../../resources/sounds/RickandMorty.mp3")
    