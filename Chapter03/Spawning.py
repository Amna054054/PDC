import multiprocessing

def myFunc(i):
    print(f'Process {multiprocessing.current_process().name} running with arg: {i}')

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()