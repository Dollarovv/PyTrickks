def list_comprehension_example():
    return [x**2 for x in range(10)]

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]
