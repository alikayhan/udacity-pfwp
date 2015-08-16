#!/usr/bin/env python3

__author__ = 'alikayhan'


class Parent:
    def __init__(self, last_name, eye_color):
        # print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):    # Overriding the parent's method
        print("Last name: " + self.last_name)
        print("Eye color: " + self.eye_color)
        print("Number of toys: " + str(self.number_of_toys))


jim_elliot = Parent("Elliot", "blue")
billy_elliot = Child("Elliot", "blue", "13")
# print(billy_elliot.eye_color, billy_elliot.last_name, billy_elliot.number_of_toys)

jim_elliot.show_info()
print("\n")
billy_elliot.show_info()

