import argparse
import sys
from pathlib import Path

# Import local module
currentFilePath = Path(__file__).resolve().parents[0].joinpath("app")

sys.path.append(str(currentFilePath.joinpath("clocktimer")))
from clocktimer import ClockTimer

sys.path.append(str(currentFilePath.joinpath("timerio")))
from timerio import TimerIO

def add_timer(timer_entry_raw):
    # Create timer entry json object from raw data
    timer_entry_json = {
        "name": timer_entry_raw[0],
        "time": timer_entry_raw[1],
        "sound_id": timer_entry_raw[2],
    }
    
    # Load timer list
    timerIO = TimerIO()
    timerIO.loadTimerList()
    # Append timer entry to timer list and save
    timerIO.append(timer_entry_json)
    timerIO.saveToFile()
    
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog= "alarm",
        description="This program is a home assistant alarm clock, \
        you can choose the clock sound and personal message.")

    parser.add_argument(
        "-a", 
        "--add-timer",
        help="add a new timer to the clock",
        action="store",
        metavar=("<name>","<timer>","<alarm-sound>"),
        dest="timer",
        nargs=3
    )
    
    parser.add_argument(
        "-r", 
        "--remove-timer",
        help="remove a new timer from the clock",
        action="store",
        metavar=("<timer-id>"),
        dest="remove_timer_id"
    )
    
    parser.add_argument(
        "-t", 
        "--timer-list",
        help="display all timers from the list",
        action="store_true",
        dest="show_timer_list"
    )
    
    # Get the arguments from the user
    args = parser.parse_args()
    
    # Processing the arguments
    if (args.timer):
        add_timer(args.timer)
    elif (args.remove_timer_id):
        print("remove timer")
    elif  (args.show_timer_list):
        print("display timer list")
