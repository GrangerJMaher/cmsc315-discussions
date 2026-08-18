"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy

# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class RocketEngine:
    # Class variable: shared by all RocketEngine objects
    engine_count = 0

    def __init__(self, name, dry_mass):
        # Instance variables: separate values for each object
        self.name = name
        self.dry_mass = dry_mass

        RocketEngine.engine_count += 1

    def display_information(self):
        print(f"Engine name: {self.name}")
        print(f"Dry mass: {self.dry_mass} kg")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SolidRocketMotor(RocketEngine):
    # Class variable shared by solid motors
    motor_count = 0

    def __init__(
            self,
            name,
            dry_mass,
            propellant_mass,
            burn_time,
            average_thrust
    ):
        # Initialize inherited instance variables
        super().__init__(name, dry_mass)

        # New instance variables
        self.propellant_mass = propellant_mass
        self.burn_time = burn_time
        self.average_thrust = average_thrust

        SolidRocketMotor.motor_count += 1

    # New method
    def calculate_total_impulse(self):
        return self.average_thrust * self.burn_time

    # Override the parent method
    def display_information(self):
        super().display_information()

        print("Engine type: Solid rocket motor")
        print(f"Propellant mass: {self.propellant_mass} kg")
        print(f"Burn time: {self.burn_time} seconds")
        print(f"Average thrust: {self.average_thrust} N")
        print(f"Total impulse: {self.calculate_total_impulse()} N·s")

class LiquidRocketEngine(RocketEngine):
    # Class variable shared by liquid engines
    engine_type = "Liquid rocket engine"

    def __init__(
            self,
            name,
            dry_mass,
            fuel_mass_flow,
            oxidizer_mass_flow,
            effective_exhaust_velocity
    ):
        # Initialize inherited instance variables
        super().__init__(name, dry_mass)

        # New instance variables
        self.fuel_mass_flow = fuel_mass_flow
        self.oxidizer_mass_flow = oxidizer_mass_flow
        self.effective_exhaust_velocity = effective_exhaust_velocity

    # New method
    def calculate_total_mass_flow(self):
        return self.fuel_mass_flow + self.oxidizer_mass_flow

    # Another new method
    def calculate_thrust(self):
        total_mass_flow = self.calculate_total_mass_flow()
        return total_mass_flow * self.effective_exhaust_velocity

    # Override the parent method
    def display_information(self):
        super().display_information()

        print(f"Engine type: {LiquidRocketEngine.engine_type}")
        print(f"Fuel mass-flow rate: {self.fuel_mass_flow} kg/s")
        print(
            f"Oxidizer mass-flow rate: "
            f"{self.oxidizer_mass_flow} kg/s"
        )
        print(
            f"Total mass-flow rate: "
            f"{self.calculate_total_mass_flow()} kg/s"
        )
        print(
            f"Effective exhaust velocity: "
            f"{self.effective_exhaust_velocity} m/s"
        )
        print(f"Thrust: {self.calculate_thrust()} N")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    # Create two objects of the same child class
    motor_1 = SolidRocketMotor(
        name="AstroJays O-Class Motor",
        dry_mass=15,
        propellant_mass=35,
        burn_time=7,
        average_thrust=5000
    )

    motor_2 = SolidRocketMotor(
        name="AstroJays M-Class Motor",
        dry_mass=8,
        propellant_mass=12,
        burn_time=5,
        average_thrust=2000
    )

    # Access the class variable through the class
    print("Accessing motor_count through the class:")
    print(SolidRocketMotor.motor_count)

    # Access the same class variable through an object
    print("\nAccessing motor_count through motor_1:")
    print(motor_1.motor_count)

    # Add a new attribute only to motor_1
    motor_1.test_status = "Static fire completed"

    # Display each object's instance namespace
    print("\nmotor_1 instance namespace:")
    print(motor_1.__dict__)

    print("\nmotor_2 instance namespace:")
    print(motor_2.__dict__)

    # Display the class namespace
    print("\nSolidRocketMotor class namespace:")
    print(SolidRocketMotor.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    # Create an object.
    original_motor = SolidRocketMotor(
        name="AstroJays O-class Motor",
        dry_mass=15,
        propellant_mass=35,
        burn_time=7,
        average_thrust=5000
    )

    # Add nested mutable data to the original object.
    # test_history is a list containing dictionaries.
    setattr(
        original_motor,
        "test_history",
        [
            {
                "test_type": "Hydrostatic test",
                "status": "Passed"
            },
            {
                "test_type": "Static fire",
                "status": "Pending"
            }
        ]
    )

    # A shallow copy creates a new motor object, but its nested
    # test_history list reference is shared with the original motor.
    shallow_motor = copy(original_motor)

    # A deep copy creates a new motor object and recursively copies
    # the nested test_history list and the dictionaries inside it.
    deep_motor = deepcopy(original_motor)

    # Modify a dictionary inside the original motor's nested list.
    # The shallow copy will see this change because it shares the
    # same test_history list and dictionaries.
    original_motor.test_history[1]["status"] = "Passed"

    # Add another dictionary to the original motor's nested list.
    # This also appears in the shallow copy, but not the deep copy.
    original_motor.test_history.append(
        {
            "test_type": "Flight test",
            "status": "Scheduled"
        }
    )

    print("\nOriginal motor namespace:")
    print(original_motor.__dict__)

    print("\nShallow-copy namespace:")
    print(shallow_motor.__dict__)

    print("\nDeep-copy namespace:")
    print(deep_motor.__dict__)

    print("\nIdentity comparisons:")

    print(
        "Original and shallow objects are the same:",
        original_motor is shallow_motor
    )

    print(
        "Original and shallow test histories are the same:",
        original_motor.test_history is shallow_motor.test_history
    )

    print(
        "Original and deep objects are the same:",
        original_motor is deep_motor
    )

    print(
        "Original and deep test histories are the same:",
        original_motor.test_history is deep_motor.test_history
    )



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    # Create an object directly from the parent class.
    generic_engine = RocketEngine(
        name="Generic Rocket Engine",
        dry_mass=100
    )

    # Call a method defined in the parent class.
    generic_engine.display_information()

    print("\nTODO: Create and test your child object: Solid Motor")

    # Create an object from the SolidRocketMotor child class.
    solid_motor = SolidRocketMotor(
        name="AstroJays O-Class Motor",
        dry_mass=15,
        propellant_mass=35,
        burn_time=7,
        average_thrust=5000
    )

    # This calls the overridden display_information() method.
    # That method also calls the inherited parent implementation
    # using super().display_information().
    solid_motor.display_information()

    # Call a method defined specifically by the child class.
    print(
        "Calculated total impulse:",
        solid_motor.calculate_total_impulse(),
        "N·s"
    )

    print("\nTODO: Create and test your child object: Liquid Motor")
    # Create an object from the LiquidRocketEngine child class.
    liquid_engine = LiquidRocketEngine(
        name="Liquid Demonstrator",
        dry_mass=30,
        fuel_mass_flow=1.0,
        oxidizer_mass_flow=2.0,
        effective_exhaust_velocity=2200
    )

    # Call the overridden child method.
    liquid_engine.display_information()

    # Call methods defined specifically in the liquid child class.
    print(
        "Calculated total mass flow:",
        liquid_engine.calculate_total_mass_flow(),
        "kg/s"
    )

    print(
        "Calculated thrust:",
        liquid_engine.calculate_thrust(),
        "N"
    )

    # Call the namespace demonstration function
    demonstrate_namespaces()

    # Call the shallow-copy and deep-copy demonstration function
    demonstrate_copying()


if __name__ == "__main__":
    main()