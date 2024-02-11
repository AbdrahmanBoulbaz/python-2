def ft_tqdm(iterable):
    total = len(iterable)
    progress = 0
    for item in iterable:
        yield item
        progress += 1
        progress_percent = progress / total * 100
        print(f"Progress: {progress_percent:.2f}% ({progress}/{total})", end='\r')

# Example usage:
if __name__ == "__main__":
    import time

    # Dummy iterable (e.g., range, list, etc.)
    items = range(100)

    # Iterate over items using ft_tqdm
    for item in ft_tqdm(items):
     for item in (items):
        # Simulate some processing time
        time.sleep(0.1)
        