import os
from pathlib import Path
import json


class TimerIO:
    def __init__(self, timer_directory=None, sound_directory=None):

        resource_directory = Path(
            __file__).resolve().parents[2].joinpath("resources")
        if (timer_directory != None):
            self.timer_directory = timer_directory
        else:
            self.timer_directory = resource_directory.joinpath("timers")

        if (sound_directory != None):
            self.sound_directory = sound_directory
        else:
            self.sound_directory = resource_directory.joinpath("sounds")

        self.timer_file_name = "timers.json"
        self.timer_list = []
        self.sound_list = []

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

    def append(self, timer_entry):
        if self.timer_list == None:
            self.timer_list = []

        self.timer_list.append(timer_entry)

    def delete(self, id):
        print(2)

    def loadSoundList(self):
        for temp_file in os.listdir(self.getSoundDirectory()):
            if (temp_file.endswith(".mp3")):
                self.sound_list.append(temp_file)

    def getSoundList(self):
        if not self.sound_list:
            self.loadSoundList()
        return self.sound_list

    def getSoundDirectory(self):
        return str(self.sound_directory)
