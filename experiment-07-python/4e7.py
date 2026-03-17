# =========================
# Q4. Exception handling for division
# =========================

n = int(input("Enter number of test cases: "))

for _ in range(n):
    try:
        a, b = input().split()
        a = int(a)
        b = int(b)
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)