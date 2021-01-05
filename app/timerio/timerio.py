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
            self.timer_list = json.load(file_reader)
        except:
            print("Timer saved file doesn't exist, created one...")
            file_reader = open(file_path, 'w+')
        finally:
            file_reader.close()

    def saveToFile(self):
        data = self.getTimerList()
        file_path = self.getTimerFilePath()
        try:
            file_writer = open(file_path, 'w+')
            json.dump(data, file_writer)
        except Exception as e:
            print(f"Failed to save data to file!!\nError: {e}")
        finally:
            file_writer.close()
            

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
