import argparse
import sys
import json
from pathlib import Path

# Import local module
currentFilePath = Path(__file__).resolve().parents[0].joinpath("app")

sys.path.append(str(currentFilePath.joinpath("clocktimer")))
from clocktimer import ClockTimer

sys.path.append(str(currentFilePath.joinpath("timerio")))
from timerio import TimerIO

sys.path.append(str(currentFilePath.joinpath("downloader")))
from downloader import Downloader

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
    print("Successfully added timer to clock...")

def display_timers():
    # Load timer list
    timerIO = TimerIO()
    timerIO.loadTimerList()
    timer_list = timerIO.getTimerList()
    print("\n-------------List of timers----------------")
    for index, timer in enumerate(timer_list):
        print(f"*Timer No.{index}*")
        print(f"Name: {timer['name']}")
        print(f"Time: {timer['time']}\n")

def download_sound(sound_info):
    name = sound_info[0]
    link = sound_info[1]
    new_downloader = Downloader()
    new_downloader.download(name, link)
        

def show_audio():
    # Instantiate a new TimerIO object
    timerIO = TimerIO()
    # Load the available audio files
    timerIO.loadSoundList()
    audio_list = timerIO.getSoundList()
    
    for audio_file in audio_list:
        audio_file_split = audio_file.split("_", 1)
        index = audio_file_split[0]
        name = audio_file_split[1]
        print(f"[{index}] {name}")
    

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
    
    parser.add_argument(
        "-d", 
        "--download-alarm-sound",
        help="download new alarm sound for timer",
        action="store",
        dest="sound_info",
        metavar=("<name>", "<link>"),
        nargs=2
    )
    
    parser.add_argument(
        "-s", 
        "--audio-sound-list",
        help="show available audio files for the alarm",
        action="store_true",
        dest="show_audio"
    )
    
    # Get the arguments from the user
    args = parser.parse_args()

    # Processing the arguments
    if (args.timer):
        add_timer(args.timer)
    elif (args.remove_timer_id):
        print("remove timer")
    elif (args.show_timer_list):
        display_timers() 
    elif (args.sound_info):
        download_sound(args.sound_info)
    elif (args.show_audio):
        show_audio()
    