import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog= "alarm",
        description="This program is a home assistant alarm clock, \
        you can choose the clock sound and personal message.")

    parser.add_argument("-a", 
                        "--add-timer",
                        help="add a new timer to the clock",
                        action="store",
                        metavar=("<timer>","<alarm-sound>"),
                        dest="timer",
                        nargs=2)
    
    # Get the arguments from the user
    args = parser.parse_args()
    
    # Processing the arguments
    print(args)
