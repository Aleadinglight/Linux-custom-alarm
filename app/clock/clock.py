# Import python library
from playsound import playsound
import time 
import sys
import threading
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
        # Add name to clock
        if name:
            self.name = name
        else:
            self.name = "Everyday Assistant"
        # Initiate timer list
        self.timerIO = TimerIO()
        self.timerIO.loadTimerList()
        self.timer_list = self.timerIO.getTimerList()
        # Initiate audio list
        self.timerIO.loadSoundList()
        self.audio_list = self.timerIO.getSoundList()
        self.audio_directory = self.timerIO.getSoundDirectory()
        
    def run(self):
        
        while (True):
            # Get current time in local machine
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"{self.name}: {current_time}")  
            
            # This logic need to be fix with something smarter
            for timer in self.timer_list:
                if (current_time == timer['time']):
                    self.trigger_alarm(timer['sound_id'])
                    break
                   
            time.sleep(1)
    
    def trigger_alarm(self, sound_id):
        # Init thread
        self.alarm_thread = threading.Thread(target=self.alarm_async, args=(sound_id))
        # Start thread
        self.alarm_thread.start() 
        
    def alarm_async(self, input_audio_id): 
        print("Ring ring ring!")        
        for audio_file in self.audio_list:
            audio_id = audio_file.split('_', 1)[0]
            if (audio_id == input_audio_id):
                audio_path = str(Path(self.audio_directory).joinpath(audio_file))
                playsound(audio_path)
    