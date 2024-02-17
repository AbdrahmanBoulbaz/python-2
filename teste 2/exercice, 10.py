def ft_progress(lst):
    total_items = len(lst)
    for index, item in enumerate(lst):
        yield (index + 1) / total_items * 100, item
my_list = range(100)
for progress, item in ft_progress(my_list):
    print(f"Progress: {progress:.2f}%, Current Item: {item}")
