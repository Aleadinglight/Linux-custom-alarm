import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program is a custom alarm clock where you can choose the clock sound and personal message.")
    
    # -t, --timer-list 
    # -, --display-timer-list
    # -a, --add-alarm-sound
    # -d, --download-alarm-sound
    
    # Get the arguments from the user
    args = parser.parse_args()
    
    # Processing the arguments
    if args.command == True:
        print("Run clock")