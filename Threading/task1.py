import threading

class Counter(threading.Thread):
    counter = 0
    rounds = 100_000
    lock = threading.Lock()

    def __init__(self):
        super().__init__()

    def run(self):
        for _ in range(Counter.rounds):
            with Counter.lock:
                Counter.counter += 1

t1 = Counter()
t2 = Counter()

t1.start()
t2.start()

t1.join()
t2.join()
