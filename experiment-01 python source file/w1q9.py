#wap to print truth table for (&, |, ^) operators
print("A\tB\tA&B\tA|B\tA^B")
for A in [0, 1]:
    for B in [0, 1]:
        print(f"{A}\t{B}\t{A & B}\t{A | B}\t{A ^ B}")