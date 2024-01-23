from tkinter import *


class Timer:
    def __init__(self, root: Tk):
        self.root = root
        self.timer = None

    def timer_is_running(self):
        return bool(self.timer)

    def stop_timer(self):
        self.root.after_cancel(self.timer)

    def reset_timer(self):
        self.timer = None

    def start_timer(self, time_limit, label_function):
        if time_limit:
            timer_in_seconds = time_limit * 60
            self.count_down(timer_in_seconds, label_function)
        # else:
        #     self.count_up(0)

    def count_down(self, count, label_function):
        label_function(count)
        if count > 0:
            self.timer = self.root.after(1000, self.count_down, count-1, label_function)
        # else:
        #     self.timer_label.configure(text="Time's Up!")
        #     self.timer = None
        #     self.stop_test()