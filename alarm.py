import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program is a custom alarm clock where you can choose the clock sound and personal message.")
    parser.add_argument("run", dest="command", action="store_const", const="delete", help="Start the clock")
