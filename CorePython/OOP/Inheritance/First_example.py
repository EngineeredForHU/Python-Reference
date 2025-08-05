# This file will showcase a few examples of inheritance

# Will first create a class called 'device' that reads in a device
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f'Device {self.name} ({self.connected_by})'

    def disconnect(self):
        self.connected = False
        print('Disconnected.')

# Now we will showcase how inheritance works
# It's important to notice how super() is being used here
# Instead of defining another init we can inherit what we need from the Device class with super().__init__(VAR1,..)

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        # There is a reason why we are assigning capacity twice here, 'capacity' is used to keep track of the total and 'remaining_pages' is current capacity
        self.capacity = capacity
        self.remaining_pages = capacity