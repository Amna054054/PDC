Chapter 03 CODES 

Killing Processes:


<img width="1079" height="332" alt="image" src="https://github.com/user-attachments/assets/c310e780-4660-4ede-b42f-a72c18ff1d91" />


Processes may need to be killed to free system resources, avoid hangs, and keep the system running smoothly. terminate() stops a process instantly, while is_alive(), exitcode, and join() help monitor and clean up after it. An exit code of 0 means success, a positive value shows an error, and a negative value indicates termination by a signal.

Naming Processes:


<img width="788" height="377" alt="naming py" src="https://github.com/user-attachments/assets/17e314af-db5e-4392-8199-4464649efb45" />


Naming processes improves debugging, clarity, and log readability when working with multiple processes. You can assign custom names using the name parameter and retrieve them inside the target function with current_process().name. After naming, simply start and join the processes to run and synchronize them.

Spawning Processes:


<img width="828" height="201" alt="spawning py" src="https://github.com/user-attachments/assets/fc99281e-1276-4b47-a7c9-d105342e3c8f" />


Spawning a process means creating a child process that runs independently of the parent. The parent can continue execution or wait for the child using join(). A process is spawned by defining it with multiprocessing.Process, starting it with start(), and synchronizing with join().







