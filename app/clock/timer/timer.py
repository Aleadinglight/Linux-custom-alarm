class Timer:
    # This class acts as a timer entry. It contains the alarm time and the alarm sound
    def __init__(self, hour, minute, second, sound):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.sound = sound
    
    # To tring method
    def get_time_as_tring():
        return ""
    
    # Check equal as another time object
    def is_equal(self, another_timer):
        if (another_timer.hour == self.hour and another_timer.minute == self.minute and another_timer.second == self.second):
            return True
        return False
    
    # Check equal as string entry
    