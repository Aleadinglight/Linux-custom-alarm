import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog= "alarm",
        description="This program is a home assistant alarm clock, \
        you can choose the clock sound and personal message.")

    parser.add_argument("-a", 
                        "--add-new-timer",
                        help="Add a new timer to the clock",
                        dest="timer")
    
    # Get the arguments from the user
    args = parser.parse_args()
    
    # Processing the arguments
    if args.command == True:
        print("Run clock")
