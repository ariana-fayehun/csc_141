# I followed the examples in the text to figure out how to complete this 
# assignment

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make               # Store the car's make (e.g., Toyota)
        self.model = model             # Store the car's model (e.g., Camry)
        self.year = year               # Store the car's manufacturing year
        self.odometer_reading = 0      # Initialize the odometer at 0 miles

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()       # Return the formatted car description

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer to a given value.
        Reject changes that attempt to roll back the odometer."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage   # Set to new mileage if valid
        else:
            print("You can't roll back an odometer!")  # Prevent rollback

    def increment_odometer(self, miles):
        """Add the given miles to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attribute with a default size."""
        self.battery_size = battery_size  # Set the battery size in kWh

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        """Upgrade the battery to 65 kWh if it's not already set to that."""
        if self.battery_size != 65:
            self.battery_size = 65  # Upgrade to 65 kWh


class ElectricCar(Car):
    """Represents aspects of a car specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)  # Initialize parent attributes
        self.battery = Battery()             # Attach a Battery instance


# Create an instance of ElectricCar with specific make, model, and year
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# Print the car's descriptive name
print(my_leaf.get_descriptive_name())

# Describe the car's battery
my_leaf.battery.describe_battery()

# Print the range of the car based on the current battery size
my_leaf.battery.get_range()

# Upgrade the battery and print the range again with the upgraded battery
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
