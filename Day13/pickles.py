import pickle
import os

file_name="username.pkl"

def saved_name ():
    name=input("Enter Your Name : ")
    with open(file_name,"wb") as file:
        pickle.dump(name,file)
    print("!!!Successfully Logged in!!!!")

def loaduser():
    with open(file_name,"rb") as file:
        name = pickle.load(file)
    return name
     
if os.path.exists(file_name):
   name=loaduser()
   print("Hai",name,"Welcome Back!")
else:
   saved_name()   
   

          

