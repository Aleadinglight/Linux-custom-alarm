import sys
from pathlib import Path

# Import local module
currentFilePath = Path(__file__).resolve().parents[1]

sys.path.append(str(currentFilePath.joinpath("app","timerio")))
from timerio import TimerIO

sys.path.append(str(currentFilePath.joinpath("app","downloader")))
from downloader import Downloader

sys.path.append(str(currentFilePath.joinpath("app","clock")))
from clock import Clock

# Modules

def testTimerIO():
    timerIO = TimerIO() 
    print("-----Testing-for-TimerIO------\n")
    
    print(f"File path: {timerIO.getTimerFilePath()}")
    
    timerIO.loadTimerList()
    print(f"Timer list: {timerIO.getTimerList()}")
    timerIO.saveToFile()
    
    sound_list = timerIO.getSoundList()
    for index, sound in enumerate(sound_list):
        print(f"[{index}] {sound}")
    
    print("\n------------------------------\n")

def testDownloader():
    new_downloader = Downloader()
    print(f"Number of sound files: {new_downloader.calculateSoundFile()}")
    new_downloader.download('https://www.youtube.com/watch?v=AwSra5p8MDw&ab_channel=ArthurZee024', 'GoodMorningVietName')
    
def testClock():
    new_clock = Clock()
    new_clock.alarm_async("1")
    new_clock.alarm_async("1")
    
if __name__ == "__main__":
    testClock()