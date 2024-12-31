age=int(input("Enter Age:"))
if(age<18):
    print("You are not eligible to drive")
elif(age>=18):
    if(age<19):
        print("trainee")
    elif(age<=25):
        print("young driver")
    else:
        print("experienced driver")
else:
    print("Invalid input")