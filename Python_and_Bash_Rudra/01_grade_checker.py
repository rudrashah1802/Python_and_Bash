marks=(int(input("Enter Marks ")))
if(marks>100 or marks<0):
    print("Invalid input")
elif(marks>=90):
    print("Your Grade is A")
elif(marks>=80 and marks<=89):
    print("Your Grade is B")
elif(marks>=70 and marks<=79):
    print("Your Grade is C")
elif(marks>=60 and marks<=69):
    print("Your Grade is D")
else:
    print("Your Grade is F")