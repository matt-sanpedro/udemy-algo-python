# inheritance: allows on class to take methods and properties from another class

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        # !r calls the __repr__ method of self.name (shows the quotes)
        return f"{self.name!r} connected by ({self.connected_by})"
    
    def disconnect(self):
        self.connected = False
        print("Disconnected")

web_cam = Device("Web cam", "USB")
print(web_cam)
web_cam.disconnect()
print(web_cam.connected)

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # get the super class (Device), aka the parent class, call the __init_ method
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining = capacity

    def __str__(self):
        # call the __str__ method of the parent class (Device), then add remaining pages
        return f"{super().__str__()} ({self.remaining} pages remaining)"
    
    def print(self, pages):
        if not self.connected:
            print("Printer is not connected")
            return
        if pages > self.remaining:
            print(f"Cannot print {pages} pages, only {self.remaining} remaining")
            return
        self.remaining -= pages
        print(f"Printed {pages} pages")

printer = Printer("Printer", "USB", 500)
print(printer)
printer.print(100)
printer.print(401)
printer.disconnect()
printer.print(100)
