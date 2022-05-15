Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A1=int(input("Enter the 1st side of triangle: "))
A2=int(input("Enter the 2nd side of triangle: "))
A3=int(input("Enter the 3rd side of triangle: "))
A4=max(A1,A2,A3)
A5=A1+A2+A3
A6=A5-A4
while(A6>A4):
    print("Triangle can be formed")
    break
while(A6<=A4):
    print("Triangle can not be formed")
    break