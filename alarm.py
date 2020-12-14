import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program is a custom alarm clock where you can choose the clock sound and personal message.")
    
    # -t, --add-timer
    # -, --display-timer-list
    # -a, --add-alarm-sound
    # -d, --download-alarm-sound
    # -, --display-alarm-sound-list
    # Get the arguments from the user
    args = parser.parse_args()
    
    # Processing the arguments
    if args.command == True:
        print("Run clock")