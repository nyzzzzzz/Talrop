#create List
to_do=[]
#Declare Function for ADD Task
def add():
    task=input("Enter the task to add:")
    to_do.append(task)
    print("Task added!")

#Declare Function for View Task
def view():
  if len(to_do) == 0:
    print("!No Data!")
  else:        
    print(to_do) 

#Declare Function for Delete Task
def pop():
    n=int(input("Enter the task to delete :"))
    if n>len(to_do) or n<1:
       print("!!Invalid Task number you entered!!")
    else:
        to_do.pop(n-1)
        print("!!Entered Task deleted!!")
    return to_do
    #return add()

#To check condition true
while True:
 print("1.Add","2.View","3.Delete","4.Exit")
 choice=input("choose the option :")      
 if choice=="1":
    add()
 elif choice=="2":
    view()
 elif choice=="3":
    pop()
 elif choice=="4":
    print("!!!See You Later!!!")
    break
 else:
    print("Invalid")   
    


    