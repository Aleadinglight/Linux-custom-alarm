from pathlib import Path

class TimerIO:
    def __init__(self, timer_directory=None):
        if (timer_directory != None):
            self.timer_directory = timer_directory
        else:
            self.timer_directory = Path(__file__).resolve().parents[2].joinpath("resources","timers")
        
        self.timer_file_name = "timers.json"
        self.timer_list = None
            
    def loadTimerList(self):
        filePath = self.getTimerFilePath()
        try: 
            print("Loading timers from files...")
            file = open(filePath, 'r')
            self.timer_list = file.read()
        except:
            print("Timer saved file doesn't exist, created one...")
            file = open(filePath, 'w+')
        finally:
            file.close()
    
    def saveToFile(self, entry):
        print("Save to")
    
    def getTimerList(self):
        return self.timer_list
    
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
        