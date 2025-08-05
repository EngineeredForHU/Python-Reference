# This file will showcase a few examples of inheritance

# Will first create a class called 'device' that reads in a device
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f'Device: {self.name}, Connected by:({self.connected_by})'

    def disconnect(self):
        self.connected = False
        print('Disconnected.')



# Now we will showcase how inheritance works
# It's important to notice how super() is being used here
# Instead of defining another init we can inherit what we need from the parent function 'Device' class with super().__init__(VAR1,..)
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # Using super().init() to inherit 'name', 'connected_by' from the parent class 'Device'
        super().__init__(name, connected_by)
        # There is a reason why we are assigning capacity twice here, 'capacity' is used to keep track of the total and 'remaining_pages' is current capacity
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f'{super().__str__()} ({self.remaining_pages} pages remaining)'

    def print_using_printer(self,pages):
        if not self.connected:
            print('your printer is not connected')
            return
        print(f'printing {pages} pages')
        self.remaining_pages -= pages


# Created an object called printer with the Printer class
printer = Printer('Printer','USB',500)
# here we are printing using the printer and printing 20 pages
printer.print_using_printer(20)
print(printer)