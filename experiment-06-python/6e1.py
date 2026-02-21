'''1.	Write a Python function to find the maximum and minimum numbers from a sequence of numbers. 
 (Note: Do not use built-in functions.)
'''
def find_max_min(seq):
    max_val = seq[0]
    min_val = seq[0]

    for num in seq:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val


# Example
print(find_max_min([10, 6, 8, 90, 12, 56]))