import os
#define the file name to store the task
file_name='task.txt'

#Function for load task 
def load():
    if not os.path.exists(file_name):
        return []
    with open(file_name,"r") as file:
     return file.readlines()  
   
to_do = load()

#Function for save task
def saved():
   with open(file_name,"w") as file:
      for i in to_do:
         file.write(i + "\n")
       

#Function for ADD Task
def add():
    task=input("Enter the task to add:")
    to_do.append(task)
    saved()
    print("Task added!")

#Function for View Task
def view():
  if len(to_do) == 0:
    print("!!Empty List!!")
  else: 
    
    print("TO DO LIST"+"\n"+"----------")
    for x in to_do:
       print(x)
    
#Function for Delete Task
def pop():
    n=int(input("Enter the task to delete :"))
    if n>len(to_do) or n<1:
       print("!!Invalid Task number you entered!!")
    else:
        to_do.pop(n-1)
        saved()
        print("!!Entered Task deleted!!")
        
    return to_do
    #return add()

#Main loop to interact with the user
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
    


    