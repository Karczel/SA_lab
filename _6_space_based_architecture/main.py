from space_based_architecture import DataGrid, LoadBalancer


# Run the simulation
if __name__ == "__main__":
    GRID_SIZE = 10  # Size of the shared data grid
    NUM_NODES = 3  # Number of processing units
    NUM_TASKS = 5  # Number of tasks to distribute

    shared_data = DataGrid(GRID_SIZE)
    print(f"Initial Data Grid: {list(shared_data.data_grid)}\n")

    load_balancer = LoadBalancer(shared_data, NUM_NODES, NUM_TASKS)
    load_balancer.start()

    print(f"\nFinal Data Grid: {list(shared_data.data_grid)}")
