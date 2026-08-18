# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation

I created a RocketEngine parent class that represented a basic rocket engine and included the engine_count class variable, instance variables for the engine's name and dry mass, a constructor, and a method for displaying engine information. The engine_count variable was incremented whenever the parent constructor was called including when an object of a child class was created.

I created a SolidRocketMotor child class that inherited from RocketEngine. The child class added the motor_count class variable and instance variables for propellant mass, burn time, and average thrust. I used super() to call the parent constructor and reuse the name and dry mass attributes. I also overrode the display_information() method and created a calculate_total_impulse() method that multiplied average thrust by burn time.

I demonstrated class and instance namespaces by creating two SolidRocketMotor objects, accessing motor_count through both the SolidRocketMotor class and an individual motor object, and adding a test_status attribute to only one object after it was created. I displayed each object's instance namespace and the child class namespace using __dict__. This showed that the dynamically added attribute belonged only to the selected object, while the class variable and method definitions belonged to the class namespace.

I demonstrated shallow and deep copying using Python's copy() and deepcopy() functions. I added a nested test_history list containing dictionaries to the original motor object. After modifying a dictionary and adding another test record to the original list, the shallow copy reflected both modifications because it shared the same nested list. The deep copy remained unchanged because it contained an independent copy of the nested mutable data.

As my student created extension I added a LiquidRocketEngine child class. This class inherited the common name and dry-mass attributes from RocketEngine and added fuel mass flow, oxidizer mass flow, and effective exhaust velocity. I created methods to calculate total propellant mass flow and approximate thrust, and I overrode display_information() to include the liquid-engine-specific information and calculated results.

Finally I completed the main() function by creating objects from the parent and child classes, calling inherited, overridden, and child-specific methods, and running the namespace and copying demonstrations. I used the if __name__ == "__main__": guard so that main() runs only when the file is executed directly.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

### Design Approach

I designed the program around a RocketEngine parent class containing information shared by all engines, including the engine name and dry mass. The SolidRocketMotor and LiquidRocketEngine child classes inherited those attributes and added data and calculations specific to each propulsion system.

### 1. What concepts or skills did you learn while completing this assignment?

I developed a better understanding of inheritance, namespaces, method overriding, and shallow versus deep copying. It was my first time using Python’s copy() and deepcopy() functions. Copying could be useful when comparing multiple versions of a rocket-engine model. A baseline engine could be copied before changing its thrust, mass, or test-history data. A deep copy would preserve an independent baseline, while a shallow copy could intentionally share common nested data.

### 2. What challenges did you encounter, and how did you overcome them?

My greatest challenge was determining which information belonged in the parent class and which belonged in each child class. Initially it was tempting to place propulsion specific attributes in RocketEngine. I resolved this by asking whether every type of engine logically possessed each attribute. Name and dry mass belonged in the parent while propellant mass and burn time belonged to the solid motor and separate mass flow rates belonged to the liquid engine.

### 3. Compare OOP to procedural programming.

Procedural programming organizes a program around a sequence of functions and operations, while OOP organizes related data and behavior into objects. This approach allowed the engine classes to remain distinct while sharing common functionality through inheritance. It also improved modularity because each class had a clearly defined responsibility. OOP further supports encapsulation and abstraction. For example, a user of the SolidRocketMotor or LiquidRocketEngine class can calculate total impulse or thrust by calling the appropriate method without needing to understand the internal equations or how the object’s attributes are used in the calculation.

### 4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

OOP requires additional planning and creates some overhead so it may be excessive for a very small script. However that overhead becomes beneficial as an application grows. The RocketEngine class acts as a reusable template allowing new engine types to inherit established attributes and methods instead of duplicating code. If common behavior changes it can be updated once in the parent class. This structure would be useful for larger engineering applications involving multiple propulsion systems, tanks, valves, sensors, or other vehicle subsystems. It improves scalability, reduces duplication, and makes future modifications less likely to introduce inconsistent behavior.

