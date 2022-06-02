s1=input("ENTER FIRST STRING:-")
s2=input("ENTER SECOND STRING:-")
ch=int(input("ENTER THE CHARACTERS TO BE SWAP:-"))
x1=s2[0:ch]+s1[ch:]
x2=s1[0:ch]+s2[ch:]
print(x1)
print(x2)
