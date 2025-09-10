attendence=int(input("enter your attendence: "))
medical=input("did you have a medical cause ")

if medical == "yes":
    print("you're allowed to attend the exam")
else:
    if attendence>=75:
        print("you're allowed to attend the exam")
    else:
        print("you're not allowed to attend the exam")