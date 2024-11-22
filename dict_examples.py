from tricks.dict_tricks import merge_dicts, invert_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

print("Merged Dictionary:", merge_dicts(dict1, dict2))
print("Inverted Dictionary:", invert_dict(dict1))
