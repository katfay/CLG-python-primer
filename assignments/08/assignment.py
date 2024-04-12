# Add a default argument for install_app method.
# Modify install_app method to avoid duplicates in app_list.
# Add a delete_app method which takes in one parameter: the name of the app you would like to delete.
# Create a SmartDevice object and use it to call the functions. 
# Use print statements to check if both methods work as you expect them to.

class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=[]):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name, version_number=[]):
        print(f"Installing {app_name}...")
        if app_name not in self.app_list:
            self.app_list.append(app_name)
            print(f"Installing {app_name}...")
        else:
            print(f"{app_name} is already installed")
        return self.app_list
    
    def delete_app(self, app_name):
        print(f"Deleting {app_name}...")
        if app_name not in self.app_list:
            print(f"{app_name} can't be deleted because it is not installed...")
        else:
            self.app_list.remove(app_name)
            print(f"{app_name} was deleted...")
        return self.app_list
    
    def app_report(self):
        if len(self.app_list) > 0:
            print(str(self.model_number) + f" has the following apps installed:")
            print(self.app_list)
        else:
            print(str(self.model_number) + f" has no  apps installed yet...")

device_a = SmartDevice(1233244, 'CLG', 5.7)
device_a.report()

device_a.install_app('food app')
device_a.install_app('tv app')
device_a.install_app('food app')
print(device_a.app_list)
device_a.delete_app('food app')
device_a.delete_app('yoga app')
device_a.install_app('podcast app')
device_a.app_report()

device_b = SmartDevice(42077413, 'Kat', 3.2)
device_b.report()
device_b.app_report()
print(device_b.app_list)



