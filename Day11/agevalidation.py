age=int(input("Enter the age :"))
try:
    if age<18:
        raise Exception("!!!Sorry you are not Eligible !!!!")
    else:
        print("You are Eligible")
except Exception as e:
    print(e) 