#4.	Write a recursive function to print Fibonacci series upto n terms.

def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=" ")
    fibonacci(n - 1, b, a + b)


# Example
fibonacci(7)