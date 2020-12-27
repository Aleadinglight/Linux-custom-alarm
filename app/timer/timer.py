class Timer:
    # This class acts as a timer entry. It contains the alarm time and the alarm sound
    def __init__(self, hour, minute, second, sound):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.sound = sound