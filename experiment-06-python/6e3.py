'''3.	Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
'''
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n)
# Example
print_1_to_n(5)