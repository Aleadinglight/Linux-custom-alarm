from pathlib import Path

class TimerIO:
    def __init__(self, timer_directory=None):
        if (timer_directory != None):
            self.timer_directory = timer_directory
        else:
            self.timer_directory = Path(__file__).resolve().parents[2].joinpath("resources","timers")
        
        self.timer_file_name = "timers.json"
            
    def getTimerList(self):
        print(1)
    
    def saveToFile(self, entry):
        print("Save to")
    
    def getTimerDirectory(self):
        return str(self.timer_directory)
    
    def getTimerFileName(self):
        return self.timer_file_name
    
    def getTimerFilePath(self):
        return self.timer_directory.joinpath(self.getTimerFileName())
    
    def append(self, entry):
        print(1)
    
    def delete(self, id):
        print(2)
        