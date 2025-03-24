# Remove Duplicates from a List
# Removes duplicate elements from a list while preserving unique elements
def remove_duplicates(input_list):
    return list(set(input_list))
input_list = [1, 2, 2, 3, 4, 4]
print(remove_duplicates(input_list)) 
