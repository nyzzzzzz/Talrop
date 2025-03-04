import requests

url='https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
#print(response)
x=response.json()
#print(x)
i=1
for a in x:
    print(i,".","Name :",a["name"],"\n","username :",a["username"],"\n","email :",a["email"],"\n","Address :",a["address"]["street"],"\n","City :",a["address"]["city"],"\n","phone :",a["phone"],"\n","website :",a["website"])
    i+=1
    print("\n")
