import webbrowser
import time
import random
import ctypes


ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
while True:
    sites = random.choice(['google.com', 'bing.com', 'yahoo.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    delay = random.randrange(10,20)
    time.sleep(delay)
