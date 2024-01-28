from tkinter import *
from tkinter import ttk

from gui.custom_widgets.text_frame import TextFrame
from gui.custom_widgets.results_frame import ResultsFrame
from gui.custom_widgets.options_frame import OptionsFrame


class MainWindow:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title('Typing Speed Test')
        self.root.iconbitmap('gui/keyboard_icon.ico')
        self.root.resizable(FALSE, FALSE)

        self.timer = None
        self.options = None

        mainframe = ttk.Frame(self.root)
        mainframe.grid(column=0, row=0, sticky='nwes')
        button_frame = ttk.Frame(mainframe)
        button_frame.grid(column=0, row=0, pady=(15, 15))
        test_frame = ttk.Frame(mainframe, borderwidth=5, relief='ridge')
        test_frame.grid(column=0, row=1, padx=50, pady=(0, 50), sticky='nwes')

        self.options_frame = OptionsFrame(test_frame)
        self.text_frame = TextFrame(test_frame, width=80, height=10, wrap='word', takefocus=0)
        self.text_scrollbar = ttk.Scrollbar(test_frame,
                                            orient='vertical',
                                            command=self.text_frame.yview)
        self.text_frame.configure(yscrollcommand=self.text_scrollbar.set)
        self.results_frame = ResultsFrame(test_frame)

        self.start_button = ttk.Button(button_frame, text='Generate Text', command=self.apply_options)
        self.stop_button = ttk.Button(button_frame, text='Stop Test', command=self.show_test_results)
        self.restart_test_button = ttk.Button(button_frame, text='Restart Test', command=self.restart_test)
        self.timer_string = StringVar(value='Type to Begin!')
        self.timer_label = ttk.Label(button_frame, textvariable=self.timer_string)

        self.options_view()

    def options_view(self):
        self.restart_test_button.grid_forget()
        self.stop_button.grid_forget()
        self.results_frame.grid_forget()
        self.text_frame.grid_forget()
        self.timer_label.grid_forget()
        self.start_button.configure(state='normal')

        self.start_button.grid(column=0, row=0)
        self.options_frame.grid(column=0, row=0)

    def text_view(self):
        self.start_button.configure(state='disabled')
        self.start_button.grid_forget()
        self.options_frame.grid_forget()

        self.restart_test_button.grid(column=2, row=0, padx=20)
        self.timer_label.grid(column=0, row=0, padx=20)
        self.text_frame.grid(column=0, row=0)
        self.text_scrollbar.grid(column=1, row=0, sticky='ns')
        if self.is_marathon_mode():
            self.stop_button.grid(column=1, row=0, padx=20)

    def results_view(self):
        self.timer_label.grid_forget()
        self.text_frame.grid_forget()
        self.text_scrollbar.grid_forget()
        self.stop_button.grid_forget()

        self.results_frame.grid(column=0, row=0)

    def is_marathon_mode(self):
        return self.options['time_limit'] is None

    def restart_test(self):
        self.stop_test()
        self.options_view()

    def stop_test(self):
        if self.timer_is_running():
            self.cancel_timer()
        self.timer = None
        self.stop_keyboard_input()
        self.text_frame.clear_text()
        self.text_frame.clear_counts()

    def show_test_results(self):
        test_data = self.get_test_data()
        self.stop_test()
        self.results_view()
        self.results_frame.show_results(test_data)

    def get_test_data(self):
        test_data = self.text_frame.get_test_data()
        minutes = self.get_timer_value()
        test_data['minutes'] = minutes
        test_data['mode'] = self.options['mode']
        return test_data

    def get_timer_value(self):
        if self.is_marathon_mode():
            minutes = self.get_marathon_time()
        else:
            minutes = self.options['time_limit']
        return minutes

    def get_marathon_time(self):
        timer_string = self.timer_string.get()
        minutes, seconds = timer_string.split(':')
        second_decimal_value = int(seconds) / 60
        minutes = int(minutes) + second_decimal_value
        return minutes

    def stop_keyboard_input(self):
        self.root.unbind('<Key>')

    def timer_is_running(self):
        return bool(self.timer)

    def cancel_timer(self):
        self.root.after_cancel(self.timer)

    def start_timer(self):
        time_limit = self.options['time_limit']
        if time_limit:
            timer_in_seconds = time_limit * 60
            self.count_down(timer_in_seconds)
        else:
            self.count_up(0)

    def count_down(self, count):
        self.set_timer_label(count)
        if count > 0:
            self.timer = self.root.after(1000, self.count_down, count-1)
        else:
            self.timer = None
            self.show_test_results()

    def count_up(self, count):
        self.set_timer_label(count)
        self.timer = self.root.after(1000, self.count_up, count+1)

    def set_timer_label(self, count):
        timer_minutes = count // 60
        timer_seconds = count % 60
        if timer_seconds < 10:
            timer_seconds = f'0{timer_seconds}'
        self.timer_string.set(f'{timer_minutes}:{timer_seconds}')

    def on_key_press(self, event):
        if not self.timer:
            self.start_timer()
        self.text_frame.process_keyboard_input(event)

    def clear_timer_label(self):
        self.timer_string.set(value='Type to Begin!')

    def apply_options(self):
        self.options = self.options_frame.get_options()
        self.text_frame.set_options(self.options['mode'], self.options['backspace'])
        self.text_frame.add_text()
        self.text_frame.configure(state='disabled')
        self.clear_timer_label()

        self.root.bind('<Key>', self.on_key_press)
        self.text_view()
