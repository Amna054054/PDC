# PDC
chapter 1 code
Two concepts are applied in this code:

- `time` → used to create delays and measure how long tasks take.  
- `threading` → used to run multiple tasks at the same time (parallel execution).  

 **Sequential Process:**  
   - Code runs **line by line**, one after another.  
   - First, Task 1 starts → waits 2 seconds → completes.  
   - Then, Task 2 starts → waits 2 seconds → completes.  
   - Total time ≈ **4 seconds (2 + 2)** because both tasks run one after another.  

**Threaded Process:**  
   - Two threads are created using `threading.Thread()`.  
   - Both threads start **simultaneously** using `t1.start()` and `t2.start()`.  
   - The program waits for both threads to finish using `t1.join()` and `t2.join()`.  
   - Since both run together, total time ≈ **2 seconds** only.  

**`time.sleep(2)` Function:**  
   - Makes the program pause for 2 seconds.  
   - Used to simulate a real task or waiting period.  

**`time.time()` Function:**  
   - Records start and end time of execution.  
   - Calculates total time taken by finding the difference between them.  

**Purpose of Threads:**  
   - Makes the program **faster and more efficient**.  
   - Useful when multiple tasks can run independently.

