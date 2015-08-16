import webbrowser
import time

start_time = time.ctime()
print ("Program started at: " + start_time)
break_count = 0

while break_count < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=euiKqmLvyMw")
    break_count += 1
