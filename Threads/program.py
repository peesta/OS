import threading
import os

def print_mess(thread_id):
    pid = os.getpid()
    message = f"Process {pid}, {thread_id}"
    for i in range(10):
        print(message)

num_threads = int(input())

threads = []
for i in range(num_threads):
    thread = threading.Thread(target=print_mess, args=(i,))
    threads.append(thread)
    thread.start()
