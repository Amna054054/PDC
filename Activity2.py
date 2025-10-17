import time
import threading

# --- Locks and Semaphore setup ---
lock = threading.Lock()         # Normal Lock
rlock = threading.RLock()       # Re-entrant Lock
semaphore = threading.Semaphore(2)  # Allows 2 threads at once


def task_with_lock(name):
    """Task using simple Lock"""
    print(f"{name} waiting for Lock...")
    with lock:
        print(f"{name} acquired Lock")
        time.sleep(2)
        print(f"{name} releasing Lock")


def task_with_rlock(name):
    """Task using RLock"""
    print(f"{name} waiting for RLock...")
    with rlock:
        print(f"{name} acquired RLock first time")
        with rlock:  # same thread can acquire it again safely
            print(f"{name} acquired RLock second time")
            time.sleep(2)
        print(f"{name} releasing RLock")


def task_with_semaphore(name):
    """Task using Semaphore"""
    print(f"{name} waiting for Semaphore...")
    with semaphore:
        print(f"{name} acquired Semaphore")
        time.sleep(2)
        print(f"{name} releasing Semaphore")


# --- Run section ---

print("\n===== Using Lock =====")
t1 = threading.Thread(target=task_with_lock, args=("Task 1",))
t2 = threading.Thread(target=task_with_lock, args=("Task 2",))
t3 = threading.Thread(target=task_with_lock, args=("Task 3",))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

print("\n===== Using RLock =====")
r1 = threading.Thread(target=task_with_rlock, args=("Task A",))
r2 = threading.Thread(target=task_with_rlock, args=("Task B",))
r1.start()
r2.start()
r1.join()
r2.join()

print("\n===== Using Semaphore =====")
s1 = threading.Thread(target=task_with_semaphore, args=("Thread 1",))
s2 = threading.Thread(target=task_with_semaphore, args=("Thread 2",))
s3 = threading.Thread(target=task_with_semaphore, args=("Thread 3",))
s4 = threading.Thread(target=task_with_semaphore, args=("Thread 4",))
s1.start()
s2.start()
s3.start()
s4.start()
s1.join()
s2.join()
s3.join()
s4.join()

print("\nAll threads completed successfully!")
