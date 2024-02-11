def print_null_types():
    try:
        print("Type of None:", type(None))
        return 0
    except Exception as e:
        print("Error:", e)
        return 1 ,
print_null_types()