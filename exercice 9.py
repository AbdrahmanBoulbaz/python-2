def print_null_types():
    null_types = [None, "", [], {}, (), set(), 0, 0.0]
    try:
        for null in null_types:
            print(type(null))
        return 0
    except Exception as e:
        print("Error:", e)
        return 1
if __name__ == "__main__":
    exit_code = print_null_types()
    exit(exit_code)