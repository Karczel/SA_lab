import concurrent.futures

from pipeline_app import *


def main():
    min_val, max_val, amount = 1, 1000, 1000

    with concurrent.futures.ProcessPoolExecutor() as executor:
        future_nums = executor.submit(gen_nums, min_val, max_val, amount)  # Generate numbers in parallel
        nums = future_nums.result()

        # Process filtering and squaring in parallel
        future_filtered = executor.submit(even_filter, nums)
        future_squared = executor.submit(square, future_filtered.result())

        squared_nums = future_squared.result()

    output(squared_nums)


if __name__ == "__main__":
    main()
