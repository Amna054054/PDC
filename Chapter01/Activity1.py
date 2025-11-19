import time

print("Task 1: Starting")
time.sleep(2)   # wait 2 seconds
print("Task 1: Done")

print("Task 2: Starting")
time.sleep(2)   # wait 2 seconds
print("Task 2: Done")

# Now we are applying threads to our code!

import time
import threading

def task(name):
    print(f"{name} Starting")
    time.sleep(2)
    print(f"{name} Done")

# create two threads
t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))

# start both at the same time
t1.start()
t2.start()

# wait until both finish
t1.join()
t2.join()

print("All tasks finished!")


