from pathlib import Path
import json

class TimerIO:
    def __init__(self, timer_directory=None):
        if (timer_directory != None):
            self.timer_directory = timer_directory
        else:
            self.timer_directory = Path(__file__).resolve().parents[2].joinpath("resources", "timers")

        self.timer_file_name = "timers.json"
        self.timer_list = None

    def loadTimerList(self):
        file_path = self.getTimerFilePath()
        try:
            print("Loading timers from files...")
            file_reader = open(file_path, 'r')
            self.timer_list = file_reader.read()
        except:
            print("Timer saved file doesn't exist, created one...")
            file = open(file_path, 'w+')
        finally:
            file.close()

    def saveToFile(self):
        data = {
            'name': 'Bob',
            'age': 12,
            'children': None
        }
        file_path = self.getTimerFilePath()
        try:
            file = open(file_path, 'w+')
            json.dump(data, file)
        except:
            print("Error!! Failed to save data to file!!")
        finally:
            file.close()
            

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
