#Find the Second Largest Number in a List
#Finds the second highest number from a list of integers.

def second_largest(numbers):
    unique_numbers = list(set(numbers)) 
    if len(unique_numbers) < 2:
        return None 
    unique_numbers.sort(reverse=True)  
    return unique_numbers[1]  
numbers = [10, 20, 4, 45, 99, 99, 5]
print(second_largest(numbers)) 
