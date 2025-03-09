import multiprocessing
import random
import time


class DataGrid:
    def __init__(self, size):
        self.data_grid = multiprocessing.Array('i', [random.randint(1, 10) for _ in range(size)])

    def __getitem__(self, index):
        return self.data_grid[index]

    def __setitem__(self, index, value):
        self.data_grid[index] = value

    def __len__(self):
        return len(self.data_grid)

# Processing Unit (Node)
class ProcessingUnit(multiprocessing.Process):
    def __init__(self, node_id, data_grid, task_queue, lock):
        super().__init__()
        self.node_id = node_id
        self.data_grid = data_grid
        self.task_queue = task_queue
        self.lock = lock

    def run(self):
        while True:
            index = self.task_queue.get()
            if index is None:
                break  # Stop condition

            with self.lock:  # Ensure safe access to shared data
                old_value = self.data_grid[index]
                new_value = old_value + 9  # Simulating some processing
                self.data_grid[index] = new_value

            print(f"Node {self.node_id} processing data at index {index}: {old_value} -> {new_value}")
            time.sleep(random.uniform(0.5, 1.5))  # Simulate processing time

# Load Balancer (Round Robin)
class LoadBalancer:
    def __init__(self, data_grid, num_nodes, num_tasks):
        self.data_grid = data_grid
        self.num_nodes = num_nodes
        self.num_tasks = num_tasks
        self.task_queue = multiprocessing.Queue()
        self.lock = multiprocessing.Lock()

    def start(self):
        nodes = [ProcessingUnit(i, self.data_grid, self.task_queue, self.lock) for i in range(self.num_nodes)]

        for node in nodes:
            node.start()

        # Distribute tasks in round-robin fashion
        for task_id in range(self.num_tasks):
            index = random.randint(0, len(self.data_grid) - 1)
            self.task_queue.put(index)

        # Send stop signal to nodes
        for _ in nodes:
            self.task_queue.put(None)

        for node in nodes:
            node.join()
