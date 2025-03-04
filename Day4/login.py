#Hardcoded username/password
username="admin"
password="123"
#user input
usrname=input('Enter your Username: ')
passwrd=input('Enter your Password: ')

#Authentication check
if usrname==username and passwrd!=password:
    print("Password incorrect")
elif usrname!=username and passwrd==password or passwrd!=password:
    print("User not Found")
elif usrname==usrname and passwrd==password:
    print("Login sucessfully")    
else:
    print("Login failed")