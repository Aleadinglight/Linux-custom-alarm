import sys
from pathlib import Path

# Import local module
currentFilePath = Path(__file__).resolve().parents[1]

sys.path.append(str(currentFilePath.joinpath("app","timerio")))
from timerio import TimerIO

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

if __name__ == "__main__":
    testTimerIO()