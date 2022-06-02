rollno=int(input("ENTER YOUR UNIVERSITY ROLL NUMBER:-"))
p=rollno%10
rollno=rollno//10
a=rollno%10
rollno=rollno//10
b=rollno%10
res=p+a+b
print("SUM OF LAST THREE DIGITS OF UNI. ROLL NO. IS=%d"%res)
