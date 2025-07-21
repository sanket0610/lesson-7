
print("Enter marks for 3 subjects")
m1=int(input())
m2=int(input())
m3=int(input())

t=m1+m2+m3
av=t/3

if av>=80 and av<=100:
    print("Grade A")
elif av>=50 and av<=79:
    print("Grade B")
else:
    print("Grade C")