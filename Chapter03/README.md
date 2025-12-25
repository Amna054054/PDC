# Chapter 03

Killing Processes:


<img width="1079" height="332" alt="image" src="https://github.com/user-attachments/assets/c310e780-4660-4ede-b42f-a72c18ff1d91" />


Processes may need to be killed to free system resources, avoid hangs, and keep the system running smoothly. terminate() stops a process instantly, while is_alive(), exitcode, and join() help monitor and clean up after it. An exit code of 0 means success, a positive value shows an error, and a negative value indicates termination by a signal.

Naming Processes:


<img width="788" height="377" alt="naming py" src="https://github.com/user-attachments/assets/17e314af-db5e-4392-8199-4464649efb45" />


Naming processes improves debugging, clarity, and log readability when working with multiple processes. You can assign custom names using the name parameter and retrieve them inside the target function with current_process().name. After naming, simply start and join the processes to run and synchronize them.

Spawning Processes:


<img width="828" height="201" alt="spawning py" src="https://github.com/user-attachments/assets/fc99281e-1276-4b47-a7c9-d105342e3c8f" />


Spawning a process means creating a child process that runs independently of the parent. The parent can continue execution or wait for the child using join(). A process is spawned by defining it with multiprocessing.Process, starting it with start(), and synchronizing with join().

Run_Background_Processes:


![alt text](image.png)



![alt text](image-1.png)


Background processing lets tasks run without user interaction, often as daemons in Unix/Linux or system-tray processes in Windows. In Python, daemon=True creates background processes that end automatically with the parent, while daemon=False makes them independent. Daemon processes are useful for lightweight tasks but cannot spawn child processes and inherit their daemon state from the parent.


Pipe Processes:


![alt text](image-2.png)


A Pipe in multiprocessing allows communication between two processes, either one-way or bidirectional. Using multiprocessing.Pipe(duplex=True), you get two connected Connection objects for sending and receiving data. Pipes are useful for exchanging data directly, such as sending numbers from one process for processing in another.


Queue Processes:


![alt text](image-3.png)


A Queue in multiprocessing is a FIFO structure used to safely exchange data between processes, commonly solving producer-consumer problems. Producers put data in the queue while consumers retrieve and process it, helping avoid deadlocks. JoinableQueue adds task_done() and join() methods to track and wait for all tasks to complete.


Process_Pool:


![alt text](image-4.png)


A process pool lets you run the same function on multiple inputs in parallel, enabling data parallelism. Methods like apply() and map() are blocking (synchronous), while apply_async() and map_async() are non-blocking, allowing background execution. map() and map_async() efficiently distribute multiple inputs across processes for parallel computation.


Processes_Barrier:


![alt text](image-5.png)


A Barrier synchronizes multiple processes by dividing a program into phases. All processes must reach the barrier before any can proceed. Code after the barrier runs only once all processes have completed the preceding phase.


Process_In_Subclass


![alt text](image-6.png)


A subclass inherits properties and methods from a superclass, allowing reuse and customization. It can override methods to provide specific behavior. In multiprocessing, overriding the run(self) method defines the code executed when the process starts, such as printing the process name.





