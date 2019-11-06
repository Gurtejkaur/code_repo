class Widget:
    """ Models a manufactured item. """
    serial_number_source = 0 # Class variable
    
    def __init__(self):
        """ Make a widget with a unique serial number. """
        self.serial_number = Widget.serial_number_source
        Widget.serial_number_source += 1
        self.get_serial_number()
        
    def get_serial_number(self):
        """ Return the widget's serial number. """
        #print("{} is stated".format(__name__))
        return self.serial_number
def main():
    widget_list = []
    for i in range(10):
        widget_list.append(Widget())
    for w in widget_list:
        print(w.serial_number, end=' ')
main()        
