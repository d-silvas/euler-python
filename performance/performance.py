import time

class Performance:
    init_time: int

    def start(self):
        self.init_time = time.perf_counter_ns()

    def end(self):
        end_time = time.perf_counter_ns()
        print(f'{(end_time - self.init_time)/1000}ms')
