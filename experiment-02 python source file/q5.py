#check weather the quadratic equation has real roots,imaginaary roots or equal roots.display the roots accordingly
a=int(input("Enter coefficient a: "))
b=int(input("Enter coefficient b: "))
c=int(input("Enter coefficient c: "))
d=b**2-4*a*c
if d>0:
    r1=(-b+d**0.5)/(2*a)
    r2=(-b-d**0.5)/(2*a)
    print("the roots are real and different")
    print("roots are:",r1,"and",r2)
elif d==0:
    r=-b/(2*a)
    print("the roots are real and equal")
    print("root is:",r)
else:   
    print("the roots are imaginary")
    real_part=-b/(2*a)
    imag_part=(abs(d)**0.5)/(2*a)
    print("roots are:",real_part,"+",imag_part,"i and",real_part,"-",imag_part,"i")
