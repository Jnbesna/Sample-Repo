import math
import sys
from os import rename

import request

# print(sys.executable)
# print(sys.version)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Besna"))

# r = request.GET("www.google.ca")
# print(r.status_code)

# name = input("Your name? ")
# print("Hello,", name)
