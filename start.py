from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *

desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)

while True:  # Run indefinitely
    for i in range(0, 100):
        PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
        Sleep(1)