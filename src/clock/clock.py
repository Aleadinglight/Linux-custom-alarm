import time 

class Clock: 
    # Python doesn't have function overloading
    def __init__(self, name, timer_list = None): 
        self.name = name
        self.timer_list = [] if timer_list is None else timer_list
    
    def run(self):
        while (True):
            # Get current time in local machine
            current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
            print(f'{self.name}: {current_time}')  
            
            # This logic need to be fix with something smarter
            for timer in timer_list:
                if (current_time == timer):
                    self.trigger_alarm()
                    
            time.sleep(1)
    
    def trigger_alarm(): 
        print("Ring ring ring! Motherfucker!")

if __name__ == "__main__":
    new_clock = Clock("Clock 1")
    new_clock.run()
    