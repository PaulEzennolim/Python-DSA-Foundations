# Defines a Human class with initializer, string representations, and age comparison logic.
class Human:
  '''
  This is a class that represents a simplified Human.

  It takes their age as an int, and their name as a str.
  '''
  def __init__(self, age, name):
    self._age = age
    self._name = name

  def __str__(self):
    return "A human with name " + self._name + "." + " Their age is " + str(self._age) + "."

  def older_younger_than(self, age):
    if self._age > age:
      print("Our age is bigger than their age.")
    elif self._age == age:
      print("Our age is equal to their age.")
    else:
      print("Our age is less than their age.")

h = Human(age=20, name="Paul")

print(h)