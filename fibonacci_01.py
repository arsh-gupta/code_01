x = int(input("Enter no. of Elements : "))
f=1
s=1
for i in range(x):
    print(f,end = ' ')
    t = f+s
    f = s
    s = t
