"""
TV controller

Create a simple prototype of a TV controller in Python.
"""


class TVController:
    def __init__(self, channels):
        self.channels = channels
        temp = dict(zip(range(1, len(self.channels) + 1), self.channels))
        self.dict_channels = temp
        self.position = 1

    def last_channel(self):
        self.position = len(self.channels)
        self.current_channel()

    def turn_channel(self):
        self.position = 1
        self.current_channel()

    def next_channel(self):
        if self.position == len(self.channels):
            self.position = 1
        else:
            self.position += 1
        self.current_channel()

    def previous_channel(self):
        if self.position == 1:
            self.position = len(self.channels)
        else:
            self.position -= 1
        self.current_channel()

    def current_channel(self):
        print(self.dict_channels[self.position])
        return self.dict_channels[self.position]

    def is_exist(self, search_arg):
        if isinstance(search_arg, int):
            if int(search_arg) in self.dict_channels.keys():
                ansver = True
            else:
                ansver = False
        elif search_arg in self.dict_channels.values():
            ansver = True
        else:
            ansver = False

        if ansver:
            print('Yes')
        else:
            print('No')

    def first_channel(self):
        self.position = 1
        self.current_channel()


CHANNELS = ['BBC', 'Discovery', 'TV1000']
controller = TVController(CHANNELS)

controller.first_channel()
controller.last_channel()
controller.turn_channel()
controller.next_channel()
controller.previous_channel()
controller.current_channel()
controller.is_exist(2)
controller.is_exist('TV1000')
