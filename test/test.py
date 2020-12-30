import sys
from pathlib import Path

# Import local module
currentFilePath = Path(__file__).resolve().parents[1]

sys.path.append(str(currentFilePath.joinpath("app","timerio")))
from timerio import TimerIO

def testTimerIO():
    print("test timer io")