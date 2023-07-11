""" print("hello",end="\t")
print("program")
empid =100
print(empid) """
# add program
""" num1 =6
num2 =4
r=num1+num2
print(r) """
# + - * /(float) //(int) %
# += -= *= /= //= %=

""" num1 =8
num1+=3
print(num1) """

# > < >= <= != == true false
""" num1 =5
num2 =7
print(num1>num2) """

# and or not
#num1 =5
#num2 =7
#print(num1>10 and num2<10)
#print(num1>10 or num2<10)
#print(not(num1>num2))


""" if False:
    print("true")

n =10
if n>=10:
    print("num is 10")
pin = 190
if pin ==100:
    print("login")
else:
    print("not login")
 """
""" 
user =  input("enter username")
if user =="admin":
    password = input("enter password")
    if password =="admin123":
        print("login")
    
    else:
        print("enter right password")
else:
    print("enter right user") """
""" 
user = input ("enter user & email")
if(user == "admin"):
    print("login")
elif user == "admin@gmail.com":
    print("login")
else:
    print("not login") """
    
""" print("1")
print("2")
print("3") """

# loop while
# 1 2 3 4 5
# start i=1   end i<=5
""" 
i=1
T=4
while i<=10:
    print(i*T)
    i+=1



i=1
sum1=0
while i<=10:
    if i%2==0:
        sum1 =sum1+i
    i+=1
print(sum1)

num =int(input("enter number"))

output 246 """


#  i=0, i+=1, i<10
""" for  num in range(1,10,2):
    print(num) """
    
#list  []
data =[1,5,2,6]
      # 0  1 2 3
      #-4 -3-2-1       
#print(data)
""" 
add=0
for data1 in data:
    print(data1)
    add=add+data1
print(add) """

""" print(sum(data))
print(max(data))
print(min(data))
print(len(data)) """

""" data.append(7)
print(data)
data.insert(2,5)
print(data)
data.pop()
print(data) """


""" user =["user1","user2"]
password =[123,456]
while True:
    username =input("Enter name")
    pos =user.index(username)
    if username in user:
        password1=int(input("Enter password"))
        if password1 == password[pos]:
            print("login")
            break
            
    else :
        print("not login")
 """
""" 
for i in range(10):
    print(i)     
 
for i in range(2,10):
    print(i)
for i in range(2,10,2):
    print(i) """
    
#list  []

#dict { key :value}

""" 
data = {"id1":1,"uname":"user","age":30}
print(data)
print(data["id1"])
print(data["uname"]) """
""" data = {"id":[3,4,5],"name":["user1","user2","user3"]}
data["salary"]=[300,400,500]
print(data)
data.update({"dept":["it","sal","acc"]})
print(data)
data.pop("name")
print(data)
print(data.items()) """




""" print(data["name"])
print(data.keys())
print(data.values())
for d in data:
    print(d)
for d in data.keys():
    print(d)
    print(d)
for d in data.values():
    print(d) """
""" for d in data.keys():
    print(d)
    if d=="name":
        while True:
            name1 =input("enter name")
            print("**************")
            print(d)
            if name1 in data[d] :
                print("login")
                break
 """        
 
 
 #data = {key:value}
"""  
data ={"id":1,"name":"user","salary":400}
print(data)
for d in data:
    print(d)
for d in data.keys():
    print(d)
print("******************")
for d in data.values():
    print(d)
print("******************")
for d in data.items():
    print(d)
data["age"] =40
print(data)
print("******************")
print(data['name'])
print("******************")
data.update({"dept":"it"})
print(data)
 """""" 
data = {"id":[1,2,3],"name":["user1","user2","user3"]}
print(data)
print(data['id']) """
#id=[1,2,3,4]
#name["user1","user2","user3","user4"]

dataset ={
    "user":["user1","user2"],
    "password":["1234","5678"],
    "product":["product1","product2"],
    "rate":[300,400],
}

while True:
   
    print("*********************")
    name = input("enter name")
    pos =-1
    for i in dataset["user"]:
        pos = pos+1
        if(name == i):
            password = input("enter password")
            if( password==dataset["password"][pos]):
                print("user login")
                for j in range(len(dataset['product'])):
                   
                    print(dataset["product"][j],"",dataset["rate"][j])
                break
                    
            
            
        
