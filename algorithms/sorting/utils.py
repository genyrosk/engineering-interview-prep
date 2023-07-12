def check_sorting_algo(sort_func):
    data = [
        ([1, 3, 2], [1, 2, 3]),
        ([1, 4, 2, 5, 1], [1, 1, 2, 4, 5]),
        ([6, 5, 4, 3, 1, 3], [1, 3, 3, 4, 5, 6]),
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ]
    for unsorted, sorted in data:
        print("")
        print("Input:", unsorted)
        out = sort_func(unsorted)
        print("Output:", out)
        print(
            "Passed"
            if out == sorted
            else "=================\n================= Failed!!!\n================="
        )
