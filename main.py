class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print('Starting engine...')
        self.engine_on = True

    def make_noise(self):
        print('Beep Beep')

    def get_info(self):
        return f'Make: {self.make}, Miles: {self.miles}, Price: {self.price}'

class Truck(Vehicle):
    def __init__(self, make, miles, price):
        super().__init__(make, miles, price)
        self.cargo = False

    def load_cargo(self):
        print('Loading the truck bed...')
        self.cargo = True

class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print('Vroom Vroom')

    def get_info(self):
        return f'Make: {self.make}, Miles: {self.miles}, Price: {self.price}, Top Speed: {self.top_speed}'

# List of Vehicles
motorcycles = [
    Motorcycle('Kawasaki', 2100, 12000, 110),
    Motorcycle('Harley Davidson', 5000, 15000, 120),
    Motorcycle('Ducati', 3000, 20000, 140)
]

trucks = [
    Truck('Toyota', 40000, 32000),
    Truck('Ford', 30000, 28000),
    Truck('Chevy', 35000, 29000)
]

vehicles_to_compare = []

# User interaction
print('Hello! Welcome to GC Bikes and Trucks!')
# bikes or trucks
while True:
    vehicle_selection = input('Would you like to view bikes or trucks? (b or t): ').lower()
    if vehicle_selection in ['b', 't']:
        if vehicle_selection == 'b':
            for i, motorcycle in enumerate(motorcycles, 1):
                print(f'{i}. {motorcycle.get_info()}')
        elif vehicle_selection == 't':
            for i, truck in enumerate(trucks, 1):
                print(f'{i}. {truck.get_info()}')
    else:
        print('Invalid input. Please enter b for bikes or t for trucks.')
        continue
# adding a vehicle to the list
    while True:
        add_vehicle = input('Would you like to add a vehicle to compare? (y or n): ').lower()
        if add_vehicle == 'y':
            if vehicle_selection == 'b':
                choice = int(input('Which vehicle would you like to compare? (please list number): ')) - 1
                if 0 <= choice < len(motorcycles):
                    vehicles_to_compare.append(motorcycles[choice])
                    print(f'{motorcycles[choice].get_info()} has been added to the comparison list.')
                else:
                    print('Invalid choice.')
            elif vehicle_selection == 't':
                choice = int(input('Which vehicle would you like to compare? (please list number): ')) - 1
                if 0 <= choice < len(trucks):
                    vehicles_to_compare.append(trucks[choice])
                    print(f'{trucks[choice].get_info()} has been added to the comparison list.')
                else:
                    print('Invalid choice.')
        elif add_vehicle == 'n':
            compare_now = input('Would you like to compare your vehicles now? (y or n): ').lower()
            if compare_now == 'y':
                break
            else:
                break  # Exiting loop to ask for vehicle selection again
        else:
            print('Invalid input. Please enter y or n.')

    if compare_now == 'y':
        break
# could probably combine the code above to be more concise?

if vehicles_to_compare:
    print('\nHere are your vehicles to compare:')
    for vehicle in vehicles_to_compare:
        print(vehicle.get_info())
        vehicle.make_noise()
else:
    print('No vehicles were selected for comparison.')

print('Goodbye! Thank you for visiting GC Bikes and Trucks.')