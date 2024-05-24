import threading

CONST = [10]

def sum(CONST):
    for i in range(1000000):
        CONST[0] += 1

num_threads = int(input())

threads = []
for i in range(num_threads):
    thread = threading.Thread(target=sum, args=(CONST,))
    threads.append(thread)
    thread.start()

print(CONST[0])
