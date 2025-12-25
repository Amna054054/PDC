# Chapter 05
asyncio_event_loop:


![alt text](image.png)


This program uses an event loop with scheduled callbacks (call_later, call_soon) to repeatedly run three tasks (A → B → C → A → …). Each task prints its name, sleeps for a random time, and then schedules the next task to run 1 second later. The loop keeps cycling through the three tasks for 60 seconds, after which the event loop stops.


asyncio_futures:


![alt text](image-1.png)


This program uses asyncio coroutines to run two computations concurrently without blocking.
One coroutine calculates the sum of N integers, while the other computes the factorial, both simulating delay with asyncio.sleep().When each coroutine finishes, its result is stored in a Future and printed using a callback.


asyncio_coroutine:


![alt text](image-2.png)


This code shows a Finite State Machine (FSM) using Python's asyncio coroutines.
It defines five states (start_state, state1, state2, state3, end_state) that transition randomly based on randint(0,1).
Each state prints its current status, waits for 1 second (time.sleep(1)), and yields control to the next state using yield from.
The simulation starts at start_state and continues through random transitions until reaching end_state, where it stops.


asyncio_task_manipulation:


![alt text](image-3.png)


This code implies that running three mathematical computations in parallel using asyncio.Task.
It defines coroutines for factorial, fibonacci, and binomial coefficient, each printing intermediate steps and pausing 1 second per iteration using yield from asyncio.sleep(1).
The task_list creates separate asyncio tasks for each function, allowing them to execute concurrently.
Finally, the event loop runs until all tasks are complete using asyncio.wait(task_list), then closes the loop.


concurrent_futures_pooling:


![alt text](image-4.png)


This code compares sequential, multithreading, and multiprocessing execution for a CPU-intensive task. The count function performs a heavy loop, and evaluate prints the result for each number in number_list. Sequential execution processes each item one by one and measures the time taken. ThreadPoolExecutor runs evaluate on multiple threads concurrently, which may not significantly speed up CPU-bound tasks due to Python’s GIL. ProcessPoolExecutor runs evaluate in multiple processes, effectively leveraging multiple CPU cores and typically giving the best speedup for CPU-bound operations.

