# a class is a blueprint. an object is the actual instance created from taht blueprint
# __init__ -> is the initialisation method. Python automatically calls it when you create a new object.
# self -> current object
# Python uses naming conventions such as _battery and name mangling with __battery to indicate or restrict access.


class Robot:

    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def move(self):
        print(self.name, "is moving!")

    def check_battery(self):
        print("Battery:", self.battery)


robot1 = Robot("Scout", 90)

robot1.move()
robot1.check_battery()


# ---------------------------------------------------------
class Robot:

    def __init__(self, battery):
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)


robot = Robot(50)

robot.charge(20)

print(robot.battery)

# -------------------------------
class Robot:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("I am", self.name)


class DeliveryRobot(Robot):

    def deliver(self):
        print("Delivering package!")


robot = DeliveryRobot("Scout")

robot.introduce()
robot.deliver()

# ----------------------------
# Task:

class Robot:

  def __init__(self, name, battery):
    self.name = name
    self.battery = battery
  
  def introduce(self):
    print("I am", self.name)
  
  def move(self):
    if self.battery < 10:
      print("Insufficient battery!")
    else:
      print(self.name, "is moving")
      self.battery -= 10
  
  def check_battery(self):
    print("Battery:", self.battery)

  def charge(self, amount):
    if self.battery + amount > 100:
      self.battery = 100
    else:
      self.battery += amount
    print("Battery:", self.battery)

robot = Robot("Scout", 90)
robot.introduce()
robot.move()
robot.check_battery()
robot.charge(30)
  

