from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("my rank is :", rank)

if rank == 0:
    data = 10000000
    destination_process = 2    # FIXED (must be < 4)
    comm.send(data, dest=destination_process)
    print("sending data %s to process %d" % (data, destination_process))

if rank == 1:
    destination_process = 3    # FIXED (must be < 4)
    data = "hello"
    comm.send(data, dest=destination_process)
    print("sending data %s to process %d" % (data, destination_process))

if rank == 2:
    data = comm.recv(source=0)
    print("data received is = %s" % data)

if rank == 3:
    data1 = comm.recv(source=1)
    print("data1 received is = %s" % data1)
