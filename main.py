#Exercise 2, Faulty Calculator
# 45*3=555 , 56+9=77, 56/6=4
#Design a calculator which will correctly solve all the problem except the following one
#your program should take operator and the two numbers as input from user and then return the result

a=int(input("Enter first number"))
b=int(input("Enter second number"))
print("1. Addition \n 2. Subtraction \n 3. multiplication \n 4. division")
print("Enter your choice")
c=input()
if c=="1":
      if a==56 and b==9:

            print(" Ans: 77")
      else:
            print("Ans:",a+b)
elif c=="2":
      print("Ans:",a-b)
elif c=="3":
      if a==45 and b==3:
            print("Ans: 555")
      else:
            print("Ans:",a*b)
elif c=="4":
      if a==56 and b==6:
            print("Ans: 4.0")
      else:
            print("Ans:",a/b)
else:
    print("Invalid choice")
