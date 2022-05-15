String="Python is a case sensitive language"
print(String)
print("Length of the string:",len(String))
print("Reverse of the string:",String[::-1])
String2=String[10:-9]
print("The specified part:",String2)
print("String after replacement",String.replace("a case sensitive","object oriented"))
print("The index of 'a' is",String.index('a'))
print("String without space",String.replace(" ",""))
