#Merge Two Dictionaries
#Combines two dictionaries into a single dictionary while maintaining key-value pairs.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)  
